#!/usr/bin/env python3

from GMPi_Pack import Sense
from GMPi_Pack import UploadFile
from GMPi_Pack import PicSnap
from GMPi_Pack import SlackAlert
from GMPi_Pack import ReadConfig

config = ReadConfig()
filepath = config["output_path"]
rcloneProfile = config["rclone_profile"]
whichDHT = config["which_dht"]
whichDataPin = config["which_data_pin"]
minLight = float(config["minimum_light_threshold"])
maxLight = float(config["maximum_light_threshold"])

print( "Light Perameters Set")
print('Max is: {}'.format(maxLight))
print('Min is: {}'.format(minLight))
#OpenFile(filepath)

#sense also returns current light intensity value, possiably others in the future.
sense_out = Sense(filepath, whichDHT, whichDataPin)

if (sense_out["lux"] < minLight or sense_out["lux"] > maxLight):
	SlackAlert(config["slack_webhook"], "Light")
	print('LightAlert sent')
#UploadFile(filepath, rcloneProfile)
#PicSnap(filepath, rcloneProfile)

