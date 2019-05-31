#!/usr/bin/env python3
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('cat.jpg',1)
crop=img[100:200,123:312]
plt.imshow(img)
cv2.imshow('img',img)
cv2.imshow('crop',crop)
cv2.waitkey(0)
cv2.destroyAllwindow()
