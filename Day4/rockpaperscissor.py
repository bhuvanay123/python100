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
import random
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice=random.randint(0,2)
print("User's Choice:")
if user_choice==0:
  print(rock)
elif user_choice==1:
  print(paper)
else:
  print(scissors)
print("Computer's Choice:")
if comp_choice==0:
  print(rock)
elif comp_choice==1:
  print(paper)
else:
  print(scissors)
if user_choice==0:
  if comp_choice==0:
    print("It's a tie!")
  elif comp_choice==1:
    print("You lose!")
  else:
    print("You won!")
elif user_choice==1:
  if comp_choice==0:
    print("You won!")
  elif comp_choice==1:
    print("It's a tie!")
  else:
    print("You lost!")
else:
  if comp_choice==0:
    print("You lost!")
  elif comp_choice==1:
    print("You won!")
  else:
    print("It's a tie!")
  