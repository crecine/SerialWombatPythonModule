
class SerialWombatPin (object):
    def __init__(self, sw, pin):
        self._sw = sw
        self._pin = pin

    @property
    def pin(self):
        return self._pin

class DigitalPin (SerialWombatPin):
    def begin(self, state, pullDown = False, openDrain = False):
        self._sw._configureDigitalPin(self._pin, state, pullDown, openDrain)
        self._state = state
        self._pullDown = pullDown
        self._openDrain = openDrain

    def digitalWrite(self,val):
        if self._state == 1:
            return self._sw.writePublicData(self._pin, val)

    def digitalRead(self):
        return self._sw.readPublicData(self._pin)

    @property
    def pinConfig(self):
        return (self._state, self._pullDown, self._openDrain)


class AnalogInput(SerialWombatPin):
    def begin(self, averageSamples=64, filterConstant = 0xFF80, output = 0):
        self._pinMode = 2 #Analog input
        tx = [200, self._pin,self._pinMode, 0, 0, 0, 0, 0]
        count, rx = self._sw.sendPacket(tx)
        if (count < 0):
            return count
        tx = [201, self._pin, self._pinMode, averageSamples & 0xFF, int(averageSamples / 256), filterConstant& 0xFF, int(filterConstant / 256), output]
        count, rx = self._sw.sendPacket(tx)
        self.updateSupplyVoltage_mV()
        return count

    def readVoltage_mV(self):
        reading = self._sw.readPublicData()
        reading *= self._sw._supplyVoltagemV
        reading /= 65536
        return (reading)

    def readCounts(self):
        return self._sw.readPublicData()

    def readFiltered_mV(self):
        x = self.readFilteredCounts()
        if (x < 0):
            return (0)
        x *= self._sw._supplyVoltagemV
        x /= 65536
        return (x)

    def readFilteredCounts(self):
        tx = [204, self._pin, self._pinMode, 0x55, 0x55, 0x55, 0x55, 0x55]
        count,rx = self._sw.sendPacket(tx)
        if (count < 0):
            return 0
        return (rx[5] + 256 * rx[6])

    def readAveragedCounts_mV(self):
        x = self.readAveragedCounts()
        if (x < 0):
            return (0)
        x *= self._sw._supplyVoltagemV
        x /= 65536
        return (x)

    def readAveragedCounts(self):
        tx = [204, self._pin, self._pinMode, 0x55, 0x55, 0x55, 0x55, 0x55]
        count,rx = self._sw.sendPacket(tx)
        if (count < 0):
            return 0
        return (rx[3] + 256 * rx[4])

    def updateSupplyVoltage_mV(self):
        return self._sw.readSupplyVoltage_mV()

    def readMaximumCounts_mV(self, resetAfterRead = False):
        x = self.readMaximumCounts(resetAfterRead)
        x *= self._sw._supplyVoltagemV
        x /= 65536
        return (x)

    def readMaximumCounts(self,resetAfterRead = False):
        tx = [203, self._pin, self._pinMode, 0x55, 0x55, 0x55, 0x55, 0x55]
        if (resetAfterRead):
            tx[3] = 1

        count,rx = self._sw.sendPacket(tx)
        if (count < 0):
            return 0
        return (rx[5] + 256 * rx[6])

    def readMinimumCounts_mV(self, resetAfterRead = False):
        x = self.readMinimumCounts(resetAfterRead)
        x *= self._sw._supplyVoltagemV
        x /= 65536
        return (x)

    def readMinimumCounts(self, resetAfterRead = False):
        tx = [203, self._pin, self._pinMode, 0x55, 0x55, 0x55, 0x55, 0x55]
        if (resetAfterRead):
            tx[3] = 1

        count,rx = self._sw.sendPacket(tx)
        if (count < 0):
            return 0
        return (rx[3] + 256 * rx[4])

class Servo (DigitalPin):
    _min = 544
    _max = 2400
    _reverse = 0
    _position = 0

    def attach(self, pin, init_angle, minimum = 544, maximum = 2400, min_angle = 0, max_angle = 180, reverse = False):
        self._pin = pin
        self._min = minimum
        self._max = maximum
        self._min_angle = min_angle
        self._max_angle = max_angle
        if (reverse):
            self._reverse = 1
        else:
            self._reverse = 0
        self._pinMode =  3 # Servo

        tx = [200, self._pin, self._pinMode,self._pin,self._position & 0xFF, int(self._position / 256), self._reverse, 0x55]

        self._sw.sendPacket(tx)
        duration = self._max - self._min
        tx2 = [201, self._pin, self._pinMode,self._min & 0xFF, int(self._min / 256), duration & 0xFF, int(duration / 256), 0x55, 0x55]
        self._sw.sendPacket(tx2)
        
        self.write(init_angle)

    def write16bit(self, position):
        self._position = int(position)
        self._sw.writePublicData(self._position)

    def write(self, angle):
        if self._min_angle < angle < self._max_angle:
            self.write16bit(int(65536 * angle / self._max_angle))
        elif angle < self._min_angle:
            pass
        elif angle > self._max_angle:
            pass
        elif angle == self._max_angle:
            self.write16bit(65535)
        elif angle == self._min_angle:
            self.write16bit(0)

    def read(self):
        returnval = self._position * (self._max - self._min) / 65536
        return int(returnval)

class UltrasonicDistanceSensor (SerialWombatPin):
    def begin(self, driver, triggerPin, autoTrigger = True, pullUp = False):
        self._pinMode =  27 # Ultrasonic Distance

        tx = [200, self._pin, self._pinMode,driver, triggerPin, pullUp, autoTrigger, 0x55]
        self._sw.sendPacket(tx)

    def readPulseCount(self):
        tx = [202, self._pin, self._pinMode, 0x55, 0x55, 0x55, 0x55, 0x55]
        count, rx= self._sw.sendPacket(tx)
        if (count >= 0):
            return (rx[5] + 256*rx[6])
        else:
            return(0)

    def manualTrigger(self):
        tx = [201, self._pin, self._pinMode, 1, 0x55, 0x55, 0x55, 0x55]
        self._sw.sendPacket(tx)

class PWM (DigitalPin):
    _dutyCycle = 0
    def begin(self, pin, dutyCycle = 0, invert = False):
        self._pin = pin
        self._pinMode =  16 # PWM

        tx = [200, self._pin, self._pinMode,self._pin,dutyCycle & 0xFF, int(dutyCycle / 256), invert,0x55]
        self._sw.sendPacket(tx)

    def writeDutyCycle(self, dutyCycle):
        self._sw.writePublicData(dutyCycle)

class PWM_4AB (PWM):
    def setFrequency(self, frequencyEnum):
        tx = [220, self._pin, frequencyEnum, 0x55, 0x55, 0x55, 0x55]
        self._sw.sendPacket(tx)

class PWM_18AB (PWM):
    def writePeriod_uS(self, period_uS):
        tx = [220, self._pin, int(period_uS / (256*256*256)), int(period_uS / (256*256))& 0xFF, int(period_uS / (256)) & 0xFF, period_uS & 0xFF, 0x55]
        self._sw.sendPacket(tx)

    def writeFrequency_Hz(self, frequency_Hz):
        self.writePeriod_uS(int(1000000/frequency_Hz))

class QuadEnc (SerialWombatPin):
    def begin(self,pin,secondPin,debounce_mS = 10,pullUpsEnabled = True, readState = 6): #6 = both, polling
        self._pin = pin
        self._pinMode = 5 #Quadrature Encoder
        tx = [200, self._pin, self._pinMode, debounce_mS & 0xFF, int(debounce_mS/256), secondPin, readState, int(pullUpsEnabled == True)]
        count, rx = self._sw.sendPacket(tx)
        return count

    def read(self, replacementValue = None):
        if (replacementValue is None):
            return self._sw.readPublicData()
        return self._sw.writePublicData(replacementValue)

    def write(self, value):
        count, rx = self._sw.writePublicData(value)
        return count