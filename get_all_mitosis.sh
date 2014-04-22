#!/bin/bash

#Don't forget *
#files are the mitosis csv folder and image is the all image data foldr
files="../A05/mitosis/*"
image="../A05/frames/x40/"

for filepath in ${files}
do
  python2.7 cut_out_mitosis.py ${filepath} ${image}
done
