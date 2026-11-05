import random
import time


def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]


def find_winner(computer_dice, user_dice):
    computer_total = sum(computer_dice)
    user_total = sum(user_dice)
    print("computer total:", computer_total)
    print("user total:", user_total)

    if user_total > computer_total:
        print("user wins")
    elif user_total < computer_total:
        print("computer wins")
    else:
        print("it's a tie")


def roll_again(choices, dice_list):
    print("rolling again...")
    time.sleep(1)

    for i, choice in enumerate(choices):
        if choice == "r":
            dice_list[i] = random.randint(1, 6)

    time.sleep(1)


def computer_strategy1(n):
    print("computer is thinking...")
    time.sleep(1)
    return "r" * n


def computer_strategy2(computer_rolls):
    print("computer is thinking...")
    time.sleep(1)
    return "".join("r" if roll < 5 else "-" for roll in computer_rolls)


number_dice = int(input("enter number of dice: "))
ready = input("ready to start? hit any key to continue:")

user_rolls = roll_dice(number_dice)
print("user first roll:", user_rolls)

while True:
    user_choices = input("enter - to hold or r to roll again: ")
    if len(user_choices) == number_dice and all(choice in "r-" for choice in user_choices):
        break
    print("you must enter", number_dice, "choices using only - or r")

roll_again(user_choices, user_rolls)
print("player new roll:", user_rolls)

print("computer turns")
computer_rolls = roll_dice(number_dice)
print("computer first roll:", computer_rolls)
computer_choices = computer_strategy2(computer_rolls)
print("computer choices:", computer_choices)
roll_again(computer_choices, computer_rolls)
print("computer new roll:", computer_rolls)

find_winner(computer_rolls, user_rolls)
