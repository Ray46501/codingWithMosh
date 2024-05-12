from random import randint

class Dice:
    def roll(self):
        roll_1 = randint(1,6)
        roll_2  = randint(1,6)
        return roll_1, roll_2
    
dice = Dice()
print(dice.roll())