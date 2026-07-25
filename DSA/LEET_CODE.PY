# PROBLEM NO. 1480
# RUNNING SUM 1D ARRAY

# numbers = [1,2,3,4]

# running_sum = 0
# new_list = []

# for number in numbers:
#     running_sum += number
#     new_list.append(running_sum)

# print(new_list)

# PROBLEM NO. 1929
# CONCETATION OF ARRAY

# numbers = [1,2,3]

# new_list = []


# for i in range(2):
#     for number in numbers:
#         new_list.append(number)
  

# print(new_list)


# 
# 

numbers = [[1,2], [2,3], [3,4]]

added_list = []
i = 0
largest = 0

for number in numbers:
    i =  sum(number)
    added_list.append(i)

    largest = added_list[0]

    for value in added_list:
        if value > largest:
            largest = value

    

print(largest)





    

    








