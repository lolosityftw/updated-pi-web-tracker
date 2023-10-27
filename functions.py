from testSensor import *
from datetime import datetime
import time

def getSensors():
        t,h = Sensor()
        c = datetime.now().strftime("%H:%M:%S")
        return c,t,h
    
def writefile(time,temperature,humidity):
    f = open("data.txt", "a")
    l = [time,temperature,humidity]
    f.write(str(l) + "\n")
    f.close()

