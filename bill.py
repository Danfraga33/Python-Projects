print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip = int(input("What percentage tip would you give? 10, 12 or 15?"))
total = (bill * (1 + tip / 100))
print("Each person should pay: ", total / people)
