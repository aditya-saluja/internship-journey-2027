

no_guess = 0

guess = int(input("enter your guess: "))



while guess != 7:
    print("incorrect")
    guess = int(input("enter your guess: "))
    no_guess = no_guess + 1
print(f"you guessed in {no_guess} attempts")

print("congratulations")




