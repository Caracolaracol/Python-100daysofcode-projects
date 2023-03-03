
import random
choice = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors. \n"))

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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
computer_choice = random.randint(0,2)
print(game_images[choice])
print("Computer choice:")
print(game_images[computer_choice])

if choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and choice == 2:
    print("You lose")
elif choice >=3 or choice < 0 :
    print("You typed an invalid number, you lose!")
elif computer_choice > choice :
    print("You lose")
elif computer_choice < choice :
    print("You win!")
elif choice == computer_choice:
    print("thats a draw")
