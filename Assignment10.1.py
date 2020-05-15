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
    #dirName = 'C:\\Users\\Timothy\\Documents\\Programing\\CS245.Python\\log'
    
    while True:
        
        dirName = input('Directory name:')
        
        if os.path.isdir(dirName) == True:
            
            while True:
                    
                fileName = input('File name:')
                
                filePath = dirName + '\\' + fileName + '.txt'
                
                
                if os.path.isfile(filePath) == False:
            
                    write_to_file(filePath)
                    print ('A file named',fileName,'was created in directory', dirName)
                    break
                
                else:
                    
                    print ('A file named',filePath,'already exists.')
            break
        
        else:
            print ("Diretory not found.")
        
    
def write_to_file(filePath):
    
    while True:
            
        userName = input(str('Name:'))
        userAddress = input(str('Address:'))
        userPhn = input(str('Phone Number:'))
        
        data = userName + ',' + userAddress + ',' + userPhn
        
        print ('\nYou entered "' + data + '." Is that all correct?')
        
        response = input('(Y)es:').lower()
        
        if response[0] == 'y':
        
            file = open(filePath , mode = 'w')    
        
            file.write(data)
            file.close()
            
            break

if __name__ == '__main__':
    make_file()  