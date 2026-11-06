import random

class Dice:
    "A class where you can make a dice with a number of given sides"
    
    def __init__(self, sides: int = 6) -> None:
        "Makes a standard dice with 6 sides"
        self.sides = sides
        
    def roll(self) -> int:
        "Roll the dice and return a random number between 1 and the number of sides"
        return random.randint(1, self.sides)
    
    def __repr__(self) -> str:
        "Return a string representation of the dice object"
        return f"Dice(sides={self.sides})"
    
    def __call__(self) -> int:
        "Allows a dice instance to be called directly like a function to roll it"
        return self.roll()
    
        """# Try to use the dice function
terning = Dice()
print(terning.roll())
print(terning)

d20 = Dice(sides = 20)
print(d20())"""
