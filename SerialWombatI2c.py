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
        # self.pi.bb_i2c_open(self.sda,self.scl,self.freq)
        with I2CTarget(self.scl, self.sda, (self.i2cAddress)) as device:
            # set address i2cAddress, start, write 8 bytes, stop, exit
            # self.pi.bb_i2c_zip(self.sda,[4, self.i2cAddress, 2, 7, 8] + tx+ [3,0])
            r = device.request(timeout=0)
            n = r.write(bytes(tx))
            
            time.sleep(0.002)
            
            # set address i2cAddress, start, read 8 bytes, stop, exit
            # rx = self.pi.bb_i2c_zip(self.sda,[4, self.i2cAddress, 2, 6, 8, 3,0])
            b = r.read(n=8)
            
            #self.pi.bb_i2c_close(self.sda)
            r.__exit__()
            device.deinint()
        return n,b  #TODO add error check, size check
