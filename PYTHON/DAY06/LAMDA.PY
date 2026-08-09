#  Python Cheat Sheet - Lambda 
map() | filter() | sorted()  
  # Lambda  

    # Examples ```
square = lambda x: x * x 
double = lambda x: x * 2 
multiply = lambda a, b: a * b 
maximum = lambda a, b: a if a > b else b 
difference = lambda a, b: abs(a - b) 

# map()  
#  Purpose Apply the SAME operation to EVERY element. 
#  Syntax 
# python map(function, iterable) 

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers)) 
print(result) 
[2, 4, 6, 8] 

list(map(lambda x: x*x, numbers)) 
list(map(str, numbers)) 

 ## filter() 
 #  Purpose Keep ONLY elements that satisfy a condition. 
 #  Syntax ```python filter(function, iterable)   Function must return: python True False    
 # Example 
numbers = [1,2,3,4,5,6]
result = list(filter(lambda x: x % 2 == 0, numbers)) 
print(result) # [2,4,6]


list(filter(lambda x: x > 10, numbers)) 
list(filter(lambda x: x < 0, numbers))

# sorted()
#  Purpose Sort data.  
# # Syntax ```python sorted(iterable)  sorted(iterable, reverse=True)  sorted(iterable, key=function) 
# 
numbers = [4,1,3,2] 
print(sorted(numbers)) # [1,2,3,4] `

sorted(numbers, reverse=True)

# sorted() using lambda  
students = [     ("Aditya",19),     ("Rahul",18),     ("Aman",21) ]  
result = sorted(students, key=lambda x: x[1])  
print(result)  # [('Rahul',18), ('Aditya',19), ('Aman',21)]
# ```  Explanation  ``` x = ("Aditya",19)  x[0] → Name  x[1] → Age ```  ---  

# Difference  | Function | Purpose 
# lambda | Short function | 
# | map() | Modify every element | 
# | filter() | Keep selected elements | 
# | sorted() | Arrange elements |  --- 
# 
#  # Memory Trick  Lambda → Small One-Line Function
#   map() → Modify Everything  filter() → Keep Some
#   sorted() → Arrange Everything  --
# 
# -  # Interview Rule  Need to MODIFY every element? → map() 
#  Need to KEEP only some elements? → filter() 
#  Need to ARRANGE data? → sorted()