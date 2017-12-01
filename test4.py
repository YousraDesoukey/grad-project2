from os import listdir
from os.path import isfile, join
import numpy
import cv2

#mypath= "C:/Users/user/Desktop/gp pics/name"
mypath= "C:/Users/user/Desktop/gp pics/4-thutmose2-birth name/f1"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )

for n in range(0, len(onlyfiles)):
    images[n] = cv2.cvtColor(images[n], cv2.COLOR_BGR2GRAY)
    ret, images[n] = cv2.threshold(images[n], 200, 255, cv2.THRESH_BINARY)
 #   images[n] = cv2.resize(images[n],None,fx=0.7, fy=0.5, interpolation = cv2.INTER_AREA)
 #   images[n] = cv2.resize(images[n], (500, 500))


for n in range(0, len(onlyfiles)):
    cv2.imshow('img', images[n])
    cv2.waitKey(0)

cv2.destroyAllWindows()