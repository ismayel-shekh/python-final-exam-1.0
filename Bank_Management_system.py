# admin user name = admin
# Admin password = admin
import random
class Admin:
    def __init__(self) -> None:
        self.users = []
        self.admin = None
        self.bank_balance = 50000
        self.loan_balance = 0
        self.loan_feature = None
    def find_acount(self,user_name, password):
        for user in self.users:
            if user.name == user_name and user.password == password:
                print(f'\n-------user found------\n')
                return user
                break
            else:
                print('\n\n-------------------!!')
    def show_all_user(self):
        for user in self.users:
            print(f'account name : {user.name}\naccount number:{user.account_number}')
    def create_user_account(self,name,email,address,account_type,password):
        user = User(name,email,address,account_type,password)
        self.users.append(user)
        print('succesfully creating account!!--')

    def delete_user_acount(self,delete_name):
        user_to_remove = None
        for user in self.users:
            if user.name == delete_name:
                user_to_remove = user
                break
        if user_to_remove:
            self.users.remove(user_to_remove)
            print(f'User {delete_name} has been removed')
        else:
            print('no user found !!!')
    def available_balance(self):
        # amount = sum(User.blance for usr in self.users)

        print(f'total available amount {self.bank_balance}')

    def total_loan_amount(self):
        # loan = sum(user.loan_taken for user in self.users)
        print(f'Total loans {self.loan_balance} taka')

    def loan_taken_feature(self,acount_name,type):
        if type == 'on':
            for user in self.users:
                if user.name == acount_name:
                    user.is_loan_feature = True
                    print('take loan feature on')
        elif type == 'off':
            for user in self.users:
                if user.name == acount_name:
                    user.is_loan_feature = False
                    print('take loan feature off')


        else:
            print('write courrect input ')


class User:
    def __init__(self,name,email,address,type,password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        self.password = password
        self.account_number = None
        self.create_account_number()
        self.balance = 0
        self.loan_taken = 0
        # self.create_account_number()
        self.transction_history = []
        self.is_loan_feature = None
    
    def create_account_number(self):
        number = random.randint(1000,9999)
        # print('your account number is',number)
        self.account_number = number
    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            print(f"succesfully deposit {amount} taka")
            self.transction_history.append(f'deposit {amount} taka\n')
            return True
        else:
            print('Invalid')
            return False
    def withdrow(self,amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print('succesfully withdrow now your balance is ',self.balance)
            self.transction_history.append(f'withdrow {amount} taka\n')
            return True
        else:
            print('Withdrawal amount exceeded!!!!')
            return False
    def available_balance(self):
        print(f'Available balance {self.balance}')

    def take_loan(self,amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            print(f'succesfully taken loan {amount} taka')
            self.transction_history.append(f'Take a loan of {amount} taka\n')
            return True
        else:
            print(f'You have reached the maximum number of loans!!!!!!!')
            return False

    def transfer_balance(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            # transfer_account.balance += amount
            print(f'succesfully transfer {amount} taka')
            self.transction_history.append(f'transfer {amount} taka \n')
            return True
        else:
            print('not enough money ')
            return False
# print('----------------welcome to Python bank---------------')
current_user = None
python = Admin()

while True:
    if current_user is None:
        print('---------no user logged in!----------\n')
        print(

              "1. Login(user)\n"
              "2. Register(user)\n"
              "3. Admin login\n"
              "4. Exit"
              )
        ch = int(input('Enter option: '))

        if ch == 1:
            name = input("user name : ")
            pas = input("password : ")
            current_user = python.find_acount(name,pas)
            if current_user != None:
                print('\n\n-----------------welcome to Python bank-----------\n')
                while True:
                    print('\n\n\n'
                    '1. Show account number\n'
                    '2. Deposit\n'
                    '3. Withdraw\n'
                    '4. Available balance\n'
                    '5. Transaction history\n'
                    '6. Take a loan\n'
                    '7. Transfer amount\n'
                    '8. Exit\n'
                    )
                    op = int(input('Enter option: '))
                    if op == 1:
                        print(f'your account number is {current_user.account_number}')
                    elif op == 2:
                        am = int(input('Amount: '))
                        x = current_user.deposit(am)
                        if x ==True:
                            python.bank_balance += am
                    elif op == 3:
                        wi = int(input('Amount: '))
                        if wi >= python.bank_balance:
                            print('\n------Bankrupt---------\n')
                        else:
                            x = current_user.withdrow(wi)
                            if x ==True:
                                python.bank_balance -= wi
                    elif op == 4:
                        current_user.available_balance()
                    elif op == 5:
                        print(*current_user.transction_history)

                    elif op == 6:
                        if current_user.is_loan_feature == True:
                            am = int(input('Amount: '))
                            if am >= python.bank_balance:
                                print('\n------Bankrupt---------\n')
                            else:    
                                x = current_user.take_loan(am)
                                if x is True:
                                    python.bank_balance -= am
                                    python.loan_balance += am
                        else:
                            print('your can not take  loan ')
                    elif op == 7:
                        user_name = input('user name ')
                        for user in python.users:
                            if user.name == user_name:
                                am = int(input('Amount: '))
                                if am >= python.bank_balance:
                                    print('\n------Bankrupt---------\n')
                                else:    
                                    x =current_user.transfer_balance(am)
                                    if x == True:
                                        python.bank_balance -= am
                                    user.balance += am

                    elif op == 8:
                        current_user = None  
                        break
                    else:
                        print("Please enter a valid option!")                    

        elif ch == 2:
            na = input("name: ")
            em = input('email: ')
            ad = input('address: ')
            typ = input('type Savings or  Cuurent(sv or cr) : ')
            pas = input('password: ')
            current_user = User(na, em, ad, typ,pas)
            python.users.append(current_user)

            print('\n\n-----------------welcome to Python bank-----------\n')
            while True:
                print('\n\n\n'
                    '1. Show account number\n'
                    '2. Deposit\n'
                    '3. Withdraw\n'
                    '4. Available balance\n'
                    '5. Transaction history\n'
                    '6. Take a loan\n'
                    '7. Transfer amount\n'
                    '8. Exit\n'
                )
                op = int(input('Enter option: '))
                if op == 1:
                    # current_user.create_account_number()
                    print(f'your account number is {current_user.account_number}')

                elif op == 2:
                    am = int(input('Amount: '))
                    x = current_user.deposit(am)
                    if x ==True:
                        python.bank_balance += am
                elif op == 3:
                    wi = int(input('Amount: '))
                    if wi >= python.bank_balance:
                        print('\n------Bankrupt---------\n')
                    else:
                        x = current_user.withdrow(wi)
                        if x ==True:
                            python.bank_balance -= wi
                elif op == 4:
                    current_user.available_balance()
                elif op == 5:
                    print(*current_user.transction_history)

                elif op == 6:
                    if current_user.is_loan_feature == True or current_user.is_loan_feature == None:
                    # if current_user.is_loan_feature == True:
                    
                        am = int(input('Amount: '))
                        if am >= python.bank_balance:
                            print('\n------Bankrupt---------\n')
                        else:    
                            x = current_user.take_loan(am)
                            if x is True:
                                python.bank_balance -= am
                                python.loan_balance += am
                    else:
                        print('your can not take  loan ')
                        
                elif op == 7:
                    user_name = input('user name ')
                    for user in python.users:
                        if user.name == user_name:
                            am = int(input('Amount: '))
                            if am >= python.bank_balance:
                                print('\n------Bankrupt---------\n')
                            else:    
                                x =current_user.transfer_balance(am)
                                if x == True:
                                    python.bank_balance -= am
                                    user.balance += am
                elif op == 8:
                    current_user = None
                    break  
                    
                else:
                    print("Please enter a valid option!")
        elif ch == 3:
            admin = User("admin","admin@gmail.com","12/140-5","admin","admin")
            admin_name = input('admin user name: ')
            admin_pass = input('admin passsword: ')
            if admin.name == admin_name and admin.password == admin_pass:
                current_user = admin
                print('---------------welcome to admin panel-------------')
                while True:

                    print('\n\n\n')
                    print("1. Create account\n"
                      "2. Delete user account\n"
                      "3. See all user accounts\n"
                      "4. Bank available balance\n"
                      "5. Total loan amount\n"
                      "6. Turn on/off loan feature\n"
                      "7. Exit\n")
                    op = int(input('Enter option: '))
                    if op == 1:
                        n = input("name : ")
                        e = input('email : ')
                        d = input("address: ")
                        ty = input('type Savings or  Cuurent(sv or cr) : ')
                        pas = input('password : ')
                        python.create_user_account(n,e,d,ty,pas)
                    elif op == 2:
                        de = input('user name: ')
                        python.delete_user_acount(de)
                    elif op == 3:
                        python.show_all_user()
                    elif op == 4:
                        python.available_balance()
                    elif op == 5:
                        python.total_loan_amount()
                    elif op == 6:
                        value = input("loan feature (on or off): ")
                        acn = input('account name : ')
                        python.loan_taken_feature(acn,value)
                    elif op == 7:
                        current_user = None
                        break
                    else:
                        print("please input currect value")  
            else: 
                "you are not admin"          

        elif ch == 4:
            break
        else:
            print("Please enter a valid option!")

