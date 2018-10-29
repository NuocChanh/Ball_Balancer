import cv2,serial,time
import numpy as np
def pid(gp, gi, gd, e, ePast):
    i += e*gi
    p = e*gp
    d = (e-ePast)*gd
    pidReturn = p+i+d
    return pidReturn
#arduino = serial.Serial('COM9', 9600, timeout=.1)
#arduino.write()
cap = cv2.VideoCapture(0)
appleLocation=[0,0]
while True:
    a = raw_input('scanDestination, moveBall, or quit? ')
    if a.lower() == 'scandestination':
        allApples = []
        appleAverageX = 0
        appleAverageY = 0
        stop = False
        while True:
            _, img = cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1,15, param1=80,param2=40, minRadius=1, maxRadius=150)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    apple=[i[0],i[1]]
                    if apple != [0,0] and len(allApples) < 60:
                        for a in apple:
                            allApples.append(a)
            if len(allApples)==60:
                i = 0
                j = 1
                while i <=58:
                    while j <= 59:
                        x=allApples[i]
                        y=allApples[j]
                        appleAverageX += int(x)
                        appleAverageY += int(y)
                        i+=2
                        j+=2
                appleAverageX /= 30
                appleAverageY /= 30
                appleLocation = [appleAverageX, appleAverageY]
                print 'Destination coordinates: ' + str(appleLocation)
                stop = True
            if stop == True:
                break;
    elif a.lower() == 'moveball':
        while True:
            _, img = cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1,80, param1=80,param2=30, minRadius=10, maxRadius=50)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    if (i[0]!=0 and i[1] !=0):
                        ball=[i[0],i[1]]
                        error = [abs(ball[0]-appleLocation[0]),abs(ball[1]-appleLocation[1])]
                        print 'Error: '+ str(error)
                        #movePid = pid(1, 1, 1, error, ePast)
            cv2.imshow('Image', img)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
    elif a.lower() == 'quit':
        quit()
    else:
        pass
cv2.destroyAllWindow()
