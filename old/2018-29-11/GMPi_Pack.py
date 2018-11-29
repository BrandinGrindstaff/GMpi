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


def PicSnap(filepath, rcloneProfile):
#default file path is '/home/pi/uploadFolder/'
#default rcloneProfile is 'myBox'
   timeStamp = datetime.datetime.now().strftime("%m-%d-%y_%H:%M")
   os.system('raspistill -vf -o {}image_{}.jpeg' .format(filepath, timeStamp))
   os.system('rclone move -v {}image_{}.jpeg {}:/GMPi/photos' .format(filepath, timeStamp, rcloneProfile))


def UploadFile(filepath, rcloneProfile):
#uses datetime lib to generate a the current date
   date = datetime.datetime.now().strftime("%m-%d-%y")
#moves the sensorOutput.txt file to sensorOutput folder on Box
#to change cloud storage destination, create a new onfiguration in rclone, and replace "myBox:/" with "yourConfigNameHere:/"
   os.system('rclone move -v {}sensorOutput_{}.txt :/GMPi/sensorOutput' .format(filepath, date, rcloneProfile))


def OpenFile(filepath):
   date = datetime.datetime.now().strftime("%m-%d-%y")
   f = open('{}sensorOutput_{}.txt'.format(filepath, date) ,'x+')
   f.close()


def AlertPerameters():
   data = array('f',[0]*10)
   datum = 0

   for f in data:
      tsl = tsl2591.Tsl2591() # initialize light sensor
      full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum an$
      lux = tsl.calculate_lux(full, ir) # convert raw values to lux
      data[datum] = lux
      datum += 1
      #time.sleep(1)

   minLight = min(data)
   maxLight = max(data)

   #print(maxLight)
   #print(minLight)
   #print("\n")

   #for f in data:
      #print(f)

   #print("\n")
   #print('Tne minimum is: {}' .format(minLight))
   #print('The maximum is: {}' .format(maxLight))

   return (minLight, maxLight)


def LightAlert():
#set sender, recipients, and write subject here! Seperate by a ", " to add more! <MULTIPLE RECIPIENTS NOT TESTED!>
   email_sender = 'pireslabgrowthmonitor@gmail.com'
   email_reciever = ['pireslabgrowthmonitor@gmail.com', 'brandingrindstaff@gmail.com']
   subject = 'Email Alert!'

#Uses MIMEMultipart function to fill these text fields in email.
   msg = MIMEMultipart()
   msg['To'] =", ".join(email_reciever)
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
#keeps track of the time
   hour = datetime.datetime.now().strftime("%H") #hour of day
   minute = datetime.datetime.now().strftime("%M") #minute of hour

#prevents the rest of the script from running from 11:59 to 12:01 to prevent scheduling conflicts with other programs.
   if hour != 11 or minute != 59:
      if hour !=0 or minute != 0:

         tsl = tsl2591.Tsl2591() # initialize light sensor
         timeStamp = datetime.datetime.now() #I'm concidering reducing the precision here, because it can be a bit confusing to look at; no need for microseconds.
         date = datetime.datetime.now().strftime("%m-%d-%y")
         f = open('{}sensorOutput_{}.txt'.format(filepath, date) ,'a')

#initialize the temp/humidity sensor. The Adafruit_DHT function takes(which DHT sensor you are using, which GPIO data pin you are using)
         humidity, temperature = Adafruit_DHT.read_retry(whichDHT, whichDataPin)
         full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
         lux = tsl.calculate_lux(full, ir) # convert raw values to lux

#below prints outputs in shell, and writes them to output{date}.txt
         print("Temp: {0:0.1f} C\nHumidity: {1:0.1f} %\n".format(temperature, humidity))
         f.write("Temp: {0:0.1f} C\nHumidity: {1:0.1f}%\n".format(temperature, humidity))

         print("Current date and time: \n", timeStamp)
         f.write("Current date and time: {}\n".format(timeStamp))

         print("Full Spectrum Light: {}\n".format(full))
         f.write("Full Spectrum Light: {}\n".format(full))

         print("Infrared Light: {}\n".format(ir))
         f.write("Infrared Light: {}\n".format(ir))

         print("Calculated Lux: {}\n".format(lux))
         f.write("Calculated Lux: {}\n".format(lux))

         print("\n")
         f.write("\n")

         return lux
