import random

def deal_cards():
    """""Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)


# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_array = []
# dealer_array = []

# to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if to_play =='y':
#     for x in range (0,2):
#         choice = random.randint(0,11)
#         user_array.append(cards[choice])
#     print(f"User array{user_array}")
#     for x in range (0,2):
#         choice = random.randint(0,11)
#         dealer_array.append(cards[choice])
#     print(f"The dealer's array: {dealer_array}")
    
# user_sum = 0
# for i in range (len(user_array)):
#     user_sum += user_array[i]
# print(f"User sum: {user_sum}")

# dealer_sum = 0
# for i in range (len(dealer_array)):
#     dealer_sum += dealer_array[i]
# print(f"Dealer sum: {dealer_sum}")

# if user_sum == 21 and dealer_sum == 21:
#     print("User Won")
#     if user_sum<21 and dealer_sum<21:
#         print("Would you like to another card")
# else:
