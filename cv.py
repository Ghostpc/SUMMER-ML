#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:52:30 2019

@author: root
"""

import cv2

read_ops=[i for i in dir(cv2) if 'read' in i]
print(read_ops)
#reading dara from image
img=cv2.imread('cat.jpg',1)
img1=cv2.imread('cat.jpg',0)
print(img.size)
print(img.shape)
print(img)
cv2.imshow('win',img)
cv2.imshow('win1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
