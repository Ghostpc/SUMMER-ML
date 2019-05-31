#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:47:47 2019

@author: root
"""

import  cv2

#search for camera handling  function 
x=[i for  i  in  dir(cv2) if  'Video' in i]
print(x)

#  starting  videocapture 
cap=cv2.VideoCapture(0)  #  data live , stored , streamed 
print(dir(cap))  #  exploring  camera ops

# checking camera start point
while  cap.isOpened()  :
    status,img=cap.read()
    #changing image  gray scale   
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('live',img)
    cv2.imshow('gray',grayimg)
    if cv2.waitKey(10)  &  0xff == ord('q') :
        
        break
cv2.destroyAllWindows()
cap.release()


