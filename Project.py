'''
This is a program to get the weather form openweathermap.org 
It allows the user to check the weather for multiple locations
It checks if the location is valid and notifies the user
It uses try blocks to detect connection errors and notifies the user 

Author: 
Timothy

commited to git on: May 16 2020 

Edited: May 19 2020
Api integreation started
'''
import requests
data_source = '&appid=5b12de548d5e384e2d222a3104b2c661'
##api key for openweathermap.org
    
def weather_check():
## Asks the user for input and will gets weather info from openweathermap.org when finished
    
    while (True):
    ## Using a loop so you user can querie the weather for multiple cities

        print("What zipcode or city name", end = '')
        
        location = input (':: ')
   
        if location.lower == 'exit' or location.lower() == 'end' or location == 'e':
        
            break
        
        else:
            try:
        
                query_api( location )
            
            except Exception as e:
                print (e)
        print('='*30)

            
def check_conecction( location ):           
    global data_source
    
    ### A dicttionary of locations
    locations = {
    '68005' : 'Bellevue',
    '90210' : 'Beverly Hills',
    }
    
    ##will check if location is valid, currenly only checkis if it is Bellevue
    try: 
        if location.title() in locations.values():
        
            return location.title()
        
        elif location in locations:
            
            return locations[location]
    
    except:
        pass
    
    print ("Sorry, the location entered couldn't be proccessed")
    raise ValueError


def  query_api( location ):
    global data_source
    
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    query = weather_url + location + "&units=imperial" + data_source
    #print (query)  ##for debugging, make sure the url is valid 
    data = requests.post(query)
    if data.status_code == 200:

        data_dict = (data.json())
        loc = data_dict['name']
        temp_dict = data_dict['main']
        temp = str(temp_dict['temp'])
        print ('It is ' + temp + '°f in ' + loc)
        
    else:
        print ('Sorry, there is no weather data for ' + location)

if __name__ == '__main__':
        
    weather_check()