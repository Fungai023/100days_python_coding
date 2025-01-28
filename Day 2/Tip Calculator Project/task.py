
print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 or 12 or 15 :"))
people = int(input("How many people to split the bill? "))
result = (bill * (tip/ 100) + bill) / 5
print(f"Each person should pay: $ {round(result, 2)}")


