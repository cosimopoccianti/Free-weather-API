# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:27:02 2021

@author: Martina, Cosimo , Carlo 
"""

import pandas
import json
import requests

Latitude = ['41.8955','64.1353','31.7857','41.3949','38.9429','43.7683','43.6683','41.8696', '39.6530','52.520396']
Longitude = ['12.4823','-21.8952','35.2007','2.1756','16.3316','11.2590','12.5224','15.0110', '16.5363','13.393949']
Location = ['Rome','Reykjavik','Jerusalem','Barcelona','Lamezia Terme','Florence','Urbania','San Martino in Pensilis', 'Schiavonea','Berlino']



for i in range(len(Location)):
    url = 'https://api.open-meteo.com/v1/forecast?latitude='+ Latitude[i] +'&longitude='+ Longitude[i] +'&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,pressure_msl,precipitation,freezinglevel_height&timezone=Europe%2FBerlin'
    response = requests.get(url)
    file = open("Forecast_"+ Location[i] +".json", "w+")
    print(file.name) #si può togliere ok va bene
    file.writelines(response.text)
    file.close()
    
result = []

for city in Location:

    json_data = json.load(open('Forecast_'+ city +'.json'))
    
    hourly = json_data['hourly']
    
    time = hourly['time'] 
    temp = hourly['temperature_2m']
    apptemp = hourly['apparent_temperature']
    hum = hourly['relativehumidity_2m']
    pre = hourly['precipitation']
    dew = hourly['dewpoint_2m']
    freez = hourly['freezinglevel_height']
    pres = hourly['pressure_msl']
    
    for i in range(len(time)):
        x = [city] + [time[i]] + [temp[i]] + [apptemp[i]] + [hum[i]] + [pre[i]] + [dew[i]] + [freez[i]] + [pres[i]]
        result.append(x)
    
csv_file_path = 'Forecast_merged.csv'
df = pandas.DataFrame(result)
df.columns = ['city','time','temperature','apparent temperature','relative humidity','precipitation', 'dewpoint','freeing level', 'pressure']
df.to_csv(csv_file_path, index=False)