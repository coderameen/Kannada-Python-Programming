
'''
Think of it like using a washing machine – you don't need to know how the motor works; you just press a few buttons, and it does the job.
'''

from abc import ABC, abstractmethod

# Abstract class
class ATM(ABC):
    
    @abstractmethod
    def pressing_for_withdraw(self):
        pass

    @abstractmethod
    def pressing_for_check_balance(self):
        pass

# Child class that implements the abstract methods
class MyBankATM(ATM):
    
    def pressing_for_withdraw(self):
        print("Cash withdrawn successfully.")
    
    def pressing_for_check_balance(self):
        print("Your balance is ₹10,000.")

# Using the class
user1 = MyBankATM()
user1.pressing_for_withdraw()
user1.pressing_for_check_balance()
