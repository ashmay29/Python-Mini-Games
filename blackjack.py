import random

is_game_over = False
user_starting_hand = []
dealer_starting_hand = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

for _ in range(2):
    user_starting_hand.append(deal_card())
    dealer_starting_hand.append(deal_card())

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_sum, dealer_sum):
    if user_sum == dealer_sum:
        print("It is a Draw.")
    elif dealer_sum == 0 or user_sum > 21:
        print("You Lose.")
    elif user_sum == 0 or dealer_sum > 21:
        print("You Win.")
    elif user_sum > dealer_sum:
        print("You Win.")
    else:
        print("You Lose.")

while not is_game_over:
    user_sum = calculate_score(user_starting_hand)
    dealer_sum = calculate_score(dealer_starting_hand)
    print(f"Your cards are: {user_starting_hand}")
    print(f"The dealer's first card is: {dealer_starting_hand[0]}")
    print(f"The sum of your cards is: {user_sum}")

    if user_sum > 21 or user_sum == 0 or dealer_sum == 0:
        is_game_over = True
    else:
        response = input("Do you want to draw another card? (yes/no) ")
        if response.lower() == "yes":
            user_starting_hand.append(deal_card())
            user_sum = calculate_score(user_starting_hand)
            print(f"Your new cards are: {user_starting_hand}, sum: {user_sum}")
        else:
            print(f"Your final hand: {user_starting_hand}, final sum: {user_sum}")
            is_game_over = True

while dealer_sum != 0 and dealer_sum < 17:
    dealer_starting_hand.append(deal_card())
    dealer_sum = calculate_score(dealer_starting_hand)

print(f"Dealer's final hand: {dealer_starting_hand}, final sum: {dealer_sum}")
compare(user_sum, dealer_sum)
