#!/usr/bin/python
import sys
import re
import pandocfilters
from pandocfilters import walk
from pandocfilters import RawInLine, Str, Para, Plain, Cite

PATTERN_FIRST = re.compile(r"""(?<={{\s*)(\w+)\s*,(\d+)""",re.VERBOSE)
PATTERN_SECOND = re.compile(r"""(?<=;\s*)(\w+)\s*,(\d+)""",re.VERBOSE)
PATTERN_LAST = re.compile(r"""(?<=;\s*)(\w+)\s*,(\d+)\s*}}""",re.VERBOSE)

def processRegex(file_name):
    with open(file_name) as fp:
        #read in file
        for line in fp.readlines():
            #iterate over lines in file
            if line.strip():
                #if flag == False:
                if re.search(pattern, string):
                    line.strip()
                    position.append(line.strip())
                else :
                    if re.search(r"""<point name""",line.strip()):
                        coords.append(line.strip())
    fp.close()

    file_name += "_filtered.md"
    fp = open(file_name,'w')
    fp.close()
if __name__ == "__main__" :
    processRegex(sys.argv)
processRegex(filename)
