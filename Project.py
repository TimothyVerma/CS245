'''
This is a program to get the weather form openweathermap.org 
It allows the user to check the weather for multiple locations

EXTRA CREDIT
Display the Clouds or Winds forecast in terms of partly, mostly cloudy, and calm, breezy, windy.

Still not perfected
Allow the user to obtain weather forecast data using their zip code and city
It checks if the location is valid and notifies the user
It uses try blocks to detect connection errors and notifies the user 


Author: 
Timothy

commited to git on: May 16 2020 

Edited: May 19 2020
Api integreation started
'''
import requests
from math import floor

data_source = '&appid=5b12de548d5e384e2d222a3104b2c661'
##api key for openweathermap.org
    
def Weather_Check():
## Asks the user for input and will gets weather info from openweathermap.org when finished
    
    while (True):
    ## Using a loop so you user can querie the weather for multiple cities

        print("Enter US zipcode or city name", end = '')
        
        location = input (':: ')
        
        if location.lower == 'exit' or location.lower() == 'end' or location == 'e':
        
            break
        
        else:
            try:
        
                Query_Api( location )
                break
            
            except Exception as e:
                print (e)
        print('='*30)

## Need to change this completely to make it a valid check for the API            
# =============================================================================
# def check_conecction( location ):           
#     global data_source
#     
#     ### A dicttionary of locations
#     locations = {
#     '68005' : 'Bellevue',
#     '90210' : 'Beverly Hills',
#     }
#     
#     ##will check if location is valid, currenly only checkis if it is Bellevue
#     try: 
#         if location.title() in locations.values():
#         
#             return location.title()
#         
#         elif location in locations:
#             
#             return locations[location]
#     
#     except:
#         pass
#     
#     print ("Sorry, the location entered couldn't be proccessed")
#     raise ValueError 
# =============================================================================

def  Query_Api( location ):
    global data_source
    
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    query = weather_url + location + "&units=imperial" + data_source
    ## makes a string that is formatted for the API, 
    ## "&units=imperial" converts the temprature and windspeed data to impreial units
    
    #print (query)  ##for debugging, make sure the url is valid 
    
    data = requests.post(query)
    if data.status_code == 200:
    ## Checks that the connection was made correctly
        
        data_dict = data.json()
        loc = data_dict['name']
        ## created a dictionary for the location provided
        
        temp = Temp(data_dict)
        wind = Wind(data_dict)
        sky = Clouds (data_dict) 
        
        print ('It is ' + temp + '°f, ' + wind + ', and ' + sky + ' in ' + loc)
        
    else:
        print ('Sorry, there is no weather data for ' + location)

def Temp(data_dict):
    temp_dict = data_dict['main']
    return str(round(temp_dict['temp']))
        
def Wind(data_dict):
    
    wind_dict = data_dict['wind']
    wind_speed = float(wind_dict['speed'])
    
    #print (wind_speed)
    ## debugging to see the raw seed
    wind_types = {        
        0 : 'calm',
        1 : 'breezy',
        2 : 'windy',
        }
    
    if wind_speed < 30:

        return wind_types[floor(wind_speed/10)]
    
    else:

        return 'overcast'
        
        
def Clouds (data_dict):
    cloud_dict = data_dict['clouds']
    cloud_cover = float(cloud_dict['all'])
    

    clouds = {        
        0 : 'clear',
        1 : 'partly cloudy',
        2 : 'mostly couldy', 
        }

    if cloud_cover < 70:
        return clouds[floor(cloud_cover/25)]

    else:

        return 'overcast'       


if __name__ == '__main__':
        
    Weather_Check()