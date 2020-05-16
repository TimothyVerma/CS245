'''
This is a program to get the weather form openweathermap.org 
It allows the user to check the weather for multiple locations
It checks if the location is valid and notifies the user
It uses try blocks to detect connection errors and notifies the user 
'''

#import module from Requests Library for pulling from api key

def weather_check():
## Asks the user for input and will gets weather info from openweathermap.org when finished
    
    while (True):
    ## Using a loop so you user can querie the weather for multiple cities

        print("What zipcode or city name", end = '')

        location = input (':: ')
   
        if location.lower() == 'exit' or location.lower() == 'end' or location == 'e':
        
            break
        
        else:
            try:
        
                location = check_location( location )
                weather = query_api( location )
    
                print ("The weather in", location , "is" , weather , "\n")
            
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
    
    ##data_source = "9a4a26cb051a9f1d9653f24047e937a3"
    ##api key for http://openweathermap.org/
    
    ## I will write code that queries the api for weather info at the location 
    return 'sunny'


if __name__ == '__main__':
        
    weather_check()