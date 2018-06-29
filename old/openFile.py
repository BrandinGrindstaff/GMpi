import datetime

date = datetime.datetime.now().strftime("%m-%d-%y")
f = open('/home/pi/uploadFolder/sensorOutput_{}.txt'.format(date) ,'x+')
f.close()
