import random
from traceback import print_tb

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock ,paper,scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game[user_input])
computer = random.randint(0 , len(game)-1)
print("Computer chose : \n" + game[computer])


if user_input == computer :
    print("It's a draw")
elif (user_input == 0  and computer==1) or (user_input ==1 and computer ==2) or (user_input ==2 and computer ==0):
    print("You loose")
elif (user_input ==1  and computer==0) or (user_input ==2 and computer ==1) :
    print("You win")
elif 0 < user_input >= 3 :
    print("Invalid input , you loose . Pls try again")


