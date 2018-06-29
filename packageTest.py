from GMPi_Pack import Sense
from GMPi_Pack import UploadFile
from GMPi_Pack import OpenFile
from GMPi_Pack import PicSnap
from GMPi_Pack import AlertPerameters
from GMPi_Pack import LightAlert

filepath = '/home/pi/uploadFolder/'
rcloneProfile = 'myBox'
whichDHT = 22
whichDataPin = 4
minLight, maxLight = AlertPerameters()

print( "Light Perameters Set")
print('Max is: {}'.format(maxLight))
print('Min is: {}' .format(minLight))
#OpenFile(filepath)

#sense also returns current light intensity value, possiably others in the future.
currentLight = Sense(filepath, whichDHT, whichDataPin)

if (currentLight < minLight or currentLight > maxLight):
   LightAlert()
   print('LightAlert sent')
#UploadFile(filepath, rcloneProfile)
#PicSnap(filepath, rcloneProfile)

