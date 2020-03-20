#!/usr/bin/python


class MoistureData:
    def position_1_data(self, ser):
        ser.write('1'.encode())
        msg = ser.readline()
        return msg.decode()

    def position_2_data(self, ser):
        ser.write('2'.encode())
        msg = ser.readline()
        return msg.decode()

    def position_3_data(self, ser):
        ser.write('3'.encode())
        msg = ser.readline()
        return msg.decode()

    def position_4_data(self, ser):
        ser.write('4'.encode())
        msg = ser.readline()
        return msg.decode()
