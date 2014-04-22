import sys
sys.path.append("/home/appl/opencv-2.4.6.1/lib/python2.6/site-packages")
import numpy as np
import cv2
from common import anorm, getsize
import os, random

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

def return_random_point(num):
  res = []
  for i in xrange(num):
    tmp = []
    ran_x = random.randint(0,1538)
    ran_y = random.randint(0,1376)
    tmp.append(ran_x)
    tmp.append(ran_y)
    res.append(tmp)

  return res

def cutout(img ,csv, file_name):
 print img
 src = cv2.imread(img, 1)
 i = 0
 for point in csv:
   dst = src[int(point[1])-30:int(point[1])+60, int(point[0])-30:int(point[0])+60]
   i += 1
   tmp_name = file_name.split("/")
   tmp = tmp_name[-1] + str(i) +"_random.jpg"
   cv2.imwrite(tmp, dst)
  

def set_path(img):
  name = img.split("/")
  return  name[-1][0:8] + ".tiff"
  
  

if __name__ == "__main__":

  argvs = sys.argv

  filename = argvs[1]
  img = argvs[2] + set_path(argvs[1])
  print img
  print "------"
  #csv = read_csv(filename)
  
 
  csv = return_random_point(10)
  cutout(img, csv, filename)

