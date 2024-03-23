import os

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, balance, phone):
        if account_number not in self.accounts:
            self.accounts[account_number] = {'name': name, 'balance': balance ,'Phone': phone }
            print(f"Account {account_number} created successfully.")
        else:
            print(f"Account {account_number} already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited ${amount} into account {account_number}.")
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew ${amount} from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print(f"Account {account_number} does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance in account {account_number}: ${self.accounts[account_number]['balance']}.")
        else:
            print(f"Account {account_number} does not exist.")

    def display_accounts(self):
        print("Account List:")
        for acc_num, details in self.accounts.items():
            print(f"Account {acc_num}: {details['name']}, Balance: ${details['balance']}, phone: {details['phone']}")

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} closed successfully.")
        else:
            print(f"Account {account_number} does not exist.")

    def modify_account(self, account_number, new_name, new_phone):
        if account_number in self.accounts:
            self.accounts[account_number]['name'] = new_name
            self.accounts[account_number]['phone'] = new_phone
            print(f"Account {account_number} modified successfully.")
        else:
            print(f"Account {account_number} does not exist.")

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBank Management System:")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display Account List")
        print("6. Close Account")
        print("7. Modify Account")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            balance = float(input("Enter initial balance: "))
            phone = int(input("Enter the phone no:+1"))
            bank.create_account(account_number, name, balance, phone)

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)

        elif choice == '5':
            bank.display_accounts()

        elif choice == '6':
            account_number = input("Enter account number to close: ")
            bank.close_account(account_number)

        elif choice == '7':
            account_number = input("Enter account number to modify: ")
            new_name = input("Enter new account holder's name: ")
            new_phone = input("Enter new account phone no: ")
            bank.modify_account(account_number, new_name, new_phone)

        elif choice == '8':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
