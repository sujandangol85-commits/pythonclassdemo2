# try:
#     with open("saroj","r") as x:
#         print(x.read())
# except FileNotFoundError:
#      print("File not found")
#
# shopping_cart = []
# for i in range(5):
#     item = input(f"{i}: input item:")
#     shopping_cart.append(item)
# try:
#     index= int(input("enter the index of your choice:"))
#     print(f"the item is {shopping_cart[index]}")
# except ValueError:
#     print("the index should be integer")
# except IndexError:
#     print("you did not enter a valid index")

class InsufficientFundError(Exception):
    def __init__(self, withdraw):
        self.withdraw=withdraw
        super().__init__(f"Insufficient balance{withdraw} your withdraw is greater than balance")
try:
    balance= 1000
    withdraw = float(input("Enter the amount you want to withdraw: "))
    if withdraw > balance:
        raise InsufficientFundError(withdraw)
    else:
        balance = balance - withdraw
        print(f"transaction successful remaining balance ={balance}")
finally:
    print("Thank you ")