# Subjects:
# Math
# Python
# SQL

# Details:
# name : Aditya
# age : 19


# def student_info(*Subjects, **Details):
#     print("Subjects:")
#     for subject in Subjects:
#         print(subject)

#     print("\nDetails:")
#     for key, value in Details.items():
#         print(key, ":", value)

# student_info("Math",
#                  "Python",
#                  "SQL",
                 
#                  name = "Aditya",
#                  age = 19)



# CHALLANGE 1
def maximum(a,b):
    if a > b:
        print("a")

    else:
        print("b")

maximum(2,3)


# CHALLANGE 2
def is_even(a):
    if a % 2 == 0:
        print("True")

    else:
        print("Fale")

is_even(3)


# CHALLANGE 3

a = 10
b = 20
c = 30
def sum(*numbers):
    for number in numbers:
        sum = a+b+c/number
        
sum(10, 20, 30)


# CHALLANGE 4
def students(**details):
    for key, value in details.items():
        print(key, ":", value )

students(
    name="Aditya",
    age=19,
    city="Delhi"
)



# CHALLANGE 5

def calculator(a, b, operation="+"):
    if operation == "+":
        print("Addition")

    if operation == "-":
        print("Subtraction")

    if operation == "*":
        print("Multiplicaion")

    if operation == "/":
        print("Disvision")

calculator (2,3 ,operation ="-")

    