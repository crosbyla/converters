#!/usr/bin/env python3
import sys
from numpy import array, dot, min as nmin, max as nmax
from pandas.io.parsers import read_csv
from math import sin, cos, radians

def convert2cif(file_name, rot=0):
    rot = float(rot)
    df = read_csv(file_name, skiprows=2, header=None, delim_whitespace=True)

    elemArray = df.values[:,0].astype(str, copy=False)
    coordArray = df.values[:,1:].astype(float, copy=False)

    outfile_name = file_name + "_coords.cif"

    trans = array([     [cos(radians(rot)), -sin(radians(rot)), 0],
                        [sin(radians(rot)), cos(radians(rot)), 0],
                        [0, 0, 1] ])
    coordArray = dot(coordArray,trans)

    x = coordArray[:,0]
    y = coordArray[:,1]
    z = coordArray[:,2]

    xlim = nmax(x) - nmin(x)
    ylim = nmax(y) - nmin(y)
    zlim = nmax(z) - nmin(z)

    x -= nmin(x)
    x /= xlim
    y -= nmin(y)
    y /= ylim
    z -= nmin(z)
    z /= zlim


    fp = open(outfile_name,'w')
    print(''.join("data_" + file_name + "_phase\n"), file=fp)
    print("_symmetry_space_group_name_H-M   'P 1'", file=fp)

    print("%s %f" % ( '_cell_length_a' , xlim ), file=fp)
    print("%s %f" % ( '_cell_length_b' , ylim ), file=fp)
    print("%s %f" % ( '_cell_length_c' , zlim ), file=fp)

    print("%s %f" % ( '_cell_angle_alpha' , 90) , file=fp)
    print("%s %f" % ( '_cell_angle_beta' , 90) , file=fp)
    print("%s %f" % ( '_cell_angle_gamma' , 90) , file=fp)

    print("\nloop_\n_symmetry_equiv_pos_as_xyz", file=fp)
    print("    'x, y, z'", file=fp)

    print("\nloop_\n    _atom_site_label", file=fp)
    print("    _atom_site_fract_x", file=fp)
    print("    _atom_site_fract_y", file=fp)
    print("    _atom_site_fract_z", file=fp)
    print("    _atom_site_occupancy", file=fp)
    print("    _atom_site_type_symbol", file=fp)

    for i, elem in enumerate(elemArray[:]):
        print("%s %1.6f %1.6f %1.6f %1.6f %s" % (elem, x[i], y[i], z[i], 1.0, elem),
            file=fp)

    fp.close()

if __name__ == "__main__" :
    if len(sys.argv) == 3:
        convert2cif(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        convert2cif(sys.argv[1])
    else :
        raise ValueError
