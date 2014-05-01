import sys
sys.path.append("/home/appl/opencv-2.4.6.1/lib/python2.6/site-packages")

from common import anorm, getsize
import os, random
import cv2

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

def return_random_point(num, csv):
  res = []
  for i in xrange(num):
    tmp = []
    ran_x = random.randint(0,1538)
    ran_y = random.randint(0,1376)
    for pos in csv:
      if ran_x - 10 < int(pos[0]) < ran_x + 10 and ran_y - 10 < int(pos[1]) < ran_y + 10:
	ran_x = ran_x + 20
	ran_y = ran_y + 20
    tmp.append(ran_x)
    tmp.append(ran_y)
    res.append(tmp)

  return res

def cutout(img ,csv, file_name, size):
 print img
 src = cv2.imread(img, 1)
 i = 0
 ##size of capture
 half = size/2
 print half
 for point in csv:
   dst = src[int(point[1])-half:int(point[1])+half, int(point[0])-half:int(point[0])+half]
   i += 1
   tmp_name = file_name.split("/")
   tmp = tmp_name[-1] + str(i) +"_random.jpg"
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
  pre_csv = read_csv(filename)
  
 
  csv = return_random_point(5,pre_csv)
  cutout(img, csv, filename, 90)

