import cv2
import cv2.aruco as aruco
import numpy as np
import math as m
import time 
import requests as rq

url='192.168.0.8'

capture=cv2.VideoCapture(1)

def main(img,subpart,target_id):
    if(subpart==0):
        ids,corners,center,angle = findAruco(img)
        if(len(corners)>0):
            print(ids,center[0],angle[0])
            print('I see Aruco!')
            if(ids[0] == target_id):
                subpart=1
                r=rq.get(url="http://"+url+"/Stop")
                return subpart
            else:
                threshold = 10
                if angle[0]>5 and angle[0]<60:
                    while(angle[0]>5):
                        r=rq.get(url="http://"+url+"/sleft")
                        time.sleep(1)
                elif angle[0]<355 and angle[0]>300:
                    while(angle[0]<355):
                        r=rq.get(url="http://"+url+"/sright")
                        time.sleep(1)
                r=rq.get(url="http://"+url+"/Forward")
                time.sleep(0.5)
                return subpart         
          
        else:
            r=rq.get(url="http://"+url+"/Forward")
            time.sleep(0.5)
            print("Going Forward")  
            return subpart
    elif subpart ==1:
        ids,corners,center,angle = findAruco(img)
        print(ids,center,angle)
        for i in range(4):
            r=rq.get("http://"+url+"/Forward")
            time.sleep(0.2)
        time.sleep(2)    
        for i in range(5):
            r=rq.get("http://"+url+"/Left")
            time.sleep(0.5)
        for i in range(8):
            r=rq.get("http://"+url+"/Forward")
            time.sleep(0.2)
        time.sleep(5)
            
        for i in range(10):
            r=rq.get("http://"+url+"/Right")  
            time.sleep(0.2)
        for i in range(8):
            r=rq.get("http://"+url+"/Forward")
            time.sleep(0.2)
        for i in range(6):
            r=rq.get("http://"+url+"/Right")  
            time.sleep(0.2)    
        subpart=2
        return subpart   
    
    elif subpart==2:
        if target_id==1:
            for i in range(12):
                r=rq.get("http://"+url+"/Forward")
        elif target_id==0:
            for i in range(25):
                r=rq.get("http://"+url+"/Forward")
        print("Operation finished")                    

def findAruco(img, marker_size=5,total_markers=250,draw=True):
    center_list=[]
    angle_list=[]
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # key=getattr(aruco,f'DICT_ARUCO_ORIGINAL')
    key=getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')
    arucoDict=aruco.Dictionary_get(key)
    arucoParam=aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict,
	parameters=arucoParam)

    print(ids)
    if len(corners) > 0:
	# flatten the ArUco IDs list
        ids = ids.flatten()
        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            center=[cX,cY]
            center_list.append(center)
            cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)
            mX = int((topRight[0] + bottomRight[0]) / 2.0)
            mY = int((topRight[1] + bottomRight[1]) / 2.0)
            x=mX-cX
            angle=m.degrees(m.atan2(mY-cY,mX-cX))
            angle=int(angle)
            if angle<0:
                angle+=360
            angle_list.append(angle)
            cv2.putText(img,f'{angle}',(cX-10,cY-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    return ids,corners,center_list,angle_list           

if __name__ == '__main__':
    subpart=0      
    target_id = int(input('Please enter the target ARUCO ID : '))
    while True:
        ret,img=capture.read()
        # img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
        subpart = main(img,subpart,target_id)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
        cv2.imshow('Webcam',img)

    capture.release()
    cv2.destroyAllWindows()    
