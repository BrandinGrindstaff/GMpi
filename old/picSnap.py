import os
import sys
import datetime
from picamera import PiCamera

timeStamp = datetime.datetime.now().strftime("%m-%d-%y_%H:%M")

os.system('raspistill -vf -o /home/pi/uploadFolder/image_{}.jpeg' .format(timeStamp))
#os.system('rclone move -v /home/pi/uploadFolder/image_{}.jpeg myBox:/GMPi/photos' .format(timeStamp))

