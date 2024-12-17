class Atm:
    def __init__(self):
        self.balance = 0
        self.__pin = 9999

    def verify(self):
        pas = int(input('enter the four digit passcode: \t'))
        if pas == __self.pin:
            return True
        else:
            print(' Wrong passcode, Try again...')
            return self.verify()
            
    def withdraw(self):
        amount = int(input('enter the amount to withdraw: \t'))
        if amount > self.balance:
            print('insufficient balance')
        else:
            self.balance = self.balance - amount
            print('please wait')
            print('collect cash')
            print('Thank you')
    def deposit(self):
        amount = int(input('enter the amount to deposit: \t'))
        self.balance = self.balance + amount
    def balance_enquiry(self):
        print(self.balance)
def atm_interface():
    a1 = Atm()
    print("welcome harsha atm")
    print("Insert a card")
    card_insert = input("type yes to insert card:\t")
    if card_insert == 'yes':
        if a1.verify():
            while True:
                print("select the option")
                print('1- withdraw')
                print('2-deposit')
                print('3-balance enquiry')
                print('4-exit')
                opt = int(input('select any option\n'))
                if opt == 1:
                    a1.withdraw()
                elif opt == 2:
                    a1.deposit()
                elif opt == 3:
                    a1.balance_enquiry()
                elif opt == 4:
                    break;
                else:
                    print('invalid option')
    else:
        print('try again')

atm_interface()