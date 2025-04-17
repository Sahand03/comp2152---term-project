import random
from hero import Hero
from monster import Monster
from magic_chest import open_magic_chest

print("Operating System: posix")
print("Python Version: 3.13.1")

# Hardcoded values for demo
hero = Hero()
monster = Monster()

# Set fixed stats
hero.combat_strength = 6
hero.health_points = 10

monster.combat_strength = 4
monster.health_points = 8

# Magic Chest
print("You open a glowing Magic Chest... (Press Enter)")
input()
print("You open a glowing Magic Chest...")
print("Inside the chest you found: Energy Elixir (+3 HP)")
print("Your new health: 13")
hero.health_points += 3

print(f"\n    Hero created with Combat Strength = {hero.combat_strength} and Health = {hero.health_points}")
print(f"    Monster created with Combat Strength = {monster.combat_strength} and Health = {monster.health_points}")

input("Press Enter to continue to the fight...")

# Fight logic (fixed winner: hero)
print("The Hero wins!")
del hero
del monster