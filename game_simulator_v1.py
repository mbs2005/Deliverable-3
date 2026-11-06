
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
        self._hp = (max(self._hp, 0)) #The total hp cannot be lower than 0

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage) #Uses the take_damage to reduce the hp 

    def heal(self, hp_heal:int) -> None:
        """Can heal or increase the total hp of the caracter"""
        self.hp += hp_heal #Increases the hp 
        self.hp = (min(self.hp, 100)) #The totalt hp cant be higher than the maximum hp of the carater

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    def is_alive(self) -> 