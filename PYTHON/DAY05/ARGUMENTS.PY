# ==============================
# PYTHON FUNCTIONS CHEAT SHEET
# ==============================


# ------------------------------
# 1. RETURN
# ------------------------------

# return sends a value back to where the function was called.

def add(a, b):
    return a + b

result = add(5, 7)
print(result)          # 12


# Difference between print() and return()

def demo1():
    print("Hello")

x = demo1()

# Output:
# Hello
# None


def demo2():
    return "Hello"

x = demo2()

print(x)

# Output:
# Hello


# Returning multiple values

def calculate(a, b):
    return a + b, a * b

sum_result, product_result = calculate(3, 4)

print(sum_result)      # 7
print(product_result)  # 12


# ------------------------------
# 2. DEFAULT ARGUMENTS
# ------------------------------

# Used when no value is passed.

def greet(name="Guest"):
    print("Hello", name)

greet()            # Hello Guest
greet("Aditya")    # Hello Aditya


# Multiple default arguments

def info(name="Guest", city="Delhi"):
    print(name, city)

info()                 # Guest Delhi
info("Eddy")           # Eddy Delhi
info(city="Mumbai")    # Guest Mumbai


# Rule:
# Required parameters FIRST
# Default parameters LAST

# Correct

def add(a, b=5):
    return a + b


# Correct

def add(a=5, b=10):
    return a + b


# Wrong

# def add(a=5, b):
#     pass


# ------------------------------
# 3. KEYWORD ARGUMENTS
# ------------------------------

# Pass values using parameter names.

def student(name, age):
    print(name, age)

student(age=19, name="Aditya")

# Output:
# Aditya 19


# Order does NOT matter.

student(name="Eddy", age=20)


# Mixing positional and keyword arguments

student("Aditya", age=19)

# Correct


# Wrong

# student(name="Aditya", 19)

# Rule:
# Positional -> Keyword  ✅
# Keyword -> Positional  ❌


# ------------------------------
# QUICK SUMMARY
# ------------------------------

# return
# -> Gives a value back.

# print
# -> Only displays the value.

# Default Argument
# -> Used if no value is provided.

# Keyword Argument
# -> Specify parameter name while calling function.

# Order Rules

# Positional Positional        ✅
# Positional Keyword           ✅
# Keyword Keyword              ✅
# Keyword Positional           ❌

# Default Rules

# Required Required            ✅
# Required Default             ✅
# Default Default              ✅
# Default Required             ❌