#!/usr/bin/env python3

import os
from sys import exit, argv
from GMPi_Pack import BuildConfig

print("Making configuration file: config.txt")
print(len(argv))
try:
	if len(argv) == 3:
		dht      = argv[1]
		data_pin = argv[2]
	elif len(argv) == 4:
		dht      = argv[2]
		data_pin = argv[3]
	else:
		print("ERROR: Unable to parse DHT and Data Pin (should be integers)...\n")
		print("Usage:")
		print("  ./configure.py <dht> <data pin>")
		exit(-1)
except:
	print("ERROR: Unable to parse DHT and Data Pin (should be integers)...\n")
	print("Usage:")
	print("  ./configure.py <dht> <data pin>")
	exit(-1)

if os.path.exists('config.txt'):
	print("\nError: Configuration file already exists.")
	print("       Please remove it before generating a new one.\n\n")
	exit(-1)

BuildConfig(dht, data_pin)
print("Done.\n\n")

print("Please open config.txt and enter the appropriate information")
print("for all entries with <REPLACE> as the current value.\n\n")
