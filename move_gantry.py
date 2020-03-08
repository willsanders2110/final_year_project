#!/usr/bin/python
import serial as sl
import time


class MoveGantry:
    def __init(self):
        self.ser = sl.serial('/dev/ttyUSB0', 9600)
        time.sleep(5)

    def move_up_position(self):
        self.ser.write('1')
        time.sleep(2)
        msg = self.ser.readline()
        print("At position: {}".format(msg))
    
    def move_down_position(self):
        self.ser.write('2')
        time.sleep(2)
        msg = self.ser.readline()
        print("At position: {}".format(msg))
    
    def move_home(self):
        self.ser.write('3')
        time.sleep(6)
        msg = self.ser.readline()
        print("At position: {}".format(msg))
    
    def small_shift_right(self):
        self.ser.write('4')
        time.sleep(2)
        msg = self.ser.readline()
        print("At position: {}".format(msg))
    
    def small_shift_left(self):
        self.ser.write('5')
        time.sleep(2)
        msg = self.ser.readline()
        print("At position: {}".format(msg))


