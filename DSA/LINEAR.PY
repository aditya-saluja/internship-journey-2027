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

# numbers = [1,2,3,4,5]

# new_list = []

# new_list.append(numbers [-1])

# for i in range (len(numbers) -1):
#     new_list.append(numbers [i])


# print(new_list)

# REVERSE ARRAY BY MODYFYING SAME ONE 


# numbers = [1,2,3,4,5]
# left = 0
# right = (len(numbers)-1)

# while left < right:
#     numbers[left], numbers[right] = numbers[right], numbers[left]
#     left += 1
#     right -= 1

# print(numbers)


# ADD BOTH ARRAY IN LIST 

# arr1 = [1,3,5]
# arr2 = [2,4,6]

# result = []

# i = 0
# j = 0

# while i < j:
#         i.append(result)



# print(result)


# BRUTE FORCE

# numbers = [1,2,3]

# result = 4

# found = False


# for i in range (len(numbers)):
#     for j in range (i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == result:
#             print([i,j])
#             found = True
#             break

    
#         if found:
#             break


# TWO POINTER PROBLEM 

# numbers = [1,2,3,4,5]

# found = False
# result = 7
# i = 0
# j = 4

# for x in range (len(numbers)):
#     if numbers[i] + numbers[j] < result:
#         i += 1

#     if numbers[i] + numbers[j] > result:
#         j -= 1

#     if numbers[i] + numbers[j] == result:
#         break


# print(result)



    


        
        
# numbers = [1,2,3,4,5]
# result = 9
# i = 0
# j = 1
# found = False

# for x in range(len(numbers)-1):
#      if numbers[i] + numbers[j] == result:
#         found = True
#         break
#      if numbers[i] + numbers[j] != result:
#             j+= 1
#             i+= 1



    
    

# print(result)



# DUPLICATES


word = "Programming"


print (word[:7])
print (word[3:7])
print (word[7:11])
print (word[:3])
print (word[:])


