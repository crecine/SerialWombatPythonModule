import time
import RPi.GPIO as GPIO

from serialwombat.chip import SWChipPigpioI2c
from serialwombat.pin import AnalogInput, QuadEnc, Servo

GPIO.setwarnings(False)

sw = SWChipPigpioI2c(3,4,0x6D)

sw.begin(False)

print(sw.version)
print(sw.model)
print(sw.fwVersion)

servo = Servo(sw)
servo.attach(3)

analog = AnalogInput(sw)
analog.begin(2)

knob = QuadEnc(sw)
knob.begin(0,1,10)

print("Pin 2 analog: ", analog.readCounts())

print("Source Voltage mv: ", sw.readSupplyVoltage_mV())

time.sleep(2)
while(True):
    print(knob.read(), " ", analog.readCounts())
    servo.write16bit(analog.readCounts())