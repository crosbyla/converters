#!/usr/bin/python
import sys
import re
import pandocfilters
from pandocfilters import walk
from pandocfilters import RawInline, Str, Para, Plain, Cite

PATTERN_FIRST = re.compile(r"""(?<={{\s*)(\w+)\s*,(\d+)""",re.VERBOSE)
PATTERN_SECOND = re.compile(r"""(?<=;\s*)(\w+)\s*,(\d+)""",re.VERBOSE)
PATTERN_LAST = re.compile(r"""(?<=;\s*)(\w+)\s*,(\d+)\s*}}""",re.VERBOSE)

def processRegex(file_name):
    processRegex(sys.argv)
def main():
    processRegex()
if __name__ == "__main__" :
    main()
