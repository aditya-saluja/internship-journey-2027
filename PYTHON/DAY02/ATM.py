# ATM MACHINE


balance = 10000

pin = int(input("enter your pin: "))

if pin == 123:
    print("your pin is correct")

    # input("check balance " \
    # " deposit money "
    # " withdraw money: ")   

else:
    print("incorrect pin") 

choices = (input("1.check balance\n 2.deposit money\n 3.withdraw money\n 4.exit: "))

if choices == "1":
    print (balance)

elif choices == "2":
    # print("enter amount to deposit money")
    more = int(input("how much you want to add: "))

    balance = balance + more
    print(balance)


elif choices == "3":
    # print("withdraw money")
    less = int(input("how much you want to withdraw: "))

    balance = balance - less
    print(balance)

elif choices == "4":
    print("exit")



