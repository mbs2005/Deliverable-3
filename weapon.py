from dice import Dice

class Weapon:
    "A class representing a weapon that uses the dice for damage calculations"
    
    def __init__(self, name: str, damage_dice: Dice) -> None:
        "Initializes a weapon with a name and a damage-dealing dice"
        self.name: str = name
        self.damage_dice = damage_dice
        
    def roll_damage(self) -> int:
        "Rolls the weapon damage dice and return the resulting damage"
        return self.damage_dice.roll()
    
    def __repr__(self) -> str:
        "Return a string representation of the weapon object"
        return f"Weapon(name = '{self.name}', damage_dice = {self.damage_dice})"
    