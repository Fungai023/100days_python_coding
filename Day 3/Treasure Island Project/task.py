import game_logo as logo

print(logo.game)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road = input("Your at a cross road . \n\t\t Choose Left or Right\n").lower()


if cross_road in ["left","l"]:
    print(logo.fort)
    fort = input("You have reached the enemy fort  . Invade or Run ")

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
    else:
        print(f"{logo.crocodile}\tYour were attacked by crocodiles and died . Game over ")
else:
    print(f"{logo.sloth}\nGame over , got bitten by a snake due to invalid input")
