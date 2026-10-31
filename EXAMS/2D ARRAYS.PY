nums = [
    [1,2,3],
    [4,5,6], 
    [7,8,9]
]

# rows = len(nums)
# cols = len(nums[0])


# for i in range (0, rows):
#     for j in range(0, cols):
        
#         print(nums[i][j])


# PRINT UPPER TRIANGLE
# rows = len(nums)
# cols = len(nums[0])


# for i in range (0, rows):
#     for j in range(0, cols):
#         if j >= i:
#             print(nums[i][j], end=" ")

#         else:
#             print("*", end=" ")

#     print()


# PRINT DIAGNOL LEFT TO RIGHT
# rows = len(nums)
# cols= len(nums[0])
# total = 0 

# for i in range (0, rows):
#     for j in range(0, cols):

#         if i == j :
             
#             print(nums[i] [j], end="")
#             total = total + nums[i] [j]
            

#         else:
#             print(end=" ")

#     print()
# print()
# print(total)


# # PRINT DIAGNOL RIGHT TO LEFT 
# rows = len(nums)
# cols = len(nums[0])


# for i in range (0, rows):
#     for j in range (0, cols):
#         if i + j == 2:
#             print(nums[i][j], end=" ")

#         else:
#             print(end= " ")

#     print()


# transpose a matrix 


# rows  = len(nums)
# cols = len(nums[0])

# result = [[0] * rows for _ in range (cols)]

# for i in range (0, rows):
#     for j in range (0, cols):
#         result [j][i] = nums [i][j]

# print(result)


# RESHAPE IN MATRIX 

rows = len(nums)
cols = len(nums[0])

r = 3
c = 2

result = [[0] * c for _ in range(r)]

for i in range(rows):
    for j in range(cols):
        index = i * cols + j

        new_i = index // c
        new_j = index % c

        result[new_i][new_j] = nums[i][j]

print(result)



# rows = len(nums)
# cols = len(nums[0])

# sum_diagonal = 0

# for i in range(rows):
#     sum_diagonal += nums[i][i]

# print(sum_diagonal)


# ADDITION OF DIAGNOL


# rows = len(nums)
# cols = len(nums[0])

# sum_diagonal = 0

# for i in range(rows):
#     sum_diagonal += nums[i][i]              # main diagonal
#     sum_diagonal += nums[i][cols - 1 - i]  # secondary diagonal

# print(sum_diagonal)


