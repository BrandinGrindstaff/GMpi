#!/usr/bin/env python3

from GMPi_Pack import UploadFile, ReadConfig

# Parse config file
config = ReadConfig()
#filepath = '/home/pi/uploadFolder/'
#rcloneProfile = 'myBox'

UploadFile(config["output_path"], config["rclone_profile"], config["rclone_path"])
