import machine
import time

led = machine.Pin(2,machine.Pin.OUT)


for i in range(100):
    led.value(1)
    time.sleep(.4)
    led.value(0)
    time.sleep(.1)
    
    
import ugit
ugit.pull_all()
