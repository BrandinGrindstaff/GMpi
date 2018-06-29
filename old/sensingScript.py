import Adafruit_DHT
import datetime
import tsl2591

#keeps track of the time
hour = datetime.datetime.now().strftime("%H") #hour of day
minute = datetime.datetime.now().strftime("%M") #minute of hour

#prevents the rest of the script from running from 11:59 to 12:01 to prevent scheduling conflicts with other programs.
if hour != 11 or minute != 59:
   if hour !=0 or minute != 0:

      tsl = tsl2591.Tsl2591() # initialize light sensor
      timeStamp = datetime.datetime.now() #I'm concidering reducing the precision here, because it can be a bit confusing to look at; no need for microseconds.
      date = datetime.datetime.now().strftime("%m-%d-%y")
      f = open('/home/pi/uploadFolder/sensorOutput_{}.txt'.format(date) ,'a')

#initialize the temp/humidity sensor. The Adafruit_DHT function takes(which DHT sensor you are using, which GPIO data pin you are using)
      humidity, temperature = Adafruit_DHT.read_retry(22, 4)
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

