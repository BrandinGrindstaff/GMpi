import os
import sys
import datetime

#uses datetime lib to generate a the current date
date = datetime.datetime.now().strftime("%m-%d-%y")

#moves the sensorOutput.txt file to sensorOutput folder on Box
#to change cloud storage destination, create a new onfiguration in rclone, and replace "myBox:/" with "yourConfigNameHere:/"
os.system('rclone move -v /home/pi/uploadFolder/sensorOutput_{}.txt myBox:/GMPi/sensorOutput' .format(date))
