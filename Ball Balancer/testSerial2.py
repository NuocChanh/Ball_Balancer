import serial, time
arduino = serial.Serial('COM9', 9600, timeout=.1)
while True:
    arduino.write('1')
    time.sleep(1)
    arduino.write('0')
    time.sleep(1)
