#!/usr/bin/env python3
"Main module"

import sys
import thumbnailer

if len(sys.argv) > 1:
    INFILES = sys.argv[1:]
else:
    INFILES = []
for inputfile in INFILES:
    thumbnailer.thumbnail(inputfile)
