print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

prices = {
    'S' : 15,
    'M': 20,
    'L': 25,
}

total = 0

total += prices[size]
if pepperoni.capitalize() == "Y" :
    if size.upper() == "S":
        total+= 2
    else:
        total+=3
elif extra_cheese.upper() == "Y":
    total+=1

print(f"Your final bill is: ${total}.")

