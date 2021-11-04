# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:27:02 2021

@author: marti
"""


import requests

Latitude = ['41.8955','64.1353','31.7857','41.3949','38.9429','43.7683','43.6683']
Longitude = ['12.4823','-21.8952','35.2007','2.1756','16.3316','11.2590','12.5224']
Location = ['Rome','Reykjavik','Jerusalem','Barcelona','Lamezia Terme','Florence','Urbania']

for i in range(len(Location)):
    url = 'https://api.open-meteo.com/v1/forecast?latitude='+ Latitude[i] +'&longitude='+ Longitude[i] +'&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum&timezone=Europe%2FBerlin'
    response = requests.get(url)
    file = open("Forecast_"+ Location[i] +".json", "w+")
    print(file.name)
    file.writelines(response.text)
    file.close()
    