import random


possible_dices = [3, 4, 6, 8, 10, 12, 100]

def dice_rolling(number_of_dice, dice_type = 6, modifier = 0):
    if dice_type in possible_dices:
        result = sum ([random.randint(1, dice_type) for _ in range(number_of_dice)]) + modifier
        return result
    else:
        return "Wrong dice type"

a = dice_rolling(2, 100)
print(a)