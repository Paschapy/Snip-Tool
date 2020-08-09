# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:38:21 2020

@author: akifcal
"""

import cv2
class Opencv():
    def __init__(self,index):
        #self.image=image
        self.index=index
        self.refPt = []
        self.cropping = False
        self.image=cv2.imread("image.jpg")
        self.clone=self.image.copy()
        name=("img000{}.png".format(self.index))
        if self.index>9:
            name=("img00{}.png".format(self.index))
        elif self.index>99:
            name=("img0{}.png".format(self.index))
        elif self.index>999:
            name=("img{}.png".format(self.index))
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.click_and_crop)





        while 1:
            cv2.imshow("image",self.image)
            self.key=cv2.waitKey(1)&0xFF
            if self.key==ord("r"):
                self.image=self.clone.copy()
            elif self.key==ord("s") or self.key==ord("S"):
               # cv2.destroyAllWindows()
                break

        if len (self.refPt)==2:
            self.roi=self.clone[self.refPt[0][1]:self.refPt[1][1],self.refPt[0][0]:self.refPt[1][0]]
            cv2.imshow("roi",self.roi)
            cv2.imwrite(name,self.roi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    def click_and_crop(self,event,x,y,flags,param):
        
        if event==cv2.EVENT_LBUTTONDOWN:
            self.refPt=[(x,y)]
            print(self.refPt)
            self.cropping=True
        elif event==cv2.EVENT_LBUTTONUP:
            self.refPt.append((x,y))
            print(self.refPt)
            self.cropping=False
            cv2.rectangle(self.image,self.refPt[0],self.refPt[1],(0,255,0),2)
            cv2.imshow("image",self.image)
        