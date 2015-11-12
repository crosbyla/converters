#!/usr/bin/python

def convert2cif(file_name):
    with open(file_name) as fp:
        #read in file
        f = fp.read()
    linelist = f.split('\n')

    outfile_name = file_name + "_coords.cif"
    fp = open(outfile_name,'w')
    for line in linelist[2:]:
        try :
            coords = zip((str,float,float,float),line.split()) 
            (elem, x, y, z) = [t(s) for t,s in coords] # extracts one line from file
            print(elem, x, y, z)
            fp.write("%s %1.6f %1.6f %1.6f \n" % elem, x, y, z)
        except ValueError:
            pass

    fp.close()
#convert2cif(sys_name)
def __main__ () :
    file_name = 'STO-110.xyz'
    convert2cif(filename)
