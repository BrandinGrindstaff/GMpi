#!/usr/bin/env python3

from GMPi_Pack import Sense
from GMPi_Pack import ReadConfig
from GMPi_Pack import LightAlert, ReadConfig
import datetime

config = ReadConfig()
whichDHT = int(config["which_dht"]) # default 22
whichDataPin = int(config["which_data_pin"]) # default 4. What is the data pin?
filepath = config["output_path"]
sethour = datetime.datetime.now().strftime("%H") #hour of day
hour = int(sethour)
currentLight = Sense(filepath, whichDHT, whichDataPin)

if hour >= 12 or hour <= 20:
   maxLight = float(config["maximum_light_threshold"])
   minLight = float(config["minimum_light_threshold"])

#for debugging
   #print(currentLight)
   #print(maxLight)
   #print(minLight)

   if (currentLight < minLight or currentLight > maxLight):
      LightAlert(config["email_sender"], config["email_receiver"])
      #print('Email Alert Sent!')
