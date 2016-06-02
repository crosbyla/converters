#!/usr/bin/env python3
import sys
import re
from pandocfilters import Str, toJSONFilter, RawInline, Para, walk, RawBlock

PATTERN1= re.compile(r"""({{.*)""",re.VERBOSE)
PATTERN2= re.compile(r"""(.*}})""",re.VERBOSE)


def processCite(key, value, fmt, meta):
    if key == 'Para':
        pass
    return None

def main():
    toJSONFilter(processCite) # pass 1

if __name__ == "__main__" :
    main()
