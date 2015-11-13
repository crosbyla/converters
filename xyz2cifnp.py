#!/usr/bin/python
import sys
import numpy as np
from math import sin, cos, radians

def convert2cif(file_name, rot=0):

    elemArray = np.genfromtxt(file_name, skiprows=2, usecols=(0,), dtype=str)
    coordArray = np.loadtxt(file_name, skiprows=2, usecols=(1,2,3))

    outfile_name = file_name + "_coords.cif"

    trans = np.array([  [cos(radians(rot)), -sin(radians(rot)), 0],
                        [sin(radians(rot)), cos(radians(rot)), 0],
                        [0, 0, 1] ])
    x = coordArray[:,0]
    y = coordArray[:,1]
    z = coordArray[:,2]

    xlim = np.max(x) - np.min(x)
    ylim = np.max(y) - np.min(y)
    zlim = np.max(z) - np.min(z)

    x /= xlim
    y /= ylim
    z /= zlim

    coordArray = np.dot(coordArray,trans)

    fp = open(outfile_name,'w')
    print("data_"+file_name+"_phase\n", file=fp)
    print("_symmetry_space_group_name_H-M   'P 1'", file=fp)

    print("%s %f" % ( '_cell_length_a' , xlim ), file=fp)
    print("%s %f" % ( '_cell_length_b' , ylim ), file=fp)
    print("%s %f" % ( '_cell_length_c' , zlim ), file=fp)

    print("%s %f" % ( '_cell_angle_alpha' , 90) , file=fp)
    print("%s %f" % ( '_cell_angle_beta' , 90) , file=fp)
    print("%s %f" % ( '_cell_angle_gamma' , 90) , file=fp)

    print("\nloop_\n    _atom_site_type_symbol", file=fp)
    print("    _atom_site_fract_x", file=fp)
    print("    _atom_site_fract_y", file=fp)
    print("    _atom_site_fract_z", file=fp)
    print("    _atom_site_occupancy", file=fp)

    for i, elem in enumerate(elemArray[:]):
        print("%s %1.6f %1.6f %1.6f %1.6f" % (elem, x[i], y[i], z[i], 1.0),
            file=fp)

    fp.close()
#convert2cif(sys_name)
if __name__ == "__main__" :
    convert2cif(sys.argv)
