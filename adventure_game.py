import time
import random

weapon = ["steel sword", "silver sword"]
enemy = ["dragon", "pirate", 'wizard']
item = ""
enemy_chosed =""

def print_pause(message):
    print(message)
    time.sleep(1)


def field():
    print_pause("You find yourself standing in an open field,filled with "
                "grass and yellow wildflowers."
                "Roumor has it that a pirate is somwhere around here,and "
                "has been tarrifying the nearby village.")
    print_pause("In front of you is a house."
                "To your right is a dark cave."
                "In your hand you hold your trusty(but not very effective)"
                "dagger.")


def choice(item, enemy_chosed):

    print_pause("Enter 1 to knock on the door of the house."
                "Enter 2 to peer into the cave."
                "What would you like to do ?")
    response = input("(Please enter 1 or 2.)\n")
    if response == "1":
        house(item, enemy_chosed)
    elif response == "2":
        cave(item)
    else:
        return response


def cave(item):
    print_pause("You peer cautiously into the cave"
                "It turns out to be only a very small cave.")
    if item == "":
        item_found = random.choice(weapon)
        print_pause("Your eye catches a glint of metal behind a rock."
                    "Your have found the " + item_found)
        item=item_found
        print_pause("You discard your silly old dagger and take it with you.")
    else:
        print_pause("You've beem here before,and gotten all the good stuff,It's"
                    "just an empty cave now.")
    print_pause("You walk back out to the field.")
    choice(item, enemy_chosed)


def house(item, enemy_chosed):
    if enemy_chosed == "":
        enemy_chosed=random.choice(enemy)
    print_pause("You approache the door of the house."
                "You are about to knock the door opnes and out steps a " + str(enemy_chosed))
    print_pause("Eep! This is the pirate's house!"
                "The " + str(enemy_chosed) + " attacks you!")
    response = input("Would you like to (1) fight or (2) run away?\n")
    if response == "1":
        print_pause("As the " + str(enemy_chosed) + " moves to attack,"
                                               "you unsheath your new weapon."
                                               "The new weapon shines brightly in your hand as "
                                               "you brace yourself for the attack")
        if len(item) == 0:
            print_pause("You do your best..."
                        "but your dagger is no match for the wicked fairie"
                        "You do your best...")
            restart()
        else:
            print_pause("But the dragon takes one look at your shiny new toy and run away!"
                        "You have rid the town of the dragon.You are victious!")
            restart()
    elif response == "2":
        print_pause("You run back into the field, Luckily,"
                    "you don't seem to have been followed")
        choice(item, enemy_chosed)
    else:
        return response


def restart():
    response = input("Would you to play again?(y/n)\n")
    if "y" in response:
        print_pause("Excellent! Restarting the game...")
        field()
        choice(item, enemy_chosed)
    elif "n" in response:
        print_pause("Thank for playing! See you next time.")
    else:
        return response


field()
choice(item, enemy_chosed)
