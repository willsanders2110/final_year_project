import serial as sl
import time

ser = sl.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

ser.write('1')
msg = ser.readline()
print(msg)