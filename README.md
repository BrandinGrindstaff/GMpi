# GMpi---NOT UP TO DATE
A growth chamber sensing system using the Raspberry Pi as a platform


These scripts must be run in sequence.  
	Run openFile.py first, 
	sensingScript.py, and snapPic.py in any order after openFile.py
	then upload.py last. 

They must all be run in "python3" to avoid errors. 

They also should not be run as admin,
no "sudo" as it causes errors with permissions while uploading.

a folder named "uploadFolder" must be created in home/pi/ to function because all file paths are hard coded.

an rclone config named "myBox" must be created

in your cloud storage destination you must create a folder named "GMPi"
with two folders inside it called "sensorOutput" and "photos".  

dependent on 2 external libraries and one program to run
	python-tsl 2591 *requires a dependency called libffi to run.  aquire this via this command: sudo apt-get install libffi -dev
	Adafruit_Python_DHT
	rclone program
