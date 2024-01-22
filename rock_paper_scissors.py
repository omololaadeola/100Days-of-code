import random

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
game = [rock, paper, scissors]
user_input = int(input("Choose your game, type 0 for rock, 1 for paper, and 2 for scissors.\n"))
print(game[user_input])

computer_choice = random.randint(0,2)
print(game[computer_choice])

if user_input > 2 or user_input < 0:
    print("invalid input, you lose.")
elif user_input == computer_choice:
    print("It's a draw")
elif user_input > computer_choice:
    print("You win!")
elif user_input < computer_choice:
    print("You lose!")