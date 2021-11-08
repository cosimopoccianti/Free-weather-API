# Progetto-Luiss
Python and R for Data Science

Our goal was to import data by accessing the API of a third-party service
and create a dataset with at least 1000 instances/observations

The project is " Free Weather API", and the variables selected by the teams are defined as follow:

- Time: hours for the next 7 days from the run time 
- Temperature 2m: air temperature at 2 meters above the surface
- Apparent_temperature: temperature perceived by humans, caused by the combined effects of air temperature, relative humidity and wind speed
- Relativehumidity_2m: is the concentration of water vapour present in the air 2 meters above the surface.
- Precipitation: any product of the condensation of atmospheric water vapour that falls under gravitational pull from clouds.
- Dewpoint_2m: air's temperature needs to be cooled to (at constant pressure) to achieve a relative humidity (RH) of 100%, 2 meters above the surface.
- Freezinglevel_height: the lowest altitude in the atmosphere over a given location when the air temperature reaches 0ºC.
- Pressure_msl: (MEAN SEA LEVEL PRESSURE)This is the pressure reading most commonly used by meteorologists to track weather systems at the surface. 

#-----------------------------------------------------------------------------

Let's divide our python code into sections to describe it.

In the first section, we have imported the libraries Panda, Json and Requests, created a list of Latitudes, Longitudes, and Locations within those coordinates. 
The location selected, as shown, are: Rome, Reykjavik, Jerusalem, Barcelona, Lamezia Terme, Florence, Urbania, San Martino in Pensilis, Schiavonea, Berlino','Budapest, Bruxelles, Malta, Parigi. 

    import pandas
    import json
    import requests
    
    Latitude = ['41.8955','64.1353','31.7857','41.3949','38.9429','43.7683','43.6683','41.8696', '39.6530','52.520396','47.499348','50.851822','35.881268','48.855591']
    Longitude = ['12.4823','-21.8952','35.2007','2.1756','16.3316','11.2590','12.5224','15.0110', '16.5363','13.393949','19.064350','4.351965','14.448590','2.324507']
    Location = ['Rome','Reykjavik','Jerusalem','Barcelona','Lamezia Terme','Florence','Urbania','San Martino in Pensilis', 'Schiavonea','Berlino','Budapest','Bruxelles','Malta','Parigi']

#-----------------------------------------------------------------------------

In the second section, we use a for loop (in the range of the length of the lists above) to insert Latitudes and Longitudes within the URL of the API; The result of this operation is the creation of .json files for each Location. 

    for i in range(len(Location)):
        url = 'https://api.open-meteo.com/v1/forecast?latitude='+ Latitude[i] +'&longitude='+ Longitude[i] +'&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,pressure_msl,precipitation,freezinglevel_height&timezone=Europe%2FBerlin'
        response = requests.get(url)
        file = open("Forecast_"+ Location[i] +".json", "w+")
        file.writelines(response.text)
        file.close()
    
#-----------------------------------------------------------------------------

The third part of the code is dedicated to extracting the lists of variables that we have selected from the .json files created in the previous section, within this part we also used a second for loop to link each value of the variables to an hour for the next 7 days.

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

#-----------------------------------------------------------------------------

The last section of the code is dedicated to merging and organizing all this data in a CSV file with column names. 

    csv_file_path = 'Forecast_merged.csv'
    df = pandas.DataFrame(result)
    df.columns = ['city','time','temperature','apparent temperature','relative humidity','precipitation', 'dewpoint','freeing level', 'pressure']
    df.to_csv(csv_file_path, index=False)

