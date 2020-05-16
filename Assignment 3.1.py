#variables created for testing and debugging
company = 'spam'
cost = 0.87 #per foot
length = 3 #in feet
price = 3 #in dollars
recipt = "eggs" # used to change price into a string

print ( 'Welcome\nPlease enter your company name.' )
company = input ( '>>> ' )

print ( '\nHow many feet of fiber optic cable do you need?' )

length = int ( input ( '>>> ' ))
price = length * cost
recipt = str ( price )

print ('\nOK ' + company + '.\nthat will be $' + recipt + '.' )