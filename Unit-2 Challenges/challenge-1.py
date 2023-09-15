class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance = 0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
      if amount > 0:
        self.__account_balance += amount
        print("Deposited ₹{}. New balance: ₹{}".format(amount,self.__account_balance))

      else:
       print("Invalid deposit amount. please deposit a positive amount.")
    

    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("withdraw ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print("Account balance for {} (Account #{}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
        return self.__account_balance

#instance of bank account
my_account =BankAccount(account_number="********5432",account_holder_name= "david",initial_balance= 1000)

#testing functionality

my_account.deposit(500)
my_account.withdraw(200)
my_account.display_balance()
my_account.withdraw(1500) 

# Display the account balance
balance = my_account.display_balance()
print(f"The current balance is: {balance}")