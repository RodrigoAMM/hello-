balance=5000

pin=int(input("Enter your pin"))
while(pin!=2036):
    pin=int(input("Enter your pin"))

print("Your balance is $"+str(balance))

choice=int(input("To withdraw, enter -, to deposit enter+, and 0 to stop"))
balance=5000

while(choice!=0):
    choice=int(input("To withdraw, enter -, to deposit enter+, and 0 to stop"))
    balance=balance+choice
    print("New balance is $"+str(balance))
print("Have a good day")
