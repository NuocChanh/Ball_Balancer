import cv2,serial,time
import numpy as np

gp = 0.0001
gi = 0.0004
gd = 0.0016
ePast1 = 0.0
iPast1 = 0.0
ePast2 = 0.0
iPast2 = 0.0
iLimit = 3.0
amplifyConstant=1.0

arduino = serial.Serial('COM3',115200)
motor_balance=[85,110]
pidLimit = 10
motorLimit=10
motor_angle=[80,110]
pidLimit =0.05
def pid(e, ePast, i):
    i += e*gi  
    p = e*gp
    d = (e - ePast)*gd
    if i > iLimit:
        i = iLimit
    elif i < -iLimit:
        i = -iLimit
    #pidReturn = p + i + d
    pidReturn = (p + i + d) 
    if pidReturn > pidLimit:
        pidReturn = pidLimit
    elif pidReturn < -pidLimit:
        pidReturn = -pidLimit
    return pidReturn

appleLocation=[350,240]
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1,80, param1=80,param2=30, minRadius=10, maxRadius=50)#change parameters
    cv2.circle(img,(appleLocation[0],appleLocation[1]),2,(255,0,0),3)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            if (i[0]!=0 and i[1] !=0):
                
                ball=[i[0],i[1]]
                error = [ball[0]-appleLocation[0],ball[1]-appleLocation[1]]    #deleted the abs
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                if abs(error[0]) <= 10 and abs(error[1]) <= 10:
                    for i in range(10):
                        arduino.write('i80m110e')
                        for i in range(100):
                            print('yay')
                motor_angle[0]=motor_angle[0]-pid(error[0],ePast1,iPast1)
                motor_angle[1]=motor_angle[1]-pid(error[1],ePast2,iPast2)

                for i in range (len(motor_angle)):
                    if motor_angle[i] > motor_balance[i] + motorLimit:
                        motor_angle[i] = motor_balance[i] + motorLimit
                    elif motor_angle[i] < motor_balance[i] - motorLimit:
                        motor_angle[i] = motor_balance[i] - motorLimit    
                PID = 'i'+str(int(motor_angle[0])) + 'm' +str(int(motor_angle[1]))+'e'                        
                print('Error: '+ str(error) +' MotorAngle: '+ PID)
                arduino.write(PID)
                #time.sleep(0.01)
                ePast1=error[0]
                ePast2=error[1]
    cv2.imshow('Camera', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindow()
