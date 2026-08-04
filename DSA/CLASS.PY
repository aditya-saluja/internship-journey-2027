# UNION OF 2 LIST IN SORTED LIST

num1 = [10,20,30,40,50,60]
num2 = [10,15,20,25,30,35]

new_num = []
i = 0
j = 0

while i < len(num1) and  j < len (num2):

    if num1[i] == num2[j]:
        # i+= 1
        new_num.append(num1[i])
        i+=1
        j+=1

    elif num1[i] <= num2[j]:
            # i+=1
            new_num.append(num1[i])
            i+=1

    elif num1[i] >= num2[j]:
                # j+=1
                new_num.append(num2[j])
                j+=1

while i < len(num1):
       new_num.append(num1[i])
       i+=1

while j < len(num2):
       new_num.append(num2[j])
       j+=1


print(new_num)






    


        

     
 


