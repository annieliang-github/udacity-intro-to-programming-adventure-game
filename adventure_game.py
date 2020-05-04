import time
import random

def print_pause(msg):
    print(msg)
    time.sleep(2)

def intro(item, monster):
    print_pause("You find yourself standing in an open field,"
            " filled with grass and yellow flowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere "
            "around here, and has been terrifying the village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a peaceful lake.")
    print_pause("Now be a hero and save the village!")

def field(item, monster):
    print_pause("What would you like to do?")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to dive into the lake.")
    while True:
        choice = input("Please enter 1 or 2.\n")
        if choice == "1":
            house(item, monster)
            break
        elif choice == "2":
            lake(item, monster)
            break

def house(item, monster):
    print_pause("You approach the door of the house.")
    print_pause("There's suddenly a huge noise.")
    print_pause("Boom! The " + monster + " opens the door.")
    if "sword" not in item:
        print_pause("You are shocked and under-prepared.")
        print_pause("You need to find a weapon!")
        print_pause("Would you like to fight anyway?")
        while True:
            tofight = input("Please enter 1 to fight or 2 to run.\n")
            if tofight == "1":
                print_pause("You are trying your best to attack.")
                print_pause("But because you are not properly armed.")
                print_pause("You have been defeated.")
                play_again()
                break
            elif tofight == "2":
                print_pause("You run back to the field.")
                print_pause("Luckily, you are not followed.")
                field(item, monster)
                break
    elif "sword" in item:
        print_pause("It seems you are ready to fight.")
        print_pause(monster + " open his mouth to bite you.")
        print_pause("You quickly move away and chop down his neck.")
        print_pause("You defeated the monster!")

def lake(item, monster):
    if "sword" in item:
        print_pause("You cautiously dive into the lake, again.")
        print_pause("You are out of luck this time.")
        print_pause("There's nothing more under the lake.")
        print_pause("You quickly swim back to the field.")
    else:
        print_pause("Your cautiously dive into the lake.")
        print_pause("Something caught your foot.")
        print_pause("You found a sword under the mud!")
        print_pause("This is definitely some weapon you can use.")
        print_pause("You quickly swim back to the field.")
        item.append("sword")
    field(item, monster)

def play_again():
    again = input("Would you like to play again? yes/no\n").lower()
    if again == "yes":
        print_pause("Awesome! Restarting the game...")
        play()
    elif again == 'no':
        print_pause("Village needs you, please come back.")
    else:
        play_again()

def play():
    item = []
    monster = random.choice(["dragon", "zombie", "ghost", "werewolf"])
    intro(item, monster)
    field(item, monster)

play()
