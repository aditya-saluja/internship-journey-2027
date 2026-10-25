# # UNION OF 2 LIST IN SORTED LIST

# num1 = [10,20,30,40,50,60]
# num2 = [10,15,20,25,30,35]

# new_num = []
# i = 0
# j = 0

# while i < len(num1) and  j < len (num2):

#     if num1[i] == num2[j]:
#         # i+= 1
#         new_num.append(num1[i])
#         i+=1
#         j+=1

#     elif num1[i] <= num2[j]:
#             # i+=1
#             new_num.append(num1[i])
#             i+=1

#     elif num1[i] >= num2[j]:
#                 # j+=1
#                 new_num.append(num2[j])
#                 j+=1

# while i < len(num1):
#        new_num.append(num1[i])
#        i+=1

# while j < len(num2):
#        new_num.append(num2[j])
#        j+=1


# print(new_num)



# num = [8,4,2,1,3,5,7,9,10]

# k = 3
# result = [num[-k:]+ num[:-k]]

# print(result)


# second maximum 

# numbers =  [12, 35, 1, 10, 34, 35]

# largest = numbers[1]
# second_largest = numbers [0]



# for number in numbers:
#     if number > largest:
#         largest = number
#         second_largest = largest

#     if number < second_largest:
#         second_largest = number

#     if number == largest:
#         largest = number

# print(second_largest)




# numbers = [1, 1, 2, 2, 3, 4, 4, 5]

# result = []

# for number in numbers:
#     if number not in result:
#         result.append(number)

# print(result)

    


# numbers = [1, 3, 4, 2, 2]

# seen = []

# for number in numbers:
#     if number not in seen:
#         seen.append(number)

#     else:
#         print("duplicate :" , number)
        


# nums1 = [1,1,2,2]
# nums2 = [2,2]

# final = []

# i = 0
# j = 0

# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         final.append(nums1[i])
#         i +=1
#         j +=1  

#     elif nums1[i] <  nums2[j]:
#         i += 1


#     else:
#         j+=1



# print(final)


# num =  ["h","e","l","l","o"]
# # Output: ["o","l","l","e","h"]

# i = 0
# j = len(num) - 1

# while i < j:
#     num [i],num[j] = num[j], num[i]

#     i+=1
#     j-=1

# print(num)



# numbers = [1, 2, 3, 4, 5]

# i = len(numbers) -1

# while i > 0:
#     numbers [i] , numbers[i - 1] = numbers [i-1], numbers [i ]

#     i-=1

# print(numbers)
    


# nums = [1,2,3,4,5,6,7]

# k = 3

# for _ in range(k):
#      last = nums[-1]

#      i = len(nums)-1
     
#      while i > 0 :
#            nums [i] = nums [i-1]
#            i -= 1
           
#      nums[0] = last
     

# print(nums)



# numbers = [9,0,0,2,3,4]

# i = 0

# for number in numbers:
#     if number != 0:
#         numbers[i] = number
#         i += 1
        
# while i < len(numbers):
#       numbers [i] = 0
#       i += 1

# print(numbers)



numbers =[0,1,3]

numbers.sort()
i = 0


for i in range (len(numbers)-1):
    if numbers[i+1] != numbers[i]+1:
        print(numbers[i] + 1)
        break
          
    















    


        

     
 


