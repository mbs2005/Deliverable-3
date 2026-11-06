
class Battle: 

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Defines the two characters that will fight each other""" 
        self.character1 = hero
        self.character2 = enemy
    
    def play_round(self) -> None:
        """Starts a battle between the two characters"""
        #Hero attacks the enemy
        self.hero.attack(self.enemy)

        print(f"{self.hero} attacks {self.enemy} and deals {self.hero.damage} damage!")
        print(f"{self.enemy} has {self.enemy.hp} Hp left!")

        #Enemy attacks hero 
        if self.enemy.is_alive:
            "Checks if the enemy is still alive befor attacking. If the enemy is still alive, it will attack back"
            self.enemy.attack(self.hero)

            print(f"{self.enemy} attacks {self.hero} and deals {self.enemy.damage} damage!")
            print(f"{self.hero} has {self.hero.hp} Hp left!")

    def simulate_battle(self) -> None:
        """Simulates the battle until the hero or enemy is defeated"""
        #Counts hpw manny rounds they have fought
        round_counter = 1

        #Checks if the hero or enemy is still alive. If one is dead, the battle ends. If not they will keepp fighting and the round counter will add 1 round
        while self.hero.is_alive and self.enemy.is_alive:
            print(f"Round number: {round_counter}")
            
            self.play_round()

            round_counter += 1
            
        #Prints the winner of the match
        if self.hero.is_alive: 
            print(f"{self.hero} is the winner!")
        else:
            print(f"{self.enemy} is the winner!")
            




        
