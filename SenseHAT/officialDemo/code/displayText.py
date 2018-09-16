'''https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat'''

from sense_hat import SenseHat

sense = SenseHat()
sense.show_message("Hello world", .2,  [0, 255, 255], [0, 0, 0])
