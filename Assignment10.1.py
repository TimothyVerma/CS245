"""
a program that performs file processing activities using the OS library in order to validate that 
a directory exists before creating a file in that directory.
It will prompt the user for the directory they would like to save the file in 
as well as the name of the file.  It then prompts the user for their 
name, address, and phone number and writes this data to a comma separated line 
in a file and stores the file in the directory specified by the user. 

after writing the program dislplays the file text for the user to verify

Created on Fri May 15 18:06:46 2020

@author: Timothy
"""
import os

def make_file():      
    while True:
    ##Loop so if they directory doesn't exist it asks again   
        
        print('In which directory should the file be saved?')
        dirName = input('Directory name:')
        ##user must specify which directory to use
        
        if os.path.isdir(dirName) == True:
        ## Makes sure the directory exists
            
            os.chdir(dirName)
            ## Changes the working directory so the file can be saved proplery
            
            while True:
            ##Loop so if the file already exists is asks again
                print('What would you like the file to be called?')    
                fileName = input('File name: ')
                
                if fileName.lower() == 'quit':
                    raise SystemExit
                    
                elif os.path.isfile(fileName) == False:
                ##If the file is new, it calls the wite_to_file function
                    
                    file = open(fileName , mode='x')
                    print ('A file named',fileName,'was created in directory', os.getcwd(),'\n')
                    ##lets the user know that the process worked (debugging)
                    file.close
                    
                    return fileName
                
                else:
                ## If the file already exists, it lets the user know and then the loop starts again
                    
                    print ('A file named',fileName,'already exists.\n')
            break
            #This program breaks the loop after making one file
        
        elif dirName.lower() == 'quit':
        ##Allows the user to quit if they decide no to make a file    

            raise SystemExit
            
        else:
        ##Lets the user know if they directory is malformed and then loops back
            print ("Diretory not found.")
        
    
def get_data(fileName):
#ask for user input, then opens and writes a file using that data    
    
    while True:
    ##loop so the user can change the data if there was an error
        
        print ('Please input your name, address, and phone number.')    
        userName = input(str('Name: '))
        userAddress = input(str('Address: '))
        userPhn = input(str('Phone Number: '))
        ##asks User for information
        
        data = userName + ',' + userAddress + ',' + userPhn
        ##combines the three to make a single string
        
        print ('\nYou entered "' + data + '." Is that all correct?')
        
        response = input('(Y)es:').lower()
        
        if response[0] == 'y':
        ## Simplified code, only looks at the first letter of the response
           
            return data     
            break
            ##This program only writes to the file once
        
        elif response.lower() == 'quit':
        ##Allows the user to quit if they decide no to make a file    
                    
            raise SystemExit
            
        

def write_file( fileName , data ):
     
     file = open(fileName , mode = 'w') 
     file.write(data) 
     file.close()
     
    
def read_file( fileName ):
##Opens a file in read mode, prints the contents, and closes the file

    file = open(fileName, mode = 'r')
    print('The file contains the following data:\n' + file.read())
    file.close
                    

if __name__ == '__main__':
    
    fileName = make_file()  
    data = get_data( fileName )
    write_file( fileName , data )
    read_file( fileName )