
class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, hp_loss:int) -> None:
        """Take damage and reduce hp"""
        self._hp -= hp_loss #Reduce hp by teh damage taken
        self._hp = (max(self.hp, 0)) #The total hp cannot be lower than 0

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage) #Uses the take_damage to reduce the hp 

    def heal(self, hp_heal:int) -> None:
        """Can heal or increase the total hp of the caracter"""
        self._hp += hp_heal #Increases the hp 
        self._hp = (min(self.hp, self.hp_max)) #The totalt hp cant be higher than the maximum hp of the carater

    def introduce(self) -> None:
        """Creates string that introd   uces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    @property
    def is_alive(self) -> bool:
        """Checks if the caracter is alive by true or false"""
        return self.hp >0 

class Warrior(Character):
    "A character type focusing on defense using armor"
    
    def __init__(self, name: str, hp_max: int = 120, damage: int = 12, weapon = None, armour: int = 5) -> None:
        super().__init__(name, hp_max, damage)
        self.weapon = weapon
        self.armour: int = armour
        
    def take_damage(self, hp_loss: int) -> None:
        "Reduces incoming damage by armer before applying it to HP"
        reduces_damage = max(hp_loss - self.armour, 0) #Does that the damage cant be negative
        super().take_damage(reduces_damage)
        
class Mage(Character):
    "A character type using mana to cast powerful spels"
    
    def __init__(self, name: str, hp_max: int = 80, damage: int = 8, weapon = None, mana: int = 30) -> None:
        super().__init__(name, hp_max, damage)
        self.weapon = weapon
        self.mana_max: int = mana
        self.mana: int = mana
        
    def attack(self, target) -> None:
        "Attack using magic if enough mana is avalible, else falls back to a base attack and restore mana"
        if self.mana >= 10:
            self.mana -= 10
            #Magic attack gives doubble damage and ignores weapons
            magical_damage = self.damage * 2
            target.take_damage(magical_damage)
        else:
            #Gets back 5 mana when it is a standard attack
            self.mana = min(self.mana + 5, self.mana_max)
            super().attack(target)