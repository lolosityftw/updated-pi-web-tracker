from functions import *
from testSensor import *
from datetime import datetime
import time

def getSensors():
        t,h = Sensor()
        c = datetime.now().strftime("%H:%M:%S")
        return c,t,h


    
while True:
    writefile(getSensors()[0],getSensors()[1],getSensors()[2])
    time.sleep(1)

