class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return self.__account_balance


# Testing the BankAccount class
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 1000)
    
    print("Initial balance:", account.display_balance())
    
    if account.deposit(500):
        print("Deposit successful. New balance:", account.display_balance())
    else:
        print("Invalid deposit amount.")
    
    if account.withdraw(200):
        print("Withdrawal successful. New balance:", account.display_balance())
    else:
        print("Insufficient balance or invalid withdrawal amount.")