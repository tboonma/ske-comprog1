import random


class Bank_Account:
    def __init__(self, acc_id, name, balance):
        self.__id = acc_id
        self.__name = name
        self.__balance = balance

    def get_id(self):
        return self.__id

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def __str__(self):
        return "{}:['{}', {}]".format(self.__id, self.__name, self.__balance)


def find_account(id, bank_account_DB):
    for account in bank_account_DB:
        if account.get_id() == id:
            return account
    print('Record not found.')
    return False


bank_account_DB = []
for i in range(10):
    account_ID = str(random.randint(1000, 9999))
    account_name = 'account' + str(i)
    balance = random.randint(20, 2000)
    bank_account_DB.append(Bank_Account(account_ID, account_name, balance))

# main loop to run our banking system
while True:
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to deposit amount')
    print('Press 4 to withdraw amount')
    print('Press 0 to exit')
    choice = input('Enter a choice (0-4): ')
    if choice == '1':
        for account in bank_account_DB:
            print(account)
    elif choice == '2':
        search_account = input('Enter an account number to search: ')
        account = find_account(search_account, bank_account_DB)
        if account:
            print(account)
    elif choice == '3':
        deposit_account = input('Enter an account number to deposit: ')
        deposit_amount = float(input('Enter an amount to deposit: '))
        account = find_account(deposit_account, bank_account_DB)
        if account:
            account.deposit(deposit_amount)
    elif choice == '4':
        withdraw_account = input('Enter an account number to withdraw: ')
        withdraw_amount = float(input('Enter an amount to withdraw: '))
        account = find_account(withdraw_account, bank_account_DB)
        if account:
            account.withdraw(withdraw_amount)
    elif choice == '0':
        break
    else:
        print('Invalid choice selection. Please try again')
