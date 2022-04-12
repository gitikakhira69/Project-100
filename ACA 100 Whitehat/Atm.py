class Atm(object):

    def __init__(self, name, card_no, balance):
        self.name = name
        self.card_no = card_no
        self.balance = balance

    def details(self):
        print("Account Holder Name : ", self.name.upper())
        print("Account Card Number : ", self.card_no())
        print("Available Balance : ", self.balance())

    def withdrawals(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance!!!")
        else:
            self.balance = self.balance - self.amount
            print("Current Balance : ", self.balance)

    def amount_deposited(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Balance = ", self.amount)

    def display(self):
        print("Current Balance = ", self.balance)

    def transaction(self):
        print(
            """
             ******TRANSACTION******
             1)Account Detail
             2)Withdrawal 
             3)Deposit
             4)Balance           
            """
        )
    while True:
        option = int(input("Enter 1,2,3,4,5 : "))
        if option == 1:
            print(details())
        elif option == 2:
            amount = input("Enter the amount to be withdraw : ")
            print(withdrawals(amount))
        elif option == 3:
            amount = input("Enter the amount to be deposited : ")
            print(amount_deposited(amount))
        elif option == 4:
            print(display())
        else:
            print("ERROR!!!!")
        break


atm = Atm("Gitika", 123456, 500)
