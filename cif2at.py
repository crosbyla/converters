#!/usr/bin/python
# Attempting to gain same functionality as the following UNIX commands
# sed -e '1,/_atom_site_fract_z/d' pd111-full-supercell.cif | sed -e '/^$/d' | awk '{ print $1!~/^[0-9]/,$2,$4,$5,$6,$3,$3}' > test-out.txt
import sys
import re

sys_name=sys.argv[1]
atomz=re.compile(r"""atom_site_fract_z""",re.VERBOSE)

def convert2at(file_name):
    title = "Converted file " + file_name
    coords = []
    angles = []
    lat_param = []
    sgroup = []
    thickness = 10
    flag = False
    zone_axis = [1,0,0]
    diff_atoms = 1
    gmax = 2.00
    micName = "JEOL2100F"
    symOps = 1
    slices = 1
    sphAber = 0.5
    deltaF = 100
    convAng  = 60
    voltage = 200
    laueCtr = [0,0]
    twoFoldAstig = 0.0
    twoFoldAng = 0.0
    threeFoldAstig = 0.0
    threeFoldAng = 0.0
    coma = 0.0
    comaAng = 0.0
    hLaue = 0
    kLaue = 0
    maxInten = 8.0
    startDef = 0
    endDef = 0
    defStep = 0
    vibX = 0.5
    vibY = 0.5
    vibAng = 0.0
    objInnerRad = 0.00
    objOuterRad = 2.00

    with open(file_name) as fp:
        #read in file
        for line in fp.readlines():
            #iterate over lines in file
            if atomz.search(line.strip()):
                # extract line if no whitespace
                flag = True # change switch for boundary condition
                continue # skip line
            if line.strip():
                # 
                if flag == False:
                    if re.search(r"""_cell_length_.*?(?P<cell>-?[\d.]+)""",
                            line.strip()):
                        lat_param.append(re.search(
                            r"""_cell_length_.*?(?P<cell>-?[\d.]+)""",
                            line.strip()))
                    if re.search(r"""_cell_angle.*?(?P<cell>-?[\d.]+)""",
                            line.strip()):
                        angles.append(re.search(r"""_cell_angle.*?(?P<cell>-?[\d.]+)""",
                            line.strip()))
                        re.search(r"""_cell_angle.*?(?P<cell>-?[\d.]+)""",
                            line.strip())
                    if re.search(r"""_symmetry_Int_Tables_number.*?(?P<cell>-?[\d.]+)""",
                            line.strip()):
                        sgroup.append(re.search(r"""_symmetry_Int_Tables_number.*?(?P<cell>-?[\d.]+)""",
                            line.strip()))
                else:
                    coords.append(line.strip())
    fp.close()

    print "Title", title
    print "Lattices Parameters and Angles:",lat_param[0].group(1),lat_param[1].group(1),lat_param[2].group(1),angles[0].group(1),angles[1].group(1),angles[2].group(1)
    print "Space Group #:",sgroup[0].group(1)
    print "Zone Axis:", zone_axis[0], zone_axis[1], zone_axis[2]
    print "Gmax: ",gmax
    print "Symmetry Operators, Slices, Basis Atoms, Unique Atoms, ",symOps, slices, 0, 1, 0
    print "Number of Atoms, Unique:",len(coords), 1

    file_name += "_coords_at"

    fp = open(file_name,'w')

    for line in coords:
        vals = line.split()
        try:
            if re.search(r'\d+',vals[0]):
                vals[0] = int(re.search(r'\d+',vals[0]).group())
            else:
                vals[0] = 1
            fp.write(str(vals[0]) + ' ' + str(vals[1]) + ' ' +str(vals[3]) + ' ' +str(vals[4]) +
                    ' ' +str(vals[5]) +' ' +str(vals[2]) + ' ' +str(vals[2]) + "\n")
#+vals[1],vals[3],vals[4],vals[5],vals[2],vals[2])
        except ValueError:
            pass
    fp.close()
#    print "Microscope Parameters:", micName, sphAber, deltaF, convAng, twoFoldAstig, threeFoldAstig, twoFoldAng, threeFoldAstig, coma, comaAng, hLaue, kLaue
#    print "Voltage", voltage
#    print 0.0000, 0.0000
#    print thickness
#    print "NO"
#    print "Focal Series", startDef, endDef, defStep
#    print "Obj Aper Radius", objInnerRad, objOuterRad
#    print "x,y,z"
#    print "Vibration Parameters:", vibX, vibY, vibAng
#    print 1
#    print ""
#    print "Max Lens Intensity", maxInten, diff_atoms
convert2at(sys_name)
