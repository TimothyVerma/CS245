"""
a program that performs file processing activities using the OS library in order to validate that 
a directory exists before creating a file in that directory.
It will prompt the user for the directory they would like to save the file in 
as well as the name of the file.  It then prompts the user for their 
name, address, and phone number and writes this data to a comma separated line 
in a file and stores the file in the directory specified by the user. 

Created on Fri May 15 18:06:46 2020

@author: Timothy
"""
import os

def make_file():      
    while True:
    ##Loop so if they directory doesn't exist it asks again    
        
        dirName = input('Directory name:')
        
        if os.path.isdir(dirName) == True:
        ## Makes sure the directory exists
            os.chdir(dirName)
            ## Changes the working directory so the file can be saved proplery
            
            while True:
            ##Loop so if the file already exists is asks again
                    
                fileName = input('File name:')
                
                if os.path.isfile(fileName) == False:
                ##If the file is new, it calls the wite_to_file function
                    
                    write_to_file(fileName)
                    
                    print ('A file named',fileName,'was created in directory', dirName)
                    break
                    
                    ## Print's the file name and directory for the user
                
                else:
                ## If the file already exists, it lets the user know and then the loop starts again
                    
                    print ('A file named',fileName,'already exists.')
            break
            #This program breaks the loop after making one file
        
        else:
        ##Lets the user know if they directory is malformed and then loops back
            print ("Diretory not found.")
        
    
def write_to_file(filePath):
    
    while True:
    ##loop so the user can change the data if there was an error
        
        userName = input(str('What Name:'))
        userAddress = input(str('What Address:'))
        userPhn = input(str('What Phone Number:'))
        ##asks User for information
        
        data = userName + ',' + userAddress + ',' + userPhn
        ##combines the three to make a single string
        
        print ('\nYou entered "' + data + '." Is that all correct?')
        
        response = input('(Y)es:').lower()
        
        if response[0] == 'y':
        ## Simplified code, only looks at the first letter of the response
            
            file = open(filePath , mode = 'w')
            #Opens a new file in write mode
            
            file.write(data)
            file.close()
            ##writes the data and closes the file to be safe
            
            break
            ##This program only writes to the file once

if __name__ == '__main__':
    make_file()  