#!/usr/bin/python
__author__ = 'nitinr'

import sys

def getcontents(afilename):
    f = open(afilename, 'r')
    retval = f.read()
    f.close()
    return retval

def main():
    args = sys.argv

    if len(args) <= 2:
        print('Not enough arguments. Syntax:  numericRunme.py {in_filename} {maxval} [minval]')
        exit(-1)

    tpl_filename = args[1]
    tpl_content = getcontents(tpl_filename)

    maxval = args[2]
    minval = args[3] if (len(args) >= 4) else 1

    accum_txt = ''
    for i in range(int(minval), int(maxval)+1):
        vals = {'n': i}
        accum_txt += tpl_content % vals

    print(accum_txt)

if __name__ == '__main__':
    main()