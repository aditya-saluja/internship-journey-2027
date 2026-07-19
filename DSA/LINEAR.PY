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
numbers = [1,2,3,4,5]

sorted_array = True

for i in range (len(numbers) -1):
    if numbers [i] > numbers [i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("sorted")

else:
    print("nooo")