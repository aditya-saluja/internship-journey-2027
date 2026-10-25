# reverse an strings 

# nums = [1,2,3,4]

# i = 0 
# j = len (nums) - 1

# while i < j:
#     nums [i], nums [j] = nums [j], nums[i]

#     i +=1
#     j-=1

# print(nums)


# reverse word in a string 

nums = ("idaa em kcuf")

words = nums.split()

for k in range(len(words)):
    word = list(words[k])

    i = 0 
    j = len(word) - 1

    while i < j:
        word [i], word[j] = word[j], word[i]

        i+=1
        j-=1

        words[k] = "".join (word)

print (" ".join(words))









