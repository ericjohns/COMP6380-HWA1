# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:28:41 2017

@author: Eric Johns
"""
from PIL import Image
im = Image.open('a0.jpg')

# Covert to 256 Gray Level mode
im = im.convert('L')

# See how the colors are distributed
print(im.getcolors())

# 255-> White, 0-> Black
# If we remove all the "whiter" colors
im = im.point(lambda x: 255 if x>128 else x)
# see how this policy works
im.show()

 # the new color distribution?
print(im.getcolors())

def clean(im):
    im = im.convert('L')
    im = im.point(lambda x:255 if x>128 or x==0 else x)
    im = im.point(lambda x:0 if x<255 else 255)
    return im

im.show()

#Divide by Columns
w, h = im.size
data = im.load()
jcolors = [sum(255-data[i,j] for j in range(h)) for i in range(w)]

print(jcolors)
