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
    dirName = input('Directory name:')
    
    if os.path.isdir(dirName) == True:
        
        fileName = input('File name:')
        
        filePath = dirName + '\\' + fileName + '.txt'
    
        if os.path.isfile(filePath) == False:
    
            write_to_file(filePath)
            print ('A file named',fileName,'was created in directory', dirName)
        
        else:
            
            print ('A file named',filePath,'already exists.')
    
    
def write_to_file(filePath):
    
    userName = input('Name:')
    userAddress = input('Address:')
    userPhn = input('Phone Number:')
    
    file = open(filePath , mode = 'w')    
    
    file.write(userName + ',' + userAddress + ',' + userPhn)


if __name__ == '__main__':
    make_file()  