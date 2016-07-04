#!/usr/bin/env python3
import sys
import re

PATTERN = re.compile(r"""(author:\n)(.*\n)""",re.VERBOSE)

def regexSep(string):
    """
        input: string (expected pattern {,} i.e a list of word-number pairs seperated by semicolons
        output: string with semicolons replaced by commas and word, number collapsed to wordnumber
    """
    return re.sub(r' and', r'\n  -', re.sub(r',', r'\n  -', string))

def processFile(file_name, outfile = None):
    with open(file_name) as fp:
        f = fp.read()
    line = f
    if outfile:
        with open(outfile, 'w') as fp:
            fp.write(processLine(line))
    else :
        sys.stdout.write(processLine(line))

def processLine(line):
    m = re.search(PATTERN,line)
    if m:
        subst = regexSep(m.group(2))
        line = line[:m.start()] + m.group(1) + subst + line[m.end():]
    return line

def main():
    if len(sys.argv) == 2:
        processFile(sys.argv[1])
    elif len(sys.argv) == 3:
        processFile(sys.argv[1], sys.argv[2])
    else :
        raise ValueError( "no file specified" )

if __name__ == "__main__" :
    main()
