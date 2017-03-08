"""
Requirement:
python3
Python Image library (PIL)

To run code:
python2.7 img_resize.py dir width height       #number to begin sequence

"""

import sys
import os
import PIL.Image

if __name__ == '__main__':
    _dir = os.path.join(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    for img in os.listdir(_dir):
        if os.path.isfile(os.path.join(_dir,img)) and img[0] != '.': #omit directories and hidden files
            im = PIL.Image.open(os.path.join(_dir,img))
            newim = im.resize((width, height))
            newim.save(os.path.join(_dir,img))
