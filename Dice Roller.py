import random


def roll_dice():
    print("Rolling Dice.....")
    return random.randint(1, 6)


print("Welcome to the Dice Simulator!")
while True:
    input("Press enter to rolla dice!")
    dice_result = roll_dice()
    print("You rolled a", dice_result)
    print('Thanks for playing!')
    break