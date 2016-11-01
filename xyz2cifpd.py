#!/usr/bin/env python3
import sys
import re
import tkinter as tk
import pandas as pd

from tkinter import filedialog
from numpy import array, dot, min as nmin, max as nmax
from pandas.io.parsers import read_csv
from math import sin, cos, radians

pattern = re.compile(r"""(\w+).xyz""", re.VERBOSE)


def write_header(outfile_name, header):
    with open(outfile_name, 'w') as fp:
        fp.write(header)


def openFileDialogue():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def convert2cif(file_name, rot=0):
    rot = float(rot)
    df = read_csv(file_name, skiprows=2, header=None, delim_whitespace=True)

    elemArray = df.values[:, 0].astype(str, copy=False)
    coordArray = df.values[:, 1:].astype(float, copy=False)

    outfile_name = file_name + "_coords.cif"

    trans = array([[cos(radians(rot)), -sin(radians(rot)), 0],
                   [sin(radians(rot)), cos(radians(rot)),  0],
                   [0,                 0,                  1]])
    coordArray = dot(coordArray, trans)

    x = coordArray[:, 0]
    y = coordArray[:, 1]
    z = coordArray[:, 2]

    xlim = nmax(x) - nmin(x)
    ylim = nmax(y) - nmin(y)
    zlim = nmax(z) - nmin(z)

    x -= nmin(x)
    x /= xlim
    y -= nmin(y)
    y /= ylim
    z -= nmin(z)
    z /= zlim

    header = """data_{file_name}_phase

_symmetry_space_group_name_H-M   'P 1'
_cell_length_a  {xlim:>3.10f}
_cell_length_b  {ylim:>3.10f}
_cell_length_c  {zlim:>3.10f}
_cell_angle_alpha  90.00
_cell_angle_beta   90.00
_cell_angle_gamma  90.00

loop_
_symmetry_equiv_pos_as_xyz
    'x, y, z'
loop_
    _atom_site_label
    _atom_site_fract_x
    _atom_site_fract_y
    _atom_site_fract_z
    _atom_site_occupancy
    _atom_site_type_symbol
""".format(file_name=file_name, xlim=xlim, ylim=ylim, zlim=zlim)

    write_header(outfile_name, header)

    df = pd.DataFrame({'elem': elemArray, 'x': x, 'y': y, 'z': z})
    df = df[df != 1].dropna()
    df['occ'] = 1.0
    df['label'] = df['elem']

    df.to_csv(outfile_name, mode='a', header=False,
              float_format='%.10f', index=False, sep=" ", escapechar=" ")


if __name__ == "__main__":
    rot = 0.0
    if len(sys.argv) == 3:
        fname = sys.argv[1]
        rot = sys.argv[2]
    elif len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = openFileDialogue()

    convert2cif(fname, rot)
