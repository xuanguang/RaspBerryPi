import time
from sense_hat import SenseHat

sense = SenseHat()
deplay_time = 0.5

r = 255
g = 255
b = 255

sense.clear((r, g, b))
time.sleep(deplay_time)

r = 0
sense.clear((r, g, b))
time.sleep(deplay_time)

g = 0
sense.clear((r, g, b))
time.sleep(deplay_time)

b = 0
sense.clear((r, g, b))
time.sleep(deplay_time)          
           
           
