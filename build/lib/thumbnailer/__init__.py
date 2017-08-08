"Turn images into 120x180 JPEG thumbnails"

import sys
import os
from glob import glob
from PIL import Image

_THUMBSIZE = (120, 180)


def thumbnail(*infiles):
    "Takes a file name and turns it into a 120x180 JPG"
    if len(infiles) < 1:
        if len(sys.argv) > 1:
            infiles = sys.argv[1:]
        else:
            infiles = glob("*.jpg")
            infiles += glob("*.png")
            infiles += glob("*.gif")
    for inputfile in infiles:
        img = Image.open(inputfile).resize(_THUMBSIZE)
        img.mode = "RGB"
        outfile, _ = os.path.splitext(inputfile)
        img.save(outfile + ".jpg")
