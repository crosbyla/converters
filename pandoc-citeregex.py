#!/usr/bin/python
import sys
import re
import pandocfilters
from pandocfilters import walk
from pandocfilters import Str, toJSONFilter

PATTERN = re.compile(r"""({{.*}})""",re.VERBOSE)

def subSeperator(string):
    """
        input: string (expected pattern {word, number; word, number} i.e a list of word-number pairs seperated by semicolons
        output: string with semicolons replaced by commas and word, number collapsed to wordnumber
    """
    return re.sub( r';', r',' , re.sub(r'(\s*,\s*)', r'', string) )

def writeCite(string):
    return string.replace(r'{{',r'\cite{').replace(r'}}',r'}')

def processRegex(key, value, fmt, meta):
    if key == 'Str':
        fmt, text = value
        if fmt == 'latex':
            if re.search(PATTERN, text):
                return Str(subSeperator(writeCite(re.search(PATTERN, text).group(1))))

def main():
    toJSONFilter(processRegex)

if __name__ == "__main__" :
    main()
