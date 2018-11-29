#!/usr/bin/env python3

from GMPi_Pack import PicSnap, ReadConfig

# Parse config file
config = ReadConfig()
#filepath = '/home/pi/uploadFolder/'
#rcloneProfile = 'myBox'

#Then pass output_path and rclone_profile to PicSnap fxn.
PicSnap(config["output_path"], config["rclone_profile"], config["rclone_path"])
