from nicegui import ui;
from datetime import datetime
from testSensor import *
import json;

ui.dark_mode().auto


now = datetime.now();
time = now.strftime("%H:%M:%S");

t,h = readSensor()
temp = readSensor()

print(temp[0])


with ui.grid(columns=2):
    ui.label('Time:')
    timeLabel = ui.label()
    ui.timer(1.0, lambda: timeLabel.set_text(datetime.now().strftime("%H:%M:%S")))

    ui.label('Temperature:')
    tLabel = ui.label()
    ui.timer(1.0, lambda: tLabel.set_text(str(readSensor()[0]) + " C"))

    ui.label('Humidity:')
    hLabel = ui.label()
    ui.timer(1.0, lambda: hLabel.set_text(str(readSensor()[1]) + " %"))



def writefile(time,temperature,humidity):
    f = open("data.txt", "a")
    l = [time,temperature,humidity]
    f.write(str(l) + "\n")
    f.close()



ui.run()


writefile(time,t,h)
print("test")

