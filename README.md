# thumbnailer
Python module to turn images into 120x180 JPEG thumbnails.

## Usage
thumbnailer can either be used in your code:

```
import thumbnailer

thumbnailer.thumbnail("MyCoolPic.png")
```

It will then create a 120x180 JPEG version of your picture. If it already was a JPEG, thumbnailer will overwrite it.

Alternatively, you can use thumbnailer from the console:
`python3 -m thumbnailer [path to image here]`
or
`tbnailer.py [path to image here]`