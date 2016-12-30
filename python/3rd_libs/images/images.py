# coding: utf-8
"""
This is module docs.
"""
__author__ = u'lovexiaov'

import os
from PIL import Image

img_path = os.path.split(__file__)[0] + r'/res/source.jpg'

name, suffix = os.path.splitext(img_path)

# open image from path
img = Image.open(img_path) 
print(img.format, img.size, img.mode) # ('JPEG', (1440, 900), 'RGB')
# img.show()

# convert image to .png format
# img.save(name + r'.png') 

size = (302, 189)
img.thumbnail(size, Image.ANTIALIAS)
img.save(name + r'.thumbnail.jpg', 'JPEG') # if not specify the format, it will try to parse the files suffix.
print(img.size)

img_path = os.path.split(__file__)[0] + r'/res/source.thumbnail.jpg'
img = Image.open(img_path)
print(img.format)


if __name__ == u'__main__':
    pass