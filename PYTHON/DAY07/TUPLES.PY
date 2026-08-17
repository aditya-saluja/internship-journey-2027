# student = ("aditya", 19, "delhi")


# print(student  [0:3:2])


# numbers = (10, 20, 10, 30, 10)


# aadi = numbers.count(10) 
# saluja = numbers.index(30)

# print(aadi)
# print(saluja)


# students = ("Aditya", 19, "Delhi")

# name, age, state = students

# print(students)





# numbers = {2, 4, 6, 8}

# numbers.add(10)

# print(numbers)


# numbers = {2, 4, 6, 8}
# numbers.remove(100)
# print(numbers)

# numbers = {2, 4, 6, 8}
# numbers.discard(100)
# print(numbers)



# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}


# print(a.union(b))
# print(a.intersection(b))


# student = {
#     "name": "Aditya",
#     "age": 19,
#     "course": "CSE"
# }

# student["city"] = "delhi"
# student["age"] = 20

# print(student)
# print(student.get("name"))
# print(student.get("age"))
# print(student.keys())
# print(student.values())
# print(student.get("keys", "values"))



student = {
    "name": "Aditya",
    "age": 19
}

student.update({"city" : "delhi"})
student.update({"course" : "cse"})
student.update({"phone" : "not available"})

student.setdefault("name", "rahul")


print(student)