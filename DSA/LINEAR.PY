# LINEAR SEARCH
# CHECK THE NUMBER PRESENT IN LIST 

# numbers = [1, 2, 3, 4, 5]

# found = False

# user = int(input("whats your number nigga: "))

# for number in numbers:
#     if user == number:
#         found = True
#         break


# if found:
#     print("yes")

# if not found:
#     print("nooo")



# IS AN ARRAY SORTED 
# numbers = [1,2,3,4,5]

# sorted_array = True

# for i in range (len(numbers) -1):
#     if numbers [i] > numbers [i + 1]:
#         sorted_array = False
#         break

# if sorted_array:
#     print("sorted")

# else:
#     print("nooo")


# RUNNING SUM 
# numbers = [1,2,3,4]

# running_sum = 0
# result = []

# for number in numbers:
#     running_sum += number
#     result.append(running_sum)


# print(result)


# SORT ALL 0 AT END

# numbers = [1,0,3,0,12]


# result = []
# zero_count = 0


# for number in numbers:
#     if number != 0:
#         result.append(number)

#     else:
#         zero_count += 1

# for i in range(zero_count):
#     result.append(0)

# print(result)


# REVERSE AN ARRAY


# numbers = [1,2,3,4,5]

# new_list = []

# for i in range  (1, len(numbers)+ 1):
#     new_list.append(numbers[-i])

# print(new_list)


# REMOVE DUPLICATES 

# numbers = [1,2,2,3,4,5,5]

# new_list = []

# for number in numbers:
#     if number not in new_list:
#         new_list.append(number)

# print(new_list)

# ROTATE JUST ONE NUMBER

numbers = [1,2,3,4,5]

new_list = []

new_list.append(numbers [-1])

for i in range (len(numbers) -1):
    new_list.append(numbers [i])


print(new_list)



    