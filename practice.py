# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age??  "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill =  7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <=55:
#     print("Ride is on us.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
#   want_photos = input("Do you want a photo taken? y or n ")
#   if want_photos == "y":
#     bill += 3
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride. ")


#*****************************************************************************************************************************************

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]

# #print(dirty_dozen)


# print(dirty_dozen[0])
# print(dirty_dozen[1])


# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

#************************************************************************************************************************

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# vertical_column = int(position[0])
# horizontal_row = int(position[1])

# select_row = map[horizontal_row - 1]
# select_row[vertical_column-1] = "X"
# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#****************************************************************************************************************************

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Papper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print(rps[human])

print("Computer Choose: ")
comp = (random.choice(rps))
print(comp)

if human == rock and comp == scissors:
  print("You won")
if human == paper and comp == rock:
  print("You won")
if human == scissors and comp == paper:
  print("You won")
if human == rock and comp == paper:
  print("You loose")
if human == paper and comp == scissors:
  print("You loose")
if human == scissors and comp == rock:
  print("You loose")
else:
  print("Draw")







