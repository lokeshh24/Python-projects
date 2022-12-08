print("Welcome to the tip calculator !")
bill = float(input("What was the total bill? \n"))
tip = int(input("How much tip you like to give? 10, 12, or 15? \n"))
tip_percent = tip*bill/100
total_bill = bill + tip_percent
split = int(input("How many people to split the bill? \n"))
bill_pp = "{:.2f}".format(total_bill/split)
print(bill_pp)