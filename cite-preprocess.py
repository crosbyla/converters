#!/usr/bin/python
import sys
import re

PATTERN = re.compile(r"""({{.*}})""",re.VERBOSE)

def regexSep(string):
    """
        input: string (expected pattern {word, number; word, number} i.e a list of word-number pairs seperated by semicolons
        output: string with semicolons replaced by commas and word, number collapsed to wordnumber
    """
    return re.sub(r'(\s*;\s*)', r',', re.sub( r'\s*,\s*', r'' , re.sub(r'\\#\d+\s*', r'', string) ) )

def regexCite(string):
    return re.sub(r'{{\s*',r'~\cite{', re.sub( r'\s*}}',r'}', string) )

def processFile(file_name, outfile = None):
    if outfile is None:
       outfile = file_name

    with open(file_name) as fp:
        f = fp.read()

    lines = f.split('\n')
    with open(outfile, 'w') as fp:
        for line in lines:
            m = re.search(PATTERN,line)
            if m:
               subst = regexCite(regexSep(m.group(1)))
               line = line[:m.start(1)] + subst + line[m.end(1):]
            fp.write(line + '\n')

def main():
    if len(sys.argv) == 2:
        processFile(sys.argv[1])
    elif len(sys.argv) == 3:
        processFile(sys.argv[1], sys.argv[2])
    else :
        print( "no file specified" )
        raise ValueError

if __name__ == "__main__" :
    main()
