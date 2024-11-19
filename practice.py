class Acount_managment:
    def __init__(self,balance,acount_no):
        self.balance = balance
        self.acount_no = acount_no
        while True:
            print("""----your acount details----
                    01. Enter 1 for chack acount number.
                    02. Enter 2 for chack balance.
                    03. Enter 3 for credit amount.
                    04. Enter 4 for debit amount.
                    05. Enter 5 for Exit.""")
            choise = int(input("Enter your choise:"))
            
            if choise == 1:
                self.show_acount_no()
            elif choise == 2:
                self.show_balance()
            elif choise == 3:
                amount = int(input("Enter your amount:"))
                self.credit_amount(amount)
            elif choise == 4:
                amount2 = int(input("Enter your amount:"))
                self.debit_amount(amount2)
            elif choise == 5:
                break
    
    def show_acount_no(self):
        print(self.acount_no)

    def show_balance(self):
        print(self.total)
        
    def credit_amount(self,amount):
        self.amount = amount
        self.total = self.amount + self.balance
        print(f"Your amount {self.amount} credited successfuly and your total amount is {self.total}....")

    def debit_amount(self,amount2):
        self.amount2 = amount2
        self.total2 = self.amount2 - self.balance
        print(f"Your amount {self.amount2} debited successfuly")


acount_detail = Acount_managment(10000,123456789)


