"Turn images into 120x180 JPEG thumbnails"

import os
from PIL import Image

_THUMBSIZE = (120, 180)


def thumbnailer(inputfile):
    "Takes a file name and turns it into a 120x180 JPG"
    img = Image.open(inputfile).resize(_THUMBSIZE)
    img.mode = "RGB"
    outfile, _ = os.path.splitext(inputfile)
    img.save(outfile + ".jpg")
