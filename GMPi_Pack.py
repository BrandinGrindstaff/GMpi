import os
import sys
import time
import datetime
import Adafruit_DHT
import tsl2591
import numpy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from picamera import PiCamera
from array import *


def PicSnap(filepath, rcloneProfile, rclonePath):
   #default file path is '/home/pi/uploadFolder/'
   #default rcloneProfile is 'myBox'
   timeStamp = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M")
   os.system('raspistill -vf -o {}image_{}.jpeg'.format(filepath, timeStamp))
   os.system('rclone move -v {}image_{}.jpeg {}:{}'.format(filepath, timeStamp, rcloneProfile, rclonePath))

def UploadFile(filepath, rcloneProfile, rclonePath):
   #uses datetime lib to generate a the current date
   date = datetime.datetime.today().strftime("%Y-%m-%d")
   #moves the sensorOutput.txt file to sensorOutput folder on Box
   #to change cloud storage destination, create a new configuration in rclone, and replace "myBox:/" with "yourConfigNameHere:/"
   os.system('rclone copy -v {}sensorOutput_{}.txt {}:{}'.format(filepath, date, rcloneProfile, rclonePath))

def UploadFile2(filepath, rcloneProfile, rclonePath, date):
    """
    Takes date as an argument too to upload output.
    """
    os.system('rclone copy -v {}sensorOutput_{}.txt {}:{}'.format(filepath, date, rcloneProfile, rclonePath))

def OpenFile(filepath):
   date = datetime.datetime.today().strftime("%Y-%m-%d")
   f = open('{}sensorOutput_{}.txt'.format(filepath, date) ,'a')
   # Write column headers for the output files. These will be in CSV format.
   print("date", "time", "temp", "humidity", "full_spectrum", "infrared", "lux", sep=",", file=f)
   f.close()


def BuildConfig():
   data = array('f',[0]*10)
   datum = 0

   for f in data:
      tsl = tsl2591.Tsl2591() # initialize light sensor
      full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and IR)
      lux = tsl.calculate_lux(full, ir) # convert raw values to lux
      data[datum] = lux
      datum += 1
      #time.sleep(1)

   #the maximum and minimum values of light in lux recorded by sensor
   minLight = min(data)
   maxLight = max(data)
   #The buffer variable adds a buffer to max and min values to prevent unwarranted alerts; change this value to your preference.
   buffer = 10

   #the maximum and minimum values of light in lux with buffer applied
   minimum = minLight - buffer
   maximum = maxLight + buffer

   #creates a configuration file using these values is configurable in config.txt file.
   config = open('config.txt', 'w')
   config.write('minimum_light_threshold={}\n' .format(minimum))
   config.write('maximum_light_threshold={}\n' .format (maximum))
   config.write('output_path=<REPLACE>\n')
   config.write('which_dht=22\n')
   config.write('which_data_pin=<REPLACE>\n')
   config.write('email_sender=<REPLACE>\n')
   config.write('email_receiver=<REPLACE>\n')
   config.write('rclone_profile=<REPLACE>\n')
   config.write('rclone_path=<REPLACE>\n')
   config.write('upload_once_per_day=True\n')
   config.close()


def ReadConfig():
   config = open('config.txt', 'r')
   res = {}
   for line in config:
       l = line.strip().split("=")
       res[l[0]] = l[1]

   return res


def LightAlert(email_sender, email_receiver):
   #set sender, recipients, and write subject here! Seperate by a ", " to add more! <MULTIPLE RECIPIENTS NOT TESTED!>
   #email_sender = 'pireslabgrowthmonitor@gmail.com'
   #email_reciever = ['pireslabgrowthmonitor@gmail.com', 'brandingrindstaff@gmail.com']
   subject = 'Growth Chamber Alert!'

   #Uses MIMEMultipart function to fill these text fields in email.
   msg = MIMEMultipart()
   msg['To'] = email_reciever
   msg['From'] = email_sender
   msg['Subject'] = subject

   #Add a body to your email!  msg.attach attaches body to email, and msg.as_string makes text info a string.
   body = 'Light below threshold during operation time!'
   msg.attach(MIMEText(body,'plain'))
   text = msg.as_string()

   #Sends the email and closes the program properly.
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(email_sender, 'calvbDe68bIh*>%DQM')
   server.sendmail(email_sender, email_reciever, text)
   server.quit()


def Sense(filepath, whichDHT, whichDataPin):
   # keeps track of the time
   # hour = datetime.datetime.now().strftime("%H") #hour of day
   # minute = datetime.datetime.now().strftime("%M") #minute of hour

   tsl = tsl2591.Tsl2591() # initialize light sensor
   timeStamp = datetime.datetime.today().strftime("%H:%M:%S") #I'm concidering reducing the precision here, because it can be a bit confusing to look at; no need for microseconds.
   date = datetime.datetime.today().strftime("%Y-%m-%d")
   date2 = datetime.datetime.today() - datetime.timedelta(days=1)
   config = ReadConfig()
   if not os.path.exists('{}sensorOutput_{}.txt'.format(filepath, date)):
       OpenFile(filepath)
       if config["upload_once_per_day"] == 'True':
           pass
           UploadFile2(filepath, config["rclone_profile"], config["rclone_path"], date2.strftime("%Y-%m-%d"))
   else:
       pass
   f = open('{}sensorOutput_{}.txt'.format(filepath, date) ,'a')
   
   #initialize the temp/humidity sensor. The Adafruit_DHT function takes(which DHT sensor you are using, which GPIO data pin you are using)
   humidity, temperature = Adafruit_DHT.read_retry(whichDHT, whichDataPin)
   full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
   lux = tsl.calculate_lux(full, ir) # convert raw values to lux

   #below prints outputs in shell, and writes them to output{date}.txt
   # This prints everything to the outut file in one line.
   print(date, timeStamp, temperature, humidity, full, ir, lux, sep=",", file=f)
   
   # This prints everything else to stdout.
   print("Temp: {0:0.1f} C\nHumidity: {1:0.1f} %\n".format(temperature, humidity))
   #f.write("Temp: {0:0.1f} C\nHumidity: {1:0.1f}%\n".format(temperature, humidity))

   print("Current date and time: \n", timeStamp)
   #f.write("Current date and time: {}\n".format(timeStamp))

   print("Full Spectrum Light: {}\n".format(full))
   #f.write("Full Spectrum Light: {}\n".format(full))

   print("Infrared Light: {}\n".format(ir))
   #f.write("Infrared Light: {}\n".format(ir))

   print("Calculated Lux: {}\n".format(lux))
   #f.write("Calculated Lux: {}\n".format(lux))

   print("\n")
   #f.write("\n")

   return lux
