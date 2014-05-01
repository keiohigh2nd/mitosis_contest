#!/bin/bash

#Don't forget *
#files are the mitosis csv folder and image is the all image data foldr
files="../A04/mitosis/*"
image="../A04/frames/x40/"

for filepath in ${files}
do
  python2.7 seq.py ${filepath} ${image}
done
