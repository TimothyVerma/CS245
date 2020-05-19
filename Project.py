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

            
def check_location( location ):           
    
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
    
    data_source = "5b12de548d5e384e2d222a3104b2c661"
    ##api key for openweathermap.org
    
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    data_source = '&appid=5b12de548d5e384e2d222a3104b2c661'
    query = weather_url + location + data_source
    data = requests.post(query)
    data_dic = (data.json())
    loc = data_dic['name']
    descrition = data_dic['weather']
    weather = (descrition[0]['description'])
    print (loc , "has a" , weather ,)
    

if __name__ == '__main__':
        
    weather_check()