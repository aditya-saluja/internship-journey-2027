# # REMOVE DUPLICATES FROM AN SORTED ARRAY 
# nums = [1,2,2,3]

# i = 0
# j = 1

# while j < len(nums) :
#     if nums [i] != nums [j]:
#         i += 1
#         nums[i] = nums[j]
#     j += 1

# print(nums)
# print(i + 1)


# # BEST TIME OF SELLING AND BUYING STOCKS
# stocks = [7,1,5,4,6,2]

# buy =  stocks [0]
# max_profit= 0


# for i in range (len(stocks) -1):
#     if stocks [i] < buy:
#         buy = stocks[i]

#     else:
#         profit = stocks[i] - buy

#         if profit >max_profit:
#             max_profit = profit


     
# print (max_profit)


# MOVE ALL ZEROS TO THE END 


# nums  = [0,1,0,5,7] 


# i = 0
# j = 1

# while j < len(nums):
#     if nums [i] == 0 and nums [j] != 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i+=1
#         j+=1

#     elif nums[j] == 0 and nums [i] !=0 :
#         i+=1
#         j+=1

#     elif nums [i] != 0 and nums [j] != 0:
#         i+=1
#         j+=1

#     elif nums[i] == 0 and nums [j] == 0:

#         j+=1
        
#         nums[i], nums[j] = nums[j], nums[i]
#         i+=1
#         j+=1
# print(nums)


# MAJORITY ELEMENT

# nums = [2,2,1,1,1,2,2]

# n = len(nums)

# majority_element = 0


# for i in range (len(nums)):
#         count = 0

#         for j in range (len(nums)):
#             if nums[i] == nums [j]:
#                 count +=1
                
#         if count>n/2:
#              majority_element = nums[i]

# print(majority_element)

# THIRD MAXIMUM NUMBER 
# nums = [3,4,6,8,1,2]

# largest = 0 
# second_largest = 0
# third_largest = 0

# for i in range (len(nums)):
#      if nums[i] > largest:
#           third_largest = second_largest
#           second_largest = largest
#           largest = nums[i]

#      elif nums[i] != largest and nums [i] > second_largest:
#           second_largest = nums[i]

#      elif nums[i] != largest and nums[i] < second_largest and nums[i] > third_largest:
#           third_largest = nums[i]


# print(third_largest)


# HEIGHT CHECKER 

# list = [1,1,4,2,1,3]

# i = 0
# j = 0
# count = 0 
# new_list = []

# for i in range (len(list)):
#     for j in range (len(list)):
#         if list[i] < list [j]:
#             new_list.append(list[i])

#     if list [i] == new_list[i]:
#         count = 0
        
#     elif list [i] != new_list[i]:
#           count += 1

# print(count)


# PRINT GREATEST ON RIGHT 

nums = [17,18,5,4,6,1]

result = [] 
greatest = 0 

for i in range (len(nums)):
    greatest = -1

    for j in range (i + 1, (len(nums))):
        if nums[j] > greatest:
            greatest = nums[j]
            
            
    result.append(greatest)


print (result)


