#!/usr/bin/python
import sys
import numpy as np
from math import sin, cos, radians

def convert2cif(file_name, rot=0):
    print(file_name)
    with open(file_name,'r') as fp:
        #read in file
        f = fp.read()

    outfile_name = file_name + "_coords.cif"
    fp = open(outfile_name,'w')

    linelist = f.split('\n')
    coorArray = [ line.split() for line in linelist[2:-1] ]
    np.arra
    for line in coorArray:
        try :
           coords = zip((str,float,float,float),line.split())
           (elem, x, y, z) = [u(v) for u,v in coords] # extracts one line from file
           print("%s %1.6f %1.6f %1.6f" % (elem, x*cos(radians(rot))
                - y*sin(radians(rot)), x*sin(radians(rot)) + y*cos(radians(rot))
                , z), file=fp)

        except ValueError:
            raise

    fp.close()
#convert2cif(sys_name)
if __name__ == "__main__" :
    convert2cif(sys.argv)
