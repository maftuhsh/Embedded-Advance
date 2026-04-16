from gpiozero import Servo
from time import sleep

# Setup servo di GPIO17 (BCM) (pin 11 pada rasberry pi)
servo = Servo(17)

def set_angle(angle):
    """
    Mengubah sudut (0-180 derajat)
    ke nilai servo (-1 sampai 1)
    """
    value = (angle / 90) - 1
    servo.value = value
    sleep(1)

# Loop pergerakan
num_loops = 1
count = 0

try:
    while count < num_loops:
        print("Set ke 0 derajat")
        set_angle(0)

        print("Set ke 90 derajat")
        set_angle(90)

        print("Set ke 120 derajat")
        set_angle(120)

        count += 1

except KeyboardInterrupt:
    print("Program dihentikan")