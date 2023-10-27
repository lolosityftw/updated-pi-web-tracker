import random
from datetime import datetime

demoTempValues = 21.3, 21.1, 21.9, 20.1, 19.7, 18.8, 18.3
demoHumidityValues = 64.5, 64.3, 63.9, 64.1, 62.9, 70.1, 71.2

def Sensor():
    h = demoTempValues[random.randrange(0, len(demoTempValues))]
    t = demoHumidityValues[random.randrange(0, len(demoHumidityValues))]

    return h, t;


