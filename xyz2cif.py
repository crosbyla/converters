#!/usr/bin/python

def convert2cif(file_name):
    with open(file_name) as fp:
        #read in file
        f = fp.read()

    for line in f:
        #iterate over lines in file
        if line.strip():
            
        else :
            continue

    file_name += "_coords.cif"

    fp = open(file_name,'w')

    for line in coords:
        vals = line.split()
        try :
            fp.write()
        except ValueError:
            pass
    fp.close()
#convert2cif(sys_name)
def __main__ :
    convert2cif(filename)
