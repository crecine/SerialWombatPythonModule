import time
import RPi.GPIO as GPIO

from serialwombat.chip import SWChipTCP
from serialwombat.pin import AnalogInput

GPIO.setwarnings(False)

sw = SWChipTCP("192.168.1.185", 4000)

sw.begin(False)

print(sw.version)
print(sw.model)
print(sw.fwVersion)

analog0 = AnalogInput(sw, 0)
analog1 = AnalogInput(sw, 1)
analog2 = AnalogInput(sw, 2)
analog3 = AnalogInput(sw, 3)
analog4 = AnalogInput(sw)
analog16 = AnalogInput(sw)
analog17 = AnalogInput(sw)
analog18 = AnalogInput(sw)
analog19 = AnalogInput(sw)
analog0.begin()
analog1.begin()
analog2.begin()
analog3.begin()
analog4.begin(4)
analog16.begin(16)
analog17.begin(17)
analog18.begin(18)
analog19.begin(19)

print("Source Voltage mv: ",sw.readSupplyVoltage_mV())

time.sleep(2)
while(True):
    print("0: ",analog0.readCounts(), " 1: ", analog1.readCounts(), " 2: ", analog2.readCounts(), " 3: ", analog3.readCounts(), " 4: ", analog4.readCounts(),
          " 16: ", analog16.readCounts(), " 17: ", analog17.readCounts(), " 18: ", analog18.readCounts(), " 19: ", analog19.readCounts())
