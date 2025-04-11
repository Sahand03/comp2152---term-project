import random
from character import Character

class Hero(Character):
    def __init__(self):
        combat_strength = random.randint(1, 6)
        health_points = random.randint(1, 20)
        super().__init__(combat_strength, health_points)

    def hero_attacks(self, monster):
        print(f"Player's attack ({self.combat_strength}) -> Monster ({monster.health_points})")
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("You have killed the monster")
        else:
            monster.health_points -= self.combat_strength
            print(f"You have reduced the monster's health to: {monster.health_points}")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()
