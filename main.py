from nicegui import ui;
from datetime import datetime
from testSensor import *
import json;

ui.dark_mode().auto


now = datetime.now();
time = now.strftime("%H:%M:%S");

t,h = readSensor()

with ui.grid(columns=2):
    ui.label('Time:')
    ui.label(time)

    ui.label('Temperature:')
    ui.label(str(t) + " C")

    ui.label('Humidity:')
    ui.label(str(h) + " %")

ui.run()