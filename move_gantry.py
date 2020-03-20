#!/usr/bin/python
import time


class GantryControls:
    def move_up_position(self, ser):
        ser.write('1'.encode())
        time.sleep(2)
        msg = ser.readline()
        msg = msg.decode()
        print("At position: {}".format(msg))
    
    def move_down_position(self, ser):
        ser.write('2'.encode())
        time.sleep(2)
        msg = ser.readline()
        msg = msg.decode()
        print("At position: {}".format(msg))
    
    def move_home(self, ser):
        ser.write('3'.encode())
        time.sleep(6)
        msg = ser.readline()
        msg = msg.decode()
        print("At position: {}".format(msg))
    
    def small_shift_right(self, ser):
        ser.write('4'.encode())
        time.sleep(2)
        msg = ser.readline()
        print("At position: {}".format(msg))
    
    def small_shift_left(self, ser):
        ser.write('5'.encode())
        time.sleep(2)
        msg = ser.readline()
        msg = msg.decode()
        print("At position: {}".format(msg))


