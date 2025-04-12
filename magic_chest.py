
import random

class MagicChest:
    def __init__(self):
        self.items = [
            {"name": "Health Potion", "type": "buff", "effect": 10},
            {"name": "Poison Trap", "type": "curse", "effect": -10},
            {"name": "Steel Blade", "type": "buff", "effect": 5},
            {"name": "Cursed Amulet", "type": "curse", "effect": -5},
            {"name": "Heroic Elixir", "type": "buff", "effect": 15},
        ]

    def open(self, hero):
        print("\nYou open a glowing Magic Chest...")

        options = [item for item in self.items if item["type"] == ("buff" if hero.health_points >= 20 else "curse")]

        if options:
            item = random.choice(options)
            print(f"Inside the chest you found: {item['name']} ({item['effect']} HP)")
            hero.health_points += item["effect"]
        else:
            print("The chest was mysteriously empty.")
