#-*- coding:utf8 -*-

import xml.etree.ElementTree as ET
import numpy as np
import cv2

tree = ET.parse('0003C4T0003F001_pose.xml') 
img = cv2.imread('0003C4T0003F001.jpg')

root = tree.getroot() 
##access specific child nodes by index:
sizes_text = root[0][0].text
#print sizes_text
#[\n    1 18 3]


data = np.zeros(54)
id_num = sizes_text.split('\n    ')[1].split(' ')[0]
if id_num != 1:
    index = 0
    data_text = root[0][2].text.split('\n    ')[1:]
    for line in data_text:
        for i in line.split(' '):           
            data[index] = float(i)
            index = index + 1

data = data.reshape(18,3)
hip_y = (data[8][1] + data[11][1])/2
hip_y = int(hip_y)
img_up = img[0:hip_y,:,:]
img_down = img[hip_y:,:,:]
#cv2.namedWindow('up',cv2.WINDOW_AUTOSIZE)
#cv2.imshow('up',img_up)
#cv2.waitKey()  
cv2.imwrite("0003C4T0003F001_up.jpg", img_up)
cv2.imwrite("0003C4T0003F001_down.jpg", img_down)




