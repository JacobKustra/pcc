from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
       print(randint(1, self.sides))

dice = Die(6)
dice10 = Die(10)
dice20 = Die(20)

dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()

dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()

dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
