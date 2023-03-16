import time
import random

def P_and_D():
    print("Welcome to P&D, Pythons and Dragons!")
    time.sleep(1)
    print("Before we set out on our adventure, let's learn a bit more about you.")
    time.sleep(1)
    name = input("What is your name? ").capitalize()
    print(f"Hello, {name}! We have a fight ahead of us so we are going to need to get you set up.")
    time.sleep(1)
    print("We will need to choose a class. You can pick from 3. Fighter, Mage or Archer")
    time.sleep(1)
    rpg_class = input("What kind of fighter are you? ").capitalize()

    player_damage = 28
    player_health = 100
    rahuul_base_health = 85
    rahuul_damage = 20
    player_xp = 0

    if rpg_class == 'Fighter':
        print(f"Sounds good, {name}! You're a Fighter with a base damage of {player_damage}!")
    elif rpg_class == 'Mage':
        print(f"Sounds good, {name}! You're a Mage with a base damage of {player_damage}!")
    elif rpg_class == 'Archer':
        print(f"Sounds good, {name}! You're a Archer with a base damage of {player_damage}!")

    time.sleep(2)

    start_quest = input(f"{rpg_class} {name}, we have some work to do, are you ready to enter the Tombs of Rahuul? ").capitalize()

    if start_quest == 'Yes':
        print("Great! Let's go!")
    else:
        print(f"Well fine, {name}! I guess we can wait. Just remember, when we start over I will have amnesia and we'll have to start over from the beginning.")
        play_again = input("Would you like to play again? ").capitalize()
        if play_again == 'Yes':
            print(P_and_D())
        else:
            quit()

    time.sleep(2)

    print(f"{name}, We have entered the Tomb of Rahuul. It's pretty gross in here.")
    time.sleep(1)
    print("There seems to be two ways we can go. From the left we can hear a low roaring sound.")
    time.sleep(1)
    print("From the right you see a small room with a chest against the wall.")
    time.sleep(1)
    first_chosen_direction = input(f"Which way would you like to go, {name}? (Hint: There could be some tastey loot in there to the right!) ").capitalize()
    time.sleep(1)
    opened_chest = 'Placeholder'
    weapon = ''
    if first_chosen_direction == 'Left':
        print(f"On no, {name}! You were mauled to death by an Owlbear! Better luck next time, should have gone right.")
        play_again = input("Would you like to play again? ").capitalize()
        if play_again == 'Yes':
            print(P_and_D())
        else:
                quit()
    elif first_chosen_direction == 'Right':
        print("You walk in to the room with the chest.")
        time.sleep(1)
        opened_chest = input("Would you like to open the chest? ").capitalize()
        if opened_chest == 'Yes' and rpg_class == 'Fighter':
            weapon = 'Two-Handed sword of big swings!'
            player_damage += 10
            print(f"You looted a {weapon}")
            time.sleep(2)
            print(f"Your base damage also increased by 10! Your attacks deal {player_damage} with each successful attack!")
        elif opened_chest == 'Yes' and rpg_class == 'Mage':
            weapon = 'Big Human Wand of shoots big magic!'
            player_damage += 10
            print(f"You looted a {weapon}")
            time.sleep(2)
            print(f"Your base damage also increased by 10! Your attacks deal {player_damage} with each successful attack!")
        elif opened_chest == 'Yes' and rpg_class == 'Archer':
            weapon = 'Cool Bow of Unspoken Truths!'
            player_damage += 10
            print(f"You looted a {weapon}")
            time.sleep(2)
            print(f"Your base damage also increased by 10! Your attacks deal {player_damage} with each successful attack!")

    time.sleep(1)
    print(f"{name}, it's time to enter the Den of...uh... Boss Fight Room.")
    time.sleep(1)
    boss_start = input("Enter the Boss Fight Room? ").capitalize()
    if boss_start == 'No':
        time.sleep(1)
        print("But we made it all the way here? Fine, fine. You're scared, I get it... *cough* Wimp *cough*")
        play_again = input("Would you like to play again? ").capitalize()
        if play_again == 'Yes':
            print(P_and_D())
        else:
            quit()
    elif boss_start == 'Yes':
        print(f"Oh wow, he is PISSED. Probably not too happy that we took that {weapon} from that chest.")
        time.sleep(1)
        dodge = input("He's coming right for you! Quick! Type in 'dodge' to dodge his attack! ").capitalize()
        if dodge == 'Dodge':
            time.sleep(1)
            print(f"Phew, {name}! That was close!")
            time.sleep(1)
        else:
            time.sleep(1)
            print("There wasn't even a time limit OR you spelled dodge wrong. How do you do that? It's literally typed on the screen.")
            time.sleep(1)
            print("Better luck next time!")
            play_again = input("Would you like to play again? ").capitalize()
            if play_again == 'Yes':
                print(P_and_D())
            else:
                quit()


    print("Here's what you should know, Rahuul has 85 health so we are going to have to fight hard if we want to win and take his loot.")
    time.sleep(3)
    attack = input(f"He's off-balance now that we dodged his attack. Type 'attack' to catch him off-guard with your {weapon} ").capitalize()
    if attack == 'Attack':
        player_roll = random.randint(-1, 100)
        rahuul_roll = random.randint(-1, 100)
        if player_roll > rahuul_roll:
            rahuul_base_health = 0
            player_xp += 100
            time.sleep(2)
            print(f"You hit him super hard and one-shotted him ganing 100 XP! Your XP is now {player_xp} Let's loot!")
            time.sleep(2)
            print("*you rummage around his pockets, what's left of them anyways*")
            time.sleep(3)
            print("You found the Skull of Rahuul! Weird his own head was in his pocket...")
            time.sleep(2)
            print("Thanks for playing P&D, Pythons and Dragons!")
            time.sleep(3)
            play_again = input("Would you like to play again? ").capitalize()
            if play_again == 'Yes':
                print(P_and_D())
            else:
                quit()
        elif rahuul_roll > player_roll:
            print("...Getting dice roll results")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("Uh oh, you were killed by Rahuul! Better luck next time!")
            time.sleep(2)
            print("Thanks for playing P&D, Pythons and Dragons!")
            time.sleep(3)
            play_again = input("Would you like to play again? ").capitalize()
            if play_again == 'Yes':
                print(P_and_D())
            else:
                quit()
            

play_game = input("Would you like to play P&D, Pythons and Dragons? ").capitalize()
if play_game == 'Yes':
    print(P_and_D())

play_again = input("Would you like to play again? ").capitalize()
if play_again == 'Yes':
    print(P_and_D())
else:
    quit()

