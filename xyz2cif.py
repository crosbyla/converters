#!/usr/bin/python

def convert2cif(file_name):
    with open(file_name) as fp:
        #read in file
        f = fp.read()

    coords = zip((str,float,float,float),f.split())
    (elem, x, y, z) = [t(s) for t,s in coords]
    file_name += "_coords.cif"

    fp = open(file_name,'w')

    for line in coords:
        try :
            print(line)
        #    fp.write()
        except ValueError:
            pass
    fp.close()
#convert2cif(sys_name)
def __main__ :
    convert2cif(filename)
