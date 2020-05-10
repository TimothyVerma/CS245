'''
A banking program.

This program created two Bank Accounts, one checking account and one
savings account.

it allows the user to do sevear actions with these accounts,
some actions are for any bank account, others are for only one type.
'''

number_of_accounts = 0


def main():
    line_break()
    print('Welcome')
    make_account_loop ()


class BankAccount:
#definition of Parent class, BankAccount

    def __init__( self , account_number , balance ):
        
        line_break()
        print('Account number', account_number ,  'has been created.')

        self.account_number = account_number
        self.balance = balance
        self.get_balance()


    def withdraw( self , ammount ):
        self.balance = self.balance - ammount

    def deposit ( self , ammount ):
        self.balance = self.balance + ammount

    def get_balance ( self ):

        print ('Account number', self.account_number, 'contains $' + str(self.balance) +'.')


class CheckingAccount ( BankAccount ):
#definintion of child class, CheckingAccount

    def __init__ ( self , account_number , balance , fee , minimum_balance):

        BankAccount.__init__( self , account_number , balance )
        line_break()

        print('Account number', account_number ,  'is a checking account.')

        self.fee = fee
        self.minimum_balance = minimum_balance
        self.check_minimum_balance()

    def deduct_fee (self):
        print ('Deducing fee...')

        self.balance = self.balance - self.fee
        self.get_balance()

    def check_minimum_balance ( self ):
        print ('Checking mimimum balance...')

        if self.balance < self.minimum_balance:
            print('The balance for account' , self.account_number ,' is too low')
            self.deduct_fee()
        else:
            print('The balance for account' , self.account_number ,' is fine')


class SavingsAccount( BankAccount ):
#defintion of child class, SavingsAccount

    def __init__( self , account_number , balance , interest_rate ):

         BankAccount.__init__( self , account_number , balance )
         line_break()
         
         self.interest_rate = interest_rate


    def add_interest ( self ):
        print ('Calculating interest...')
        interest = self.balance * self.interest_rate
        print('Account number' , self.account_number , 'has gained $' + str(interest) +'.')
        self.balance = self.balance + interest


def make_account_loop():    
    
    line_break()
    
    print("Let's create a bank account:")
    
    while(True):
        
        print('What kind of account do you want to create??')
        answer = input('1)Savings\n2)Checking\n3)Exit\n:: ')
        
        if int(answer) == 1:
            1
            balance = initial_deposit()
            interest_rate = float(input("What's the interest rate (in percent)?\n:: "))
            
            
            SavingsAccount ( number_of_accounts , balance , interest_rate )
        
        elif int(answer) == 2:
            
            balance = initial_deposit()     
            fee = float(input("What's the fee?\n:: $"))
            minimum_balance = float(input("What's the minimum balance?\n:: $"))            
        
            CheckingAccount ( number_of_accounts , balance , fee , minimum_balance )
        
        elif int(answer) == 3:
            
            break
        
        else:
            print ("Sorry, I didn't understand that. Please enter a number listed")

        
def initial_deposit():
    
    global number_of_accounts
    
    number_of_accounts += 1
    return int(input('how much do you you want to diposit?\n:: $'))

def line_break():
    
    print ('='*45)

main()      