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

    if len(args) < 3:
        print('Not enough arguments. Syntax:  numericRunme.py {tpl_filename} {list_filename}')
        exit(-1)

    tpl_filename = args[1]
    tpl_content = getcontents(tpl_filename)

    list_filename = args[2]
    list_content = getcontents(list_filename)

    accum_txt = ''
    for iter in list_content.split('\n'):
        vals = {'tag': iter}
        accum_txt += tpl_content % vals

    print(accum_txt)

if __name__ == '__main__':
    main()