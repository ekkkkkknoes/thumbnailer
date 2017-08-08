"Main module"

import sys
import glob
import thumbnailer

if len(sys.argv) > 1:
    _FLIST = sys.argv[1:]
else:
    _FLIST = glob.glob("*.jpg")
    _FLIST += glob.glob("*.png")
    _FLIST += glob.glob("*.gif")
for infile in _FLIST:
    thumbnailer.thumbnailer(infile)
