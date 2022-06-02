import time

from serialwombat.chip import SWChipUART
from serialwombat.pin import UltrasonicDistanceSensor

sw = SWChipUART("/dev/ttyUSB0")

sw.begin(False)

print(sw.version)
print(sw.model)
print(sw.fwVersion)


distanceSensor = UltrasonicDistanceSensor(sw, 10) #echo pin10

distanceSensor.begin(0, # HC_SR04 driver
                     11) # Trigger pin

print("Source Voltage mv: ",sw.readSupplyVoltage_mV())

time.sleep(2)
while(True):
    print("Distance (mm): ",distanceSensor._sw.readPublicData()," Pulse count: ",distanceSensor.readPulseCount())
