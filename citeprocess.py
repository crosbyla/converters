#!/usr/bin/python
import sys
import re
import fileinput

PATTERN = re.compile(r"""(\\{\\{.*\\}\\})""",re.VERBOSE)

def subSeperator(string):
    """
        input: string (expected pattern {word, number; word, number} i.e a list of word-number pairs seperated by semicolons
        output: string with semicolons replaced by commas and word, number collapsed to wordnumber
    """
    return re.sub( r';', r',' , re.sub(r'(\s*,\s*)', r'', string) )

def writeCite(string):
    return string.replace(r'\{\{',r'\cite{').replace(r'\}\}',r'}')

def processFile(file_name):
    outfile = file_name[:-3] + 'text' + file_name[-3:]

    with open(file_name) as fp:
        f = fp.read()

    lines = f.split('\n')

    with open(outfile, 'w') as fp:
        for line in lines:
            if re.search(PATTERN, line):
                line = subSeperator(writeCite(re.search(PATTERN, line).group(2)))
            fp.write(line)

def main():
    if len(sys.argv) >= 2:
        processFile(sys.argv[1])
    else :
        print( "no file specified" )
        raise ValueError

if __name__ == "__main__" :
    main()
