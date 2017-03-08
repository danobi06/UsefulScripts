"""
Requirement:
python3

To run code:
python2.7 files_rename.py dir newname.ext 1        #number to begin sequence

"""

import sys
import os

if __name__ == '__main__':
    _dir = (os.path.join(sys.argv[1]))
    name, ext = sys.argv[2].split('.')
    seq = int(sys.argv[3])
    for _file in os.listdir(_dir):
        if os.path.isfile(os.path.join(_dir,_file)) and _file[0] != '.': #omit directories and hidden files
            newname = name + str(seq)+ '.'+ext
            os.rename(os.path.join(_dir,_file),os.path.join(_dir,newname))
            seq+=1
