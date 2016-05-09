import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)  # set pin 21 to output

p = GPIO.PWM(40, 60)  # set the PWM channel (pin 40) and frequency (60 Hz)

p.start(0)  # Set the PWM duty cycle in percent 0-100 

try:

    while True:

        for dc in range(100):
            p.ChangeDutyCycle(dc)
            time.sleep(0.02)

        for dc in range(100):
            p.ChangeDutyCycle(100-dc)
            time.sleep(0.02)

except KeyboardInterrupt:
    pass

p.stop() # Stop PWM
GPIO.cleanup()

