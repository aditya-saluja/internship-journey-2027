# CALCULATOR

operator = input("enter any value (+ - * /):")

num1 = float(input("enter a num: "))
num2 = float(input("enter a num: "))


if operator == "+":
    result = num1 + num2
    print (round(result))

elif operator == "-":
    result = num1 - num2
    print (round(result))

elif operator == "*":
    result = num1 * num2
    print (round(result))

elif operator == "/":
    result = num1 / num2
    print (round(result, 2))


else:
    print(f"{operator} is not valid")