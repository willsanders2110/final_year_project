import RPi.GPIO as GPIO


class LED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.LED_1 = 17
        self.LED_2 = 27
        self.LED_3 = 22
        self.LED_4 = 23
        self.LED_5 = 24
        self.LED_6 = 25
        self.LED_7 = 5
        self.LED_8 = 6
        self.LED_9 = 26
        self.LED_10 = 16
        self.LED_11 = 20
        self.LED_12 = 21

        GPIO.setup(self.LED_1, GPIO.OUT)
        GPIO.setup(self.LED_2, GPIO.OUT)
        GPIO.setup(self.LED_3, GPIO.OUT)
        GPIO.setup(self.LED_4, GPIO.OUT)
        GPIO.setup(self.LED_5, GPIO.OUT)
        GPIO.setup(self.LED_6, GPIO.OUT)
        # GPIO.setup(self.LED_7, GPIO.OUT)
        # GPIO.setup(self.LED_8, GPIO.OUT)
        # GPIO.setup(self.LED_9, GPIO.OUT)
        # GPIO.setup(self.LED_10, GPIO.OUT)
        # GPIO.setup(self.LED_11, GPIO.OUT)
        # GPIO.setup(self.LED_12, GPIO.OUT)

    def led_on(self):
        print('LEDs on')
        GPIO.output(self.LED_1, GPIO.HIGH)
        GPIO.output(self.LED_2, GPIO.HIGH)
        GPIO.output(self.LED_3, GPIO.HIGH)
        GPIO.output(self.LED_4, GPIO.HIGH)
        GPIO.output(self.LED_5, GPIO.HIGH)
        GPIO.output(self.LED_6, GPIO.HIGH)
        # GPIO.output(self.LED_7, GPIO.HIGH)
        # GPIO.output(self.LED_8, GPIO.HIGH)
        # GPIO.output(self.LED_9, GPIO.HIGH)
        # GPIO.output(self.LED_10, GPIO.HIGH)
        # GPIO.output(self.LED_11, GPIO.HIGH)
        # GPIO.output(self.LED_12, GPIO.HIGH)

    def led_off(self):
        print('LEDs off')
        GPIO.output(self.LED_1, GPIO.LOW)
        GPIO.output(self.LED_2, GPIO.LOW)
        GPIO.output(self.LED_3,  GPIO.LOW)
        GPIO.output(self.LED_4,  GPIO.LOW)
        GPIO.output(self.LED_5,  GPIO.LOW)
        GPIO.output(self.LED_6,  GPIO.LOW)
        # GPIO.output(self.LED_7,  GPIO.LOW)
        # GPIO.output(self.LED_8,  GPIO.LOW)
        # GPIO.output(self.LED_9,  GPIO.LOW)
        # GPIO.output(self.LED_10, GPIO.LOW)
        # GPIO.output(self.LED_11, GPIO.LOW)
        # GPIO.output(self.LED_12, GPIO.LOW)
