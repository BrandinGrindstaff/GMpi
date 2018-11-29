#!/usr/bin/env python3

import os
from sys import exit
from GMPi_Pack import BuildConfig

print("Making configuration file: config.txt")
if os.path.exists('config.txt'):
	print("\nError: Configuration file already exists.")
	print("       Please remove it before generating a new one.\n\n")
	exit(-1)

BuildConfig()
print("Done.\n\n")

print("Please open config.txt and enter the appropriate information")
print("for all entries with <REPLACE> as the current value.\n\n")

