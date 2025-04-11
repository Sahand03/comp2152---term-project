import random
from character import Character

class Monster(Character):
    def __init__(self):
        combat_strength = random.randint(1, 6)
        health_points = random.randint(1, 20)
        super().__init__(combat_strength, health_points)

    def monster_attacks(self, hero):
        print(f"Monster's attack ({self.combat_strength}) -> Hero ({hero.health_points})")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("Player is dead")
        else:
            hero.health_points -= self.combat_strength
            print(f"The monster has reduced the player's health to: {hero.health_points}")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()
