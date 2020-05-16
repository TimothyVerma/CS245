'''
Assignment 7.1
Create a program that includes a dictionary of stocks. 
Your dictionary should include at least 10 ticker symbols.
The key should be the stock ticker symbol and the value should be the current 
price of the stock (the values can be fictional).
Ask the user to enter a ticker symbol.  
Your program will search the dictionary for the ticker symbol and then 
print the ticker symbol and the stock price.  
If the ticker symbol isn’t located print a message indicating that the 
ticker symbol wasn’t found.
'''

stocks = {
    ## The stock prices can be fictional so I set them to 1 - 12 to make debugging quicker
    
    'AAPL':1,
    'GOOG':2,
    'HOG':3,
    'MSFT':4,
    'FB':5,
    'NFLX':6,
    'AMZN':7,
    'SNE':8,##Sony
    'TWTR':9,
    'F':10,##Ford
    'WMT':11,
    'T':12 ##AT&T
    }

while(True):
    
    print ('Please enter a NYSE stock symbol')
    Ticker_Symbol = input('>>>')
    
    
    if upper(Ticker_Symbol) in stocks.keys():
    
        print ("The current price of",Ticker_Symbol,'is',(stocks[Ticker_Symbol]))
    
    elif Ticker_Symbol == 'exit'or Ticker_Symbol == 'end':
        
        break
  
    else:
        
        print ('Sorry I do not recongize',Ticker_Symbol)