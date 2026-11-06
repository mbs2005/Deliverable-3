class Warrior(Character):
    "A character type focusing on defense using armor"
    
    def __init__(self, name: str, hp_max: int = 120, damage: int = 12, weapon = None, armour: int = 5) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.armour: int = armour
        
    def take_damage(self, hp_loss: int) -> None:
        "Reduces incoming damage by armer before applying it to HP"
        reduces_damage = max(hp_loss - self.armour, 0) #Does that the damage cant be negative
        super().take_damage(reduces_damage)
        
class Mage(Character):
    "A character type using mana to cast powerful spels"
    
    def __init__(self, name: str, hp_max: int = 80, damage: int = 8, weapon = None, mana: int = 30) -> None:
        super().__init__(name, hp_max, damage, weapon)
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