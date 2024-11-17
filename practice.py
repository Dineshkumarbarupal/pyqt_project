# class Acount:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no

#         print("""
#               1.For chack total balance.
#               2.chack your account no.
#               3.credit amount.
#               4.debit amount.
#               """
#               )
#         while True:
#             choise = int(input("Enter your choise:"))
#             sum = 0  
            
#             # try:
#             #     for num in total:
#             #         sum + num
#             #         print(f"The total balance is {sum}")
#             # except Exception as e:
#             #     print("an error...")
#             if choise == 1:
#                 print(f"Your total balance is {self.balance}")
#             elif choise == 2:
#                 print(f"your account no.{account_no}")
#             elif choise == 3:
#                 amo = int(input("Enter your amount which you want to credit:"))
#                 if amo > 0:
#                     self.balance += amo

#                 # amount = amo
#                 # total = self.balance + amount

#                 print(f"Total balance is = {self.balance}: ")
#             elif choise == 4:
#                 amount = int(input("Enter amount wich you want to debit:"))

#                 if amount > 0:
#                     self.balance -= amount
#                 print(f"Your total amount is = {self.balance}")
#             else:
#                 break

#             # def debit(self,amount2):
#             #     self.amount2 = amount2
#             #     self.total2 = self.total - self.amount2
#             #     print(f"Total balance is = {self.total2}:")


# acc1  = Acount(10000, 112233445566)



# class Student:
#     name = "vihaan"
#     def __init__(self,name ):
#         # self.name = name
#         print("hello this is a cunstructor...")

# stu1 = Student("dinesh")
# print(stu1.name)

class cars:
    name = "bmw"
    def __init__(self, name):
        self.name= name

car1 = cars("marcidies")
print(car1.name)
car2 = cars("lemborgini")
print(car2.name)



