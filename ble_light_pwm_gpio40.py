import time
import bluepy 
from bluepy.bluepy import sensortag

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)  # set pin 40 to output

p = GPIO.PWM(40, 60)  # set the PWM channel (pin 40) and frequency (60 Hz)

tag = sensortag.SensorTag('b0:b4:48:bc:fd:81')

p.start(0)  # Set the PWM duty cycle in percent 0-100

time.sleep(1.0)
tag.lightmeter.enable()

try:

    while True:

        tag.waitForNotifications(.2)
        reading = tag.lightmeter.read()
        print reading
        if reading > 180:
            reading = 180
        p.ChangeDutyCycle(100-(reading/1.8))

except KeyboardInterrupt:
    pass

p.stop() # Stop PWM
tag.disconnect()
del tag
GPIO.cleanup()



