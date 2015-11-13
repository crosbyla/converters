#!/usr/bin/python
import sys
import numpy as np
from math import sin, cos, radians

def convert2cif(file_name, rot=0):
    print(file_name)

    elemArray = np.loadtxt(file_name, skiprows=2, usecols=(0,), dtype='S2')
    coordArray = np.loadtxt(file_name, skiprows=2, usecols=(1,2,3))

    outfile_name = file_name + "_coords.cif"

    trans = np.array([  [cos(radians(rot)), -sin(radians(rot)), 0],
                        [sin(radians(rot)), cos(radians(rot)), 0],
                        [0, 0, 1] ])

    x = coordArray[:,0], y = coordArray[:,1], z = coordArray[:,2]

    xlim = np.max(x) - np.min(x)
    ylim = np.max(y) - np.min(y)
    zlim = np.max(z) - np.min(z)

    x /= xlim
    y /= ylim
    z /= zlim

    coordArray = np.dot(coordArray,trans)


           print("%s %1.6f %1.6f %1.6f" % (elem, x*cos(radians(rot))
                - y*sin(radians(rot)), x*sin(radians(rot)) + y*cos(radians(rot))
                , z), file=fp)

    fp.close()
#convert2cif(sys_name)
if __name__ == "__main__" :
    convert2cif(sys.argv)