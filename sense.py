#!/usr/bin/env python3

from GMPi_Pack import Sense
from GMPi_Pack import ReadConfig
from GMPi_Pack import SlackAlert, ReadConfig
import datetime

config = ReadConfig()
whichDHT = int(config["which_dht"]) # default 22
whichDataPin = int(config["which_data_pin"]) # default 4. What is the data pin?
filepath = config["output_path"]
sethour = datetime.datetime.now().strftime("%H") #hour of day
hour = int(sethour)
sense_out = Sense(filepath, whichDHT, whichDataPin)

maxLight = float(config["maximum_light_threshold"])
minLight = float(config["minimum_light_threshold"])
maxTemp = float(config["maximum_temp_threshold"])
minTemp = float(config["minimum_temp_threshold"])
maxHumidity = float(config["maximum_humidity_threshold"])
minHumidity = float(config["minimum_humidity_threshold"])

if hour >= int(config["hr_lights_on"]) or hour <= int(config["hr_lights_off"]):
	if (sense_out["lux"] < minLight or sense_out["lux"] > maxLight):
		SlackAlert(config["slack_webhook"], "Light")

if (sense_out["temperature"] < minTemp or sense_out["temperature"] > maxTemp):
	SlackAlert(config["slack_webhook"], "Temperature")

if (sense_out["humidity"] < minHumidity or sense_out["humidity"] > maxHumidity):
	SlackAlert(config["slack_webhook"], "Humidity")