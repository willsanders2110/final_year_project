import RPi.GPIO as GPIO


class LED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.LED_1 = 17
        self.LED_2 = 27
        GPIO.setup(self.LED_1, GPIO.OUT)
        GPIO.setup(self.LED_2, GPIO.OUT)

    def led_on(self):
        print('LEDs on')
        GPIO.output(self.LED_1, GPIO.HIGH)
        GPIO.output(self.LED_2, GPIO.HIGH)

    def led_off(self):
        print('LEDs off')
        GPIO.output(self.LED_1, GPIO.LOW)
        GPIO.output(self.LED_2, GPIO.LOW)
