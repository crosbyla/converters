#!/usr/bin/python
import re
import Tkinter as tk
import tkFileDialog as filedialog

root=tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
pattern=re.compile(r"""<positions>""",re.VERBOSE)
flag = False
coords=[]
position=[]
date=[]
start_date=[]
date_diff=[]

def extractcoords(file_name):

    with open(file_name) as fp:
        #read in file
        for line in fp.readlines():
            #iterate over lines in file
            if pattern.search(line.strip()):
                # extract line if no whitespace
                flag = True # change switch for boundary condition
                continue # skip line
            if line.strip():
                #if flag == False:
                if re.search(r"""<position desktopRef=.*?(?P<cell>-?[\d.]+)""",
                        line.strip()):
                    position.append(line.strip())
                else:
                    if re.search(r"""<point name""",line.strip()):
                        coords.append(line.strip())
    fp.close()

    file_name += "_extracted-coords.csv"
    fp = open(file_name,'w')
    for i,line in enumerate(coords):
        #try:
        date = position[i].split()
        date_match=re.findall(r'(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+)',date[3])
        date_match_int = reduce(lambda m,s: int(m)*60 + int(s), date_match[0][3:6])
        if i == 0:
            start_date=date_match_int
        date_diff = date_match_int - start_date
        vals = line.split()
        try:
            if re.search(r'\d+',vals[2]):
                vals[2] = float(re.search(r'\d+',vals[2]).group())
            if re.search(r'\d+',vals[3]):
                vals[3] = float(re.search(r'\d+',vals[3]).group())
            fp.write("%s " % date_diff )
            fp.write(" " + str(vals[2]) + ','+ str(vals[3]) + "\n")
        except ValueError:
            pass
        print date_match
        print date_diff
        print vals[2],vals[3]
    fp.close()
extractcoords(filename)
