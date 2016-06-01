#!/usr/bin/env python3
import sys
import re
from pandocfilters import Str, toJSONFilter, RawInline, Para, walk

PATTERN1= re.compile(r"""({{.*)""",re.VERBOSE)
PATTERN2= re.compile(r"""(.*}})""",re.VERBOSE)

def subSeperator(string):
    """
        input: string (expected pattern {word, number; word, number} i.e a list of word-number pairs seperated by semicolons
        output: string with semicolons replaced by commas and word, number collapsed to wordnumber
    """
    return re.sub( r';', r',' , re.sub(r'(\s*,\s*)', r'', string) )

def writeCite(string):
    return string.replace(r'{{',r'\cite{').replace(r'}}',r'}')

def processCite(key, value, fmt, meta):
    if key == 'Para':
        if key == 'Str' and re.search(PATTERN1, value):
            return RawInline('latex', subSeperator(writeCite(re.search(PATTERN1, value).group(1))))
            #if fmt == 'latex':
        elif key == 'Str' and re.search(PATTERN1, value):
            return RawInline('latex', subSeperator(writeCite(re.search(PATTERN2, value).group(1))))

def removeSpace(key, value, fmt, meta):
    if key == 'Space':
        return Str("")

def main():
    toJSONFilter(processCite) # pass 1

if __name__ == "__main__" :
    main()
