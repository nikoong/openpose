#-*- coding:utf8 -*-

import json as js
import numpy as np
import cv2

 
img = cv2.imread('00480_00008.jpg')

with open("00480_00008_pose.json","r") as f:
    data = js.load(f)
    people = data['people']
    if(len(people) == 1):
        pose = np.array(people[0]['body_parts'])
        pose = pose.reshape(18,3)
        hip_y = (pose[8][1] + pose[11][1])/2
        hip_y = int(hip_y)
        #print hip_y
        img_up = img[0:hip_y,:,:]
        img_down = img[hip_y:,:,:]
        cv2.namedWindow('up',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('up',img_up)
        cv2.waitKey()  
        cv2.imwrite("00480_00008_pose_up.jpg", img_up)
        cv2.imwrite("00480_00008_pose_down.jpg", img_down)
                
        


