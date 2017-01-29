# import needed modules and panda shortened to pd
import requests
import pandas as pd

# make empty lists
location_list = []
temperature_list = []

# repeat process for five different places
for x in range(5):
    # build url to get lat and long from address
    url1 = 'https://maps.googleapis.com/maps/api/geocode/json'
    
    # get places from user
    input_address = input('Pick an address: ')
    # use API key and ask user to input address
    payload1 = {'key':'AIzaSyCa-VTu9dCDz8pcIHwJTdKQFLBdTS29JQk', 'address': input_address}

    # get data
    r1 = requests.get(url1, params=payload1)
    data = r1.json()

    # goes to the dictionary with latitude and longitude
    result = data['results'][0]
    location = result['geometry']['location']

    # construct parts of url for weather
    endpoint = 'https://api.darksky.net/forecast/'
    key = 'feace1a5e9e9c048dc21e7ddd2851e3c'
    
    # assign lat and long from googl
    latitude = str(location['lat'])
    longitude = str(location['lng'])
    
    # makes url for weather
    url2 = endpoint + key + '/' + latitude + ',' + longitude
    
    # send request
    r2 = requests.get(url2)
    
    # format weather
    weather = r2.json()
    
    # assign different data in dictionaries to different variables
    daily_temp_max = weather['daily']['data'][0]['temperatureMax']
    daily_temp_min = weather['daily']['data'][0]['temperatureMin']
    
    # average out the data
    tempAVG = .5 * (daily_temp_max + daily_temp_min)

    # add data to the lists
    location_list.append(input_address)
    temperature_list.append(tempAVG)

# make data frame with data
df = pd.DataFrame({
    'Location' : location_list,
    'Temperature' : temperature_list
})

# import functions from bokeh
from bokeh.charts import Bar, output_file, save

# make the bar graph
p = Bar(df, 'Location', 'Temperature', title = 'Average Temperatures in Cities')

# save file to file location
output_file('CitiesBar.html')
save(p)