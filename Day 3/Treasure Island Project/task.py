import game_logos as logo

print(logo.game)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

def cross_roads(place_one ,options ) :
    x,y = options
    road = input("Your at a cross road . \n\t\t Choose Left or Right\n").lower()
    if road in ["left", "l"]:
        choice = input(f"You have reached the {place_one} . {x} or {y} \n").lower()
        if choice == x.lower():
            print("You were captured and tortured to death\n Game over , Try again Later ")
        elif choice == y.lower():
            print("Congratulations ,you found the treasure chest.")
        else:
            print(f"{logo.sloth}\nGame over , got bitten by a snake due to invalid input")
    elif road in ['right','r']:
        print("You fell into an endless pit.Game over")


cross_road = input("Your at a cross road . \n\t\t Choose Left or Right\n").lower()

if cross_road in ["left","l"]:
    print(logo.fort)
    fort = input("You have reached the enemy fort  . Invade or Run \n").lower()
    if fort == "invade":
        print("You were captured and tortured to death\n Game over , Try again Later ")

    elif fort == "run":
        run = input("You find yourself in a dense forest. Ahead, you see a dark cave and a narrow wooden bridge over a river. "
                 "Do you enter the 'cave' or cross the 'bridge'?\n").lower()

        if run == "cave":
            cave = input("Inside the cave, you discover an ancient temple with three doors, each marked with a strange symbol: "
                    "a serpent, a sun, and a skull. "
                    "Which door do you enter? ('serpent', 'sun', or 'skull')\n").lower()

            if cave == "sun":
                print(logo.fountain)
                drink = input("Beyond the door, you find a glowing fountain filled with shimmering water. "
                              "A stone tablet reads: 'To unlock the path, drink from the right cup.' "
                              "There are three cups: gold, silver, and clay. "
                              "Which one do you choose?\n").lower()

                if drink == "gold":
                    cross_roads("jungle" , ("left","right"))

                elif drink == "silver":
                    print("You got an allergic reaction and died within 5 sec.Game over .")

                elif drink == "clay":
                    print("Congratulations ,you found the treasure chest.")

                else:
                    print(logo.mummy + "\tYou got mummy-fied .Game over")

            elif cave == "skull":
                print(logo.mummy + "\tYou got mummy-fied .Game over")

            elif cave == "serpent" or cave not in ['serpent', 'sun','skull']:
                print("You were poisoned by toxic fumes\n Game over .")

elif cross_road in ['right','r']:
    lake = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()

    if lake == "wait":
        print(logo.island)
        colour = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()

        if colour in ["red","r"]:
            print("Congratulations ,you found the treasure chest.")

        elif colour in ["yellow","y"]:
            print("Game over , you walked into the sun planet and got burnt.")

        elif colour in ["blue","b"]:
            print("Hello")

    elif lake == "boat" :
        cross_roads("mars",("stay","escape"))

    else:
        print(f"{logo.crocodile}\tYour were attacked by crocodiles and died . Game over ")
else:
    print(f"{logo.sloth}\nGame over , got bitten by a snake due to invalid input")
