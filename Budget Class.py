class Budget:
    def __init__(self, category):
        self.name = category
        self.balance = 0
        self.ledger = []



    def get_balance(self):
        print('{} have #{}'.format(self.name, self.balance))
        return self.balance
        
        
    def deposit(self):
        amount = int(input('Please enter amount you will like to deposit for {}: \n'.format(self.name)))
        self.balance += amount
        print('#{} added to {}'.format(amount, self.name))

        
    def withdraw(self):
        amount = int(input('Please enter amount you would like to withdraw from {}: \n'.format(self.name)))
        if self.balance >= amount:
            if amount >=1000:
                self.balance -= amount
                print('You have withdrawn #{} from {}'.format(amount, self.name))
            else:
                print('Please withdraw an amount greater than #1000.')
        else:
                print('Insufficient fund. Please deposit and try again')

    
    def get_options(self):
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Get balance')
        selected_option = int(input('Please select an option. \n'))

        while True:
            if selected_option == 1:
                self.deposit()               
                break
            elif selected_option == 2:
                self.withdraw()
                break
            elif selected_option == 3:
                self.get_balance()
                break
            else:
                print('You have seleceted an invalid option. Please try again')
                selected_option = int(input('Please select an option. \n'))
                continue

    def transfer(self):
        while True:
            print('Please select a category: ')
            print('1. Food')
            print('2. Clothing')
            print('3. Entertainment')
            category = int(input('Please enter a category to transfer to: \n'))
            if category == 1:
                amount = int(input('Please input amount to transfer to Food wallet'))
                print('{} has been transferred to food wallet'.format(amount))
                
                break
            elif category == 2:
                amount = int(input('Please input amount to transfer to Clothe wallet'))
                print('{} has been transferred to food wallet'.format(amount))
                self.end()
                break
            elif category == 3:
                amount = int(input('Please input amount to transfer to Entertainment wallet'))
                print('{} has been transferred to food wallet'.format(amount))
                
                break
            else:
                print('You have selected an invalid option.')
                amount = int(input('Please input amount to transfer to Clothe wallet'))
                continue


        
        

cloth = Budget('Clothes') 
food = Budget('Food')
entertainment = Budget('Entertainment')

