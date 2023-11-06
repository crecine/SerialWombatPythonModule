import SerialWombat
import time
from i2ctarget import I2CTarget


class SerialWombatChipI2c(SerialWombat.SerialWombatChip):
    i2cAddress = 0
    sda = 17
    scl = 27
    freq = 100000
    def __init__(self,sda,scl,i2cAddress,freq = 100000):
        self.sda = sda
        self.scl = scl
        self.freq = freq
        self.i2cAddress = i2cAddress


    def sendPacket (self,tx):
        tx = bytearray(tx)
        # self.pi.bb_i2c_open(self.sda,self.scl,self.freq)
        i2c = busio.I2C(self.scl, self.sda, frequency=self.freq)
        while not i2c.try_lock():
            pass
        
        # set address i2cAddress, start, write 8 bytes, stop, exit
        # self.pi.bb_i2c_zip(self.sda,[4, self.i2cAddress, 2, 7, 8] + tx+ [3,0])
        i2c.writeto(self.i2cAddress, tx)
        
        # set address i2cAddress, start, read 8 bytes, stop, exit
        # rx = self.pi.bb_i2c_zip(self.sda,[4, self.i2cAddress, 2, 6, 8, 3,0])
        rx = bytearray([0]*8)
        n = 0
        while rx == bytearray([0]*8):
            n += 1
            time.sleep(0.002)
            i2c.readfrom_into(self.i2cAddress,rx)
            if n>= 100:
                break
        
        #self.pi.bb_i2c_close(self.sda)
        i2c.unlock()
        i2c.deinit()
        return len(rx),rx  #TODO add error check, size check
