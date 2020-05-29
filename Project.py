'''
This is a program to get the weather form openweathermap.org 
It allows the user to check the weather for multiple locations
It checks if the location is valid and notifies the user
It uses try blocks to detect connection errors and notifies the user 

EXTRA CREDIT
Display the Clouds or Winds forecast in terms of partly, mostly cloudy, and calm, breezy, windy.
Allow the user to obtain weather forecast data using their zip code and city

Known bug:
Some zipcodes appear to be slightly wrong in the database 

Author: 
Timothy

commited to git on: May 16 2020 

Edited: May 19 2020
Api integreation started

Edited May 22 2020
Edited May 23 2020
'''
import requests
from math import floor

##api key for openweathermap.org
    
def Weather_Check():
## Asks the user for input and will gets weather info from openweathermap.org when finished
    print('='*80)
    print ( 'Welcome, I will tell you the weather for cities in the US' )
    print ( "Enter US zipcode or city name or Enter exit or end when you're done." , end = '' )
    
    while (True):
    ## Using a loop so you user can check the weather for multiple cities
        
        location = input (':: ')
        
        if location.lower == 'exit' or location.lower() == 'end' or location.lower() == 'e':
            break
        
        else:
            try:
            ##Attempts to run code that will fail if connection isn't mad

                data = Connect_To_Api( location )
                ## pulls data from the API
                
                if data == 'error':
                    
                    print ('Sorry, there is no weather data for ' + location )
                    
                else:
                    Query_Api( data )
                    ##converst the data from the API into a simple sentance. 
                
                print( '='*80 )
                print ( "Enter Another location or enter exit or end if you're done." , end = '' )

                
            except:
                print ("Connection Error")
        
        
def  Connect_To_Api( location ):
## ci,

    data_source = '&appid=5b12de548d5e384e2d222a3104b2c661'

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    
    query =  weather_url + location + ",us" + "&units=imperial" + data_source
    ## string containing the location that is formatted for the API, 

    ## ',us' makes it only check US codes, otherwise Zipcodes can be misinterpereted 

    ## "&units=imperial" converts the temprature and windspeed data to impreial units
    
    data = requests.post( query )
    
    if data.status_code == 200:
    ## Checks that the connection was made correctly
        return data
    else:
        return 'error'
        
    
def Query_Api( data ):
    ## Checks that the connection if vaild, and runs funtions to format the data
        
    data_dict = data.json()
    ## created a dictionary for the location provided
    
    loc = data_dict['name']
    ##Uses a city name provided by the API, mostly for zipcode 
    ##Also useful if they user used all caps or lowercase
    
    print('Ok, finding weather data for ' + loc)
    ##lets user know their location was accepted, converts it to city name
    
    temp = Temp( data_dict )
    wind = Wind ( data_dict )
    sky = Clouds (data_dict ) 
    
    print ('It is ' + temp + '°f, ' + wind + ', and ' + sky + ' in ' + loc)
    ##prints the data in a simple sentance
   
def Temp(data_dict):
    ## Converts the temprature to string
    
    temp_dict = data_dict['main']
    return str(round(temp_dict['temp']))
        
def Wind(data_dict):
    ## converst the wind data to a simple word
    
    wind_dict = data_dict['wind']
    wind_speed = float(wind_dict['speed'])
    
    
    if wind_speed < 30:
        
        wind_types = {        
            0 : 'calm', ##if the wind is below 10mph 
            1 : 'breezy', ## if the wind is between 10 and 20 mph
            2 : 'windy', ##if the wind is between 20 and 30 mph
            }

        return wind_types[floor(wind_speed/10)]
    
    else:

        return 'gusty'
        ##if the wind is 30mph or more
        
def Clouds (data_dict):
    ## Converts the coulds data to a simple word or phrase
    
    cloud_dict = data_dict['clouds']
    cloud_cover = float(cloud_dict['all'])
    


    if cloud_cover < 70:
        
        
        clouds = {        
            0 : 'clear', ##if there is less than 25% cloud cover
            1 : 'partly cloudy', ## if there is more than 25% but less than 50%
            2 : 'mostly couldy', ## if there is more than 50 %
            }
        
        return clouds[floor(cloud_cover/25)]

    else:

        return 'overcast'       
        ## if there is more than 70% cloud cover

if __name__ == '__main__':     
    Weather_Check()