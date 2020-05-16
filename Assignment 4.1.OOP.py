company = 'spam'
cost = 0.87 #per foot
length = 1 #in feet
price = 3 #in dollars
rcpt = "eggs" # used to change price into a string

def main():
    welcome()
    ask()
    ask2()
    tell()

#welcomes the user
def welcome():    
    
    print ('\n\n\nWelcome!\n')
    
    
#changes the company name based on user input
def ask():    
    
    global company
    
    print ( 'Please enter your company name.' )

    company = input ( '>>> ' )

#changes the length based on user input
def ask2():     
    
    global length
    
    print ( '\nHow many feet of fiber optic cable do you need?' )

    length = int ( input ( '>>> ' ))

#changes the price based on the new length
def calculate():     
    
    global price
    
    if length > 250: #biggest discount

        cost = 0.70    

    elif length >100: #discount

        cost = 0.80

    else: #standard price

        'null'
        
    price = length * cost

#tells the user the data
def tell():    
    
    calculate() 
    
    rcpt = str ( price )
    
    print ('\nOK ' + company + '.\n\nThat will be $' + rcpt)
    
main()