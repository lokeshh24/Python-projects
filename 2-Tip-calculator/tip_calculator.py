print("Welcome to the tip calculator !")
bill = float(input("What was the total bill? \n"))
tip = int(input("How much tip you like to give? 10, 12, or 15? \n"))
new_tip = tip*bill/100
total_bill = bill + new_tip
split = int(input("How many people to split the bill? \n"))
print(round(total_bill/split,2))