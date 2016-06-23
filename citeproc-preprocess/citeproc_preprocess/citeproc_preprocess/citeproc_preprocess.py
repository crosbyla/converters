#!/usr/bin/env python3
import sys
import re

PATTERN = re.compile(r"""([a-zA-Z0-9]\s)+({{.*}})""",re.VERBOSE)

def regexSep(string):
    """
        input: string (expected pattern {word, number; word, number} i.e a list of word-number pairs seperated by semicolons
        output: string with semicolons replaced by commas and word, number collapsed to wordnumber
    """
    return re.sub(r'(\s*;\s*)', r';@', re.sub( r'\s*,\s*', r'' , re.sub(r'\\#\d+\s*', r'', string) ) )

def regexCite(string):
    return re.sub(r'{{\s*',r'[@', re.sub( r'\s*}}',r']', string) )

def processFile(file_name, outfile = None):

    with open(file_name) as fp:
        f = fp.read()

    lines = f.split('\n')
    if outfile:
        with open(outfile, 'w') as fp:
            for line in lines:
                fp.write(processLine(line) + '\n')
    else :
        for line in lines:
            sys.stdout.write(processLine(line) + '\n')

def processLine(line):
    m = re.search(PATTERN,line)
    if m:
        subst = regexCite(regexSep(m.group(2)))
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
