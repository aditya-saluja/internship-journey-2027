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

# numbers = [[1,2], [2,3], [3,4]]

# added_list = []
# i = 0
# largest = 0

# for number in numbers:
#     i =  sum(number)
#     added_list.append(i)

#     largest = added_list[0]

#     for value in added_list:
#         if value > largest:
#             largest = value

    

# print(largest)n

# 
# permutation 

# numbers = [0,2,1,5,3,4]

# i = 0
# new_list = []

# for i in range (len(numbers)):
#       answer = numbers[numbers[i]]
#       new_list.append(answer)
    
      
# print(new_list)



# numbers = [2,3,5,1,3]

# maximum = 5
# extra = 3
# i = 0

# for number in numbers:
#     if number + extra >= maximum:
#          print("true")

# else:
#          print("false")


# PROBLEM 2235
# def addition(num1, num2):
#     return num1 + num2

# print(addition(2 , 3))


# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation: 
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

def most_words(sentences):
    
    maximum = 0

    for sentence in sentences:
       
       words = sentence.split()

       if len(words) > maximum:
           maximum = len(words)
           
           
    return maximum
    
sentences = ["alice and bob love leetcode", 
             "i think so too",
             "this is great thanks very muc"]

print(most_words(sentences))



        
        



      
        
    
    





    

    








