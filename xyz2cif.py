#!/usr/bin/python
def convert2cif(file_name):
    with open(file_name) as fp:
        #read in file
        f = fp.read()
    atomlist = []
    for line in f[2:]:
        atoms = zip((str,float,float,float),f.split('\n'))
        (elem, x, y, z) = [t(s) for t,s in atoms]
        atomlist.append([elem,x,y,z])

    file_name += "_coords.cif"

    fp = open(file_name,'w')

    for a in atomlist
        try :
            print(a)
        #    fp.write()
        except ValueError:
            pass
    fp.close()
#convert2cif(sys_name)
def __main__ :
    convert2cif(filename)
