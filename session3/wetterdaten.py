#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:58:46 2023

@author: fbo
"""
# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2023, 4,1)
end = datetime(2023, 9, 30)


from meteostat import Stations
stations = Stations()
stations = stations.nearby(52.4667,13.4)
stationList = stations.fetch(20)
selectedStation = stations.fetch(1)
data = Daily(selectedStation, start, end)
data = data.fetch()


# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()

#berechne die Eignung für Weinbau nach huglin
huglinDaily=(data["tmax"]+data["tavg"]-20)/2
huglinDaily[huglinDaily<0]=0 # Das stimmt so in Wikipedia nicht...
print(huglinDaily.sum()*1.06)
# 