# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions
from hero import Hero
from monster import Monster
import os
import platform

print("Operating System:", os.name)
print("Python Version:", platform.python_version())

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Create Hero and Monster objects
hero = Hero()
monster = Monster()

print("    ------------------------------------------------------------------")
print(f"    |    Hero created with Combat Strength = {hero.combat_strength} and Health = {hero.health_points}")
print(f"    |    Monster created with Combat Strength = {monster.hero.combat_strength} and Health = {monster.hero.health_points}")

if not input_invalid:
    input_invalid = False
    hero.combat_strength = int(hero.combat_strength)
    monster.combat_strength = int(monster.combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    hero.combat_strength = min(6, (hero.combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Lab 06 - Question 5b
    functions.adjust_hero.combat_strength(hero.combat_strength, monster.combat_strength)

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    hero.health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(hero.health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    monster.health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(monster.health_points) + " health points for the monster")

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, hero.health_points = functions.use_loot(belt, hero.health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((hero.combat_strength + hero.health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    monster.combat_strength += min(6, monster.combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        monster.combat_strength) + " using the " + power_roll + " magic power")

    # Lab Week 06 - Question 6
    num_dream_lvls = -1 # Initialize the number of dream levels
    while (num_dream_lvls < 0 or num_dream_lvls > 3):
        # Call Recursive function
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")
        # If the value entered was not an integer, set the number of dream levels to -1 and loop again 
        if ((num_dream_lvls == "")):
            num_dream_lvls = -1
            print("Number entered must be a whole number between 0-3 inclusive, try again")
    
        else:
            num_dream_lvls = int(num_dream_lvls)

            if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")
            elif (not num_dream_lvls == 0):
                hero.health_points -= 1
                crazy_level = functions.inception_dream(num_dream_lvls)
                hero.combat_strength += crazy_level
                print("combat strength: " + str(hero.combat_strength))
                print("health points: " + str(hero.health_points))
        print("num_dream_lvls: ", num_dream_lvls)

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while monster.health_points > 0 and hero.health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            monster.health_points = functions.hero_attacks(hero.combat_strength, monster.health_points)
            if monster.health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                hero.health_points = functions.monster_attacks(monster.combat_strength, hero.health_points)
                if hero.health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            hero.health_points = functions.monster_attacks(monster.combat_strength, hero.health_points)
            if hero.health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                monster.health_points = functions.hero_attacks(hero.combat_strength, monster.health_points)
                if monster.health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    if(monster.health_points <= 0):
        winner = "Hero"
    else:
        winner = "Monster"

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")

        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")

        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)       


