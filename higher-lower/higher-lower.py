from data import data
from data import logo
from data import vs

import random
import os

print(logo)
final_score = 0
game_over = False
account_b = random.choice(data)

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def details(a):
    account_name = a["name"]
    account_follower_count = a["follower_count"]
    account_description = a["description"]
    account_country = a["country"]
    return account_name, account_follower_count, account_description, account_country

def compare(a, b):
    account_follower_count_a = a["follower_count"]
    account_follower_count_b = b["follower_count"]
    if account_follower_count_a > account_follower_count_b:
        return 'a'
    else:
        return 'b'

while not game_over:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    details_a = details(account_a)
    details_b = details(account_b)

    print(f"Compare A: {details_a[0]}, a {details_a[2]}, from {details_a[3]}")
    print(vs)
    print(f"Against B: {details_b[0]}, a {details_b[2]}, from {details_b[3]}")

    response = input("Who has more followers? Type 'a' or 'b': ")
    result = compare(account_a, account_b)

    clear_console()
    print(logo)

    if result == response:
        final_score += 1
        while account_a == account_b:
            account_b = random.choice(data)
        print(f"Great! Your current score is: {final_score}")
    else:
        game_over = True
        print(f"Game over! Your final score is: {final_score}")



