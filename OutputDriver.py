import RPi.GPIO as GPIO
from time import sleep

class OutputDriver:

    class LED:
        def __init__(self, pin):
            self.pin = pin
            self._state = False
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, state):
            self._state = state
            GPIO.output(self.pin, state)

        def on(self):
            GPIO.output(self.pin, True)
            self._state = True

        def off(self):
            GPIO.output(self.pin, False)
            self._state = True

        def toggle(self):
            GPIO.output(self.pin, ~self._state)
            self._state = ~self._state

    def __init__(self, total_leds):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.leds = []
        gpios = [14, 15, 18, 23, 24, 25, 8, 7]
        for i in range(total_leds):
            new_led = self.LED(gpios[i])
            self.leds.append(new_led)

    def all_on(self):
        for led in self.leds:
            led.on()

    def all_off(self):
        for led in self.leds:
            led.off()

    def walking_dot(self, delay=0.3, direction="up"):
        self.all_off()

        if direction is "up":
            indexes = range(len(self.leds))
        elif direction is "down":
            indexes = reversed(range(len(self.leds)))
        else:
            print("Wrong direction selected")

        for i in indexes:
            self.leds[i].on()
            if i > 1:
                self.leds[i-1].off()
            sleep(delay)

        self.leds[-1].off()







