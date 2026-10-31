# RESHAPE 
import numpy as np
# marks =  np.array([1,2,3,4,5,6])

# print (marks.reshape (2,3))

# TRANSPOSE

# marks = np.array ([
#     [1,2,3],
#     [4,5,6]
# ])

# print (marks.T)

# BROADCASTING 

# marks = np.array ([
#     [1,2,3],
#                   [3,4,5]
#                   ])
# marks1 = np.array ([1,2,3])

# print (marks + marks1)

#   SORTING 

# marks = np.array([2,3,4,1,6,3])
# print (np.sort(marks)[::-1])

# # MAX VALUE INDEX , MIN VALUE INDEX 
# marks = np.array([2,3,4,1,6,3])
# print(np.argmax(marks))
# print(np.argmin(marks))


# # FIND INDEX

# marks = np.array([2,3,4,1,6,3])

# print(np.where(marks>2))

# # REMOVE DUPLICATES

# marks = np.array([2,3,4,1,6,3])
# print(np.unique(marks))



# CONCATENATE
# a = np.array([[1,2,3],
#               [7,8,9]])
# b = np.array([[4,5,6],
#               [9,0,0]])

# print (np.concatenate((a,b), axis = 0))



#  SPLITING 

# a = np.array([1,2,3,4,4,56,7,9])
# print(np.split(a, 2))


# MISSING VALUES

# marks = np.array([1,2,3,np.nan,5,6])

# print(marks)

# IGNORE AND SUM 

# marks = np.array([1,2,3,np.nan,5,6])

# print(np.isnan(marks))

# ignore and sum
# marks = np.array([1,2,3,np.nan,5,6])

# marks [np.isnan(marks)] = 0

# print(np.nanmean(marks))


# 