#!/usr/bin/env python3
"Setup script"

from distutils.core import setup

setup(
    name="thumbnailer",
    version="1.0",
    description="Module to turn images into thumbnails",
    author="Sönke Lambert",
    author_email="soelam@live.de",
    url="https://github.com/ekkkkkknoes/thumbnailer",
    scripts=["bin/tbnailer.py"],
    packages=["thumbnailer"]
)
