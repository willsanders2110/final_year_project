#!/usr/bin/python


class MoistureData:
    def position_1_data(self, ser):
        ser.write('1')
        msg = ser.readline()
        return msg

    def position_2_data(self, ser):
        ser.write('2')
        msg = ser.readline()
        return msg

    def position_3_data(self, ser):
        ser.write('3')
        msg = ser.readline()
        return msg

    def position_4_data(self, ser):
        ser.write('4')
        msg = ser.readline()
        return msg
