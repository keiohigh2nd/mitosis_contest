import sys
sys.path.append("/home/appl/opencv-2.4.6.1/lib/python2.6/site-packages")
import numpy as np
import cv2
from common import anorm, getsize
import os


def read_csv(filename):
  f = open(filename)
  lines = f.readlines()
  f.close()

  res = []
  for line in lines:
    tm = line.split(",")
    tmp = []
    tmp.append(tm[0].strip("\t"))
    tmp.append(tm[1].strip("\t"))
    res.append(tmp)
  return res


def cutout(img ,csv, file_name, size):
 print img
 src = cv2.imread(img, 1)
 i = 0
 half = size/2
 for point in csv:
   dst = src[int(point[1])-half:int(point[1])+half, int(point[0])-half:int(point[0])+half]
   i += 1
   tmp_name = file_name.split("/")
   tmp = tmp_name[-1] + str(i) +".jpg"
   try:
     if len(dst[0]) == size and len(dst) == size:
       cv2.imwrite(tmp, dst)
   except:
     print "Not found"
  

def set_path(img):
  name = img.split("/")
  return  name[-1][0:8] + ".tiff"
  
  

if __name__ == "__main__":

  argvs = sys.argv

  filename = argvs[1]
  img = argvs[2] + set_path(argvs[1])
  print img
  print "------"
  csv = read_csv(filename)
  cutout(img, csv, filename, 90)

