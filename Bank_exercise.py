
import random
database = {2056379789:['Jide', 'Oyebiyi', 'gdaybiyi@gmail.com', '12345' , 50000]}
def init():
    print('Welcome to UBI-United Bank of Iree')
    print('===================================')
    selectedOption = input('To Register, Press 1 \nTo log in to your account, press 2: \n')
    valid_selection = init_validation(selectedOption)
    if valid_selection:
        if int(selectedOption) == 1:
            register()
        elif int(selectedOption) == 2:
            login()
        else:
            print('************************')
            print('You have selected an invalid option. Please try again')
            print('************************')
            init()
    else:
        init()
        


def init_validation(number):
    if number:
        try:
            int(number)
            return True
        except ValueError:
            print('Please enter only numbers.')
            return False
    else:
        print("Please enter number(s).")
        return False
            

def GenerateAccountNumber():
    return random.randrange(1111111111, 9999999999)
    



def register():
    first_name = input('Please enter your first name: \n')
    register_validation(first_name)
    last_name = input('Please enter your last name: \n')
    register_validation(last_name)
    email = input('Please enter your email address \n')
    register_validation(email)
    password = input('Please enter a password you\'d like to use:  \n')
    register_validation(password)
    accountNumber = GenerateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password, 0]
    print('===================================')
    print('Your account number is: %s. Thank you for banking with us. %s' %(accountNumber, first_name))
    print('===================================')
    login()
    

def register_validation(field):
    if field:
        return True
    else:
        print('This is a required field')
        register()
        return False




def login():
    accountNumberUser = input('Please enter your account number: \n')
    validated_account_number = account_validation(accountNumberUser)
    if validated_account_number:
        print('===================================')
        password = input('Enter your password: \n')
        for accountNumber, userdetails in database.items():
            if accountNumber == int(accountNumberUser):
                if userdetails[3] == password:
                    bankOperations(userdetails)
                else:
                    print('Password is incorrect')
            else:
                print('Account number does not exist. ')
    else:
        init()


def account_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print('Invalid account number. Please try again.')
                return False
        else:
            print('Account number should be 10 digits.')
            return False
    else:
        print('Account number is a required field.')
        return False
       



    


def bankOperations(user):
    print('===================================')
    print('Welcome to UBI %s %s' %(user[0], user[1]))
    option = input('Please select the operation you will like to perform (1) Withdrawal (2) Deposit (3) Logout (4) Exit \n')
    validated_option = init_validation(option)
    if validated_option:
        if int(option) == 1:
            withdraw(user)
        elif int(option) == 2:
            deposit(user)
        elif int(option) == 3: 
            login()
        elif int(option) == 4:
            exit()
        else:
            print('You have entered an invalid operation %s' %user[0])
            bankOperations(user)
    else:
        bankOperations(user)



def withdraw(user):
    amount_to_withdraw = input('Please enter amount you will like to withdraw. \n')
    validated_amount = init_validation(amount_to_withdraw)
    if validated_amount:
        withdrawn_amount = int(amount_to_withdraw)
        if user[4] < withdrawn_amount:
            current_balance = user[4]
            print('Insufficient balance. Your current balance is %s. Please deposit and try again later' % current_balance)
            bankOperations(user)
        else:
            user[4] = user[4] - withdrawn_amount
            print('You have successfully withdrawn %s' % amount_to_withdraw)
            print('Your current balance is %s' % user[4])
        other_operation = int(input('Would you like to perform another operation 1. Yes 2. No \n'))
        if other_operation == 1:
            bankOperations(user)
        else: 
            print('Please take your card, %s.' % user[0])
            print('Thank you for banking with us')
            exit()
    else:
        withdraw(user)


def deposit(user):
    amount_to_deposit = input('Please enter amount to deposit: \n')
    deposited_amount = init_validation(amount_to_deposit)
    if deposited_amount:
        user[4] = user[4] + int(amount_to_deposit)
        print('You have succesfully deposited %s' % amount_to_deposit)
        print('Your current balance is %s' % user[4])
        print('=====================================')
        other_operation = int(input('Would you like to perform another operation 1. Yes 2. No \n'))
        if other_operation == 1:
            bankOperations(user)
        else: 
            print('Please take your card')
            exit()
    else:
        deposit(user)
    


init()