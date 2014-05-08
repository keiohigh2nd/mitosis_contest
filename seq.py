import sys
sys.path.append("/home/appl/opencv-2.4.6.1/lib/python2.6/site-packages")
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
 
def get_distance(y, x, qy, qx):
  tmp_y = (y-qy)*(y-qy)
  tmp_x = (x-qx)*(x-qx)

  return (tmp_y+tmp_x)
  
def check_label(csv,yt,xt,size):
  center_y = yt + size/2
  center_x = xt + size/2

  for pos in csv:
    distance = get_distance(center_y, center_x, int(pos[1]), int(pos[0]))
    if distance < 1060:
      print "distance close"
      return 1
  return 0

def cutout_seq(img, csv, size):
  print img
  src = cv2.imread(img, 1)

  quart = size/3
  x_pix = len(src[0])
  y_pix = len(src)

  x_time = x_pix/quart
  y_time = y_pix/quart

  j = 0
  for yt in xrange(y_time):
    i = 0
    for xt in xrange(x_time):
      dst = src[yt*quart: yt*quart+size, xt*quart:xt*quart+size]
      tmp_name = img.split("/")
      try:
        if len(dst[0]) == size and len(dst) == size:
          if check_label(csv, yt*quart, xt*quart, size) == int(1):
            tmp = tmp_name[-1] + str(i) + "_" + str(j) +"_seq_true.jpg"
            tmp_f = "true/" + tmp
            cv2.imwrite(tmp_f, dst)
          else:
            tmp = tmp_name[-1] + str(i) + "_" + str(j) +"_seq_false.jpg"
            tmp_f = "false/" + tmp
            cv2.imwrite(tmp_f, dst)
      except:
        print "Not found"
      i += 1
    j += 1


  

if __name__ == "__main__":

  argvs = sys.argv

  filename = argvs[1]
  img = argvs[2] + set_path(argvs[1])
  #img = argvs[2]
  print img
  print "------"
  csv = read_csv(filename)
  
 
  #csv = return_random_point(5)
  #cutout(img, csv, filename, 90)
  cutout_seq(img, csv, 90)

