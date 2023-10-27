from functions import *
from testSensor import *
from datetime import datetime
import threading
import time as clock
import os

c,t,h = 0,0,0
r = open("data.txt", "r")

def writefile():
    while True:
        f = open("data.txt", "a")
        f.flush()
        clock.sleep(1)
        t,h = Sensor()
        c = datetime.now().strftime("%H:%M:%S")
        l = [c,t,h]
        f.write(str(l) + "\n")
        f.close()



threading.Thread(target=writefile, args=()).start()

def readData():
    print (r.tell())

readData()

print(time)

