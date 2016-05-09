import time
import bluepy 
from bluepy.bluepy import sensortag

tag = sensortag.SensorTag('b0:b4:48:bc:fd:81')

time.sleep(1.0)
tag.lightmeter.enable()
for i in range(50):
    tag.waitForNotifications(1.0)
    print tag.lightmeter.read()
tag.disconnect()
del tag
