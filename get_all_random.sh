#!/bin/bash

#Don't forget *
#files are the mitosis csv folder and image is the all image data foldr
files="../A07/mitosis/*"
image="../A07/frames/x40/"

for filepath in ${files}
do
  python2.7 cut_out_random.py ${filepath} ${image}
done
