#!/usr/bin/python
import sys
from math import sin, cos, radians

def convert2cif(file_name, rot=0):

    with open(file_name,'r') as fp:
        #read in file
        f = fp.read()

    outfile_name = file_name + "_coords.cif"

    linelist = f.split('\n')
    elems = []
    x = []
    y = []
    z = []

    for line in linelist[2:-1]:
        elems.append( line.split()[0] )
        x.append( float(line.split()[1]) )
        y.append( float(line.split()[2]) )
        z.append( float(line.split()[3]) )

    xlim = max(x) - min(x)
    ylim = max(y) - min(y)
    zlim = max(z) - min(z)

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

    for i,elem in enumerate(elems):
        x[i] /= xlim
        y[i] /= ylim
        z[i] /= zlim
        print("%s %1.6f %1.6f %1.6f %1.6f" % (elem, x[i]*cos(radians(rot))
            - y[i]*sin(radians(rot)), x[i]*sin(radians(rot)) + y[i]*cos(radians(rot))
            , z[i], 1), file=fp)

    fp.close()
#convert2cif(sys_name)
if __name__ == "__main__" :
    convert2cif(sys.argv)
