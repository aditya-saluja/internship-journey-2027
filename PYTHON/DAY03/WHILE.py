# COMPOUND CALCULATOR 

principle = 0 
time = 0
rate = 0 

while principle <= 0:
    principle = float(input("enter a valid principle  amount: "))
    if principle <= 0:
        print("enter again: ")

print(f"thanks for the {principle} principle amount")


while time <= 0:
    time = int(input("enter a valid time in years: "))
    if time <= 0:
        print("enter again: ")

print(f"thanks for the {time} year")

while rate <= 0:
    rate = int(input("enter a valid rate of intrests: "))
    if rate <= 0:
        print("enter again: ")

print(f"thanks for the {rate} % rate of intrests")



total = principle * pow((1+ rate / 100),time)

print(F"this is your {total} intrest")
 

