import sys
sys.path.append("/home/appl/opencv-2.4.6.1/lib/python2.6/site-packages")
import cv2

from common import anorm, getsize
import os, random
  
def cutout_seq(img, size):
  print img
  src = cv2.imread(img, 1)

  quart = size/4
  x_pix = len(src[0])
  y_pix = len(src)

  x_time = x_pix/quart
  y_time = y_pix/quart

  i = 0
  for yt in xrange(y_time):
    for xt in xrange(x_time):
      dst = src[yt*quart: yt*quart+size, xt*quart:xt*quart+size]
      tmp_name = img.split("/")
      tmp = tmp_name[-1] + str(i) +"_seq.jpg"
      i += 1
      try:
        if len(dst[0]) == size and len(dst) == size:
          cv2.imwrite(tmp, dst)
      except:
        print "Not found"
  

if __name__ == "__main__":
  argvs = sys.argv

  cutout_seq(argvs[1],90) 
 

