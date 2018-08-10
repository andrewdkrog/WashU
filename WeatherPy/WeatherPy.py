
# Observations

The maximum temperature for August 9, 2018 had a clear parabolic relationship with the latitude of the city, peaking somewhere near 25 degrees North. The reason the peak is in the northern hemisphere is because it is summer time there. I would expect the peak 6 months from now in February would be somewhere similar in terms of latitude but in the southern hemisphere (~25 degrees South, or -25 on the chart).

Cloudiness clustered at round numbers with 0% and 90% appearing to be the most common values. There does not seem to be any obvious relationship between latitude and cloudiness among the cities randomly selected for this day.

Most cities had average wind speeds under 5 mph, although there was a considerable amount of variability. The highest wind speed for a city was close to 35 mph. Similar to cloudiness, there does not appear to be an easily observable relationship with wind speed and latitude for this day in August.

# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import openweathermapy.core as owm
import json
import csv

# Import API key
import api_keys

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

## Generate Cities List

# List for holding lat_lngs and cities
lat_lngs = []
cities = []
latitudes = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)
        latitudes.append(lat_lng[0])

# Print the city count to confirm sufficient count
print(len(cities))

## Perform API Calls

# OpenWeatherMap API Key
api_key = api_keys.api_key
settings = {"units": "imperial", "appid": api_key}

# Starting URL for Weather Map API Call
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID="

query_url = url + api_key + "&q=" + cities[1]

# Create empty lists for today's max temp, humidity, cloudiness, & wind speed
max_temps = []
humidity = []
cloudiness = []
wind_speed = []

# create variables to track the record number within loop and the total number of cities we're looping through
record_number = 1
num_cities = len(cities)

print(f'Processing record {record_number} of {num_cities} | {cities[0]}')
print(f'{query_url}')

for city in cities:
    '''
    Loop through each city in city list to pull today's max temp from OWM API
    Create the query url using api key and city name
    Pull out max temp from JSON response and append to max temp list
    For cities that are not in OWM database, return NA
    To comply with OWM's max calls per minute, delay code .1 second each iteration
    '''
    
    # Create the url string for the query using OWM url, the API key, and the city name
    query_url = url + api_key + "&q=" + city
    
    # Use requests to query the OWM API
    weather_response = requests.get(query_url)
    
    # Format API response as JSON
    weather_json = weather_response.json()
    
    # Attempt to pull max temp, wind speed, humidity, and cloudiness from JSON response
    # If there is a value, append that value to corresponding list, if not append an NA
    try:
        max_temps.append(weather_json['main']['temp_max'])
    except:
        max_temps.append('NA')
        
    try:
        wind_speed.append(weather_json['wind']['speed'])
    except:
        wind_speed.append('NA')
        
    try:
        humidity.append(weather_json['main']['humidity'])
    except:
        humidity.append('NA')
        
    try:
        cloudiness.append(weather_json['clouds']['all'])
    except:
        cloudiness.append('NA')                
    
    # Print the record number, total number of records, city name, and query url    
    print(f'Processing record {record_number} of {num_cities} | {city}')
    print(f'{query_url}')
    
    # Add 1 to record number to keep track of where loop is
    record_number = record_number + 1
    
    # Add a .1 second delay to avoid too many requests from OWM's API
    time.sleep(.1)
    

# Create pandas dataframe of city, latitude, max temp, wind speed, humidity, and cloudiness
owm_df = pd.DataFrame({'City' : cities, 'Latitude' : latitudes, 'Max Temp' : max_temps,
                       'Wind Speed' : wind_speed, 'Humidity' : humidity, 'Cloudiness' : cloudiness})

# Drop all cities that have an NA returned for any attribute
owm_df = owm_df[owm_df['Max Temp'] != 'NA']

# Format all data except city name as float
owm_df[['Cloudiness', 'Humidity', 'Max Temp', 'Wind Speed', 'Latitude']] = owm_df[['Cloudiness', 'Humidity', 'Max Temp', 'Wind Speed', 'Latitude']].astype(float)

# Write the pandas dataframe to a csv file
owm_df.to_csv("city_weather_df")

# Plot latitude vs cloudiness using pandas plot function, clean up titles and save figure
owm_df.plot(kind = 'scatter', x = 'Latitude', y = 'Cloudiness')
plt.title('Cloudiness by Latitude (8/9/18)', size = 18)
plt.savefig('Cloudiness')
plt.ylabel('Cloudiness (%)')

# Plot latitude vs humidity using pandas plot function, clean up titles and save figure
owm_df.plot(kind = 'scatter', x = 'Latitude', y = 'Humidity')
plt.title('Humidity (%) by Latitude (8/9/18)', size = 18)
plt.savefig('Humidity')
plt.ylabel('Humidity (%)')

# Plot latitude vs wind speed using pandas plot function, clean up titles and save figure
owm_df.plot(kind = 'scatter', x = 'Latitude', y = 'Wind Speed')
plt.title('Wind Speed by Latitude (8/9/18)', size = 18)
plt.savefig('Wind_speed')
plt.ylabel('Wind Speed (mph)')

# Plot latitude vs max temp using pandas plot function, clean up titles and save figure
owm_df.plot(kind = 'scatter', x = 'Latitude', y = 'Max Temp')
plt.title('Max Temperature by Latitude (8/9/18)', size = 18)
plt.savefig('Max_Temp')
plt.ylabel('Max Temperature (F)')