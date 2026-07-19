SHOPPING CART PROBLEM 


foods = []
prices = []
total = 0 

while True:
    food = input("enter your item (q to quit): ")
    if food.lower() == "q":
        break

    else:
        price = float(input("enter a price: "))
        foods.append(food)
        prices.append(price)

print("------you are done------")

for food in foods:
    print(food , end=" ")

for price in prices:
    total += price

print(total)



print(total)


