import random

# random.seed(321)
# random_int=random.randint(1,10)
# print(random_int)

# random_float=random.random()
# # random_float*5
# print(random_float)

# test_seed=int(input("Create a seed number: "))
# random.seed(test_seed)

# random_int=random.randint(0,1)

# if random_int==0:
#     print("Heads ")
# else:
#     print("Tails ")

# print(random_int)

# Lists

# us_states = ["Delaware", "Pennyslvania", "Carlifonia"]
# us_states[1]="Georgia"
# us_states.append("Hawaii")
# us_states.extend(["Wisconsin","Arizona"])
# print(us_states[20])

# namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
# names = namesAsCSV.split(", ")
# number_of_names=len(names)

# random_int=random.randint(0,number_of_names-1)
# # print(names[random_int])
# print(random.choice(names))

# Nested-Lists

# dirty_dozen=["Strawberries","Apples","Kale", "Potatoes"]
# fruits=["Strawberries","Apples"]
# vegetables=["Kale","Potatoes"]

# dirty_dozen=[fruits,vegetables]

# print(dirty_dozen)

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal=int(position[0])
# vertical=int(position[1])

# map[vertical - 1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors
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
print("Rock Paper Scissors")

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computer_choice = random.randint(0, 3)

game_images = [rock, paper, scissors]

if player_choice == 0:
    print(f"You chose {player_choice}: " + rock)
    if computer_choice == 1:
        print(f"Computer chose {computer_choice}: " + paper + "\n You lose")
    elif computer_choice == 2:
        print(f"Computer chose {computer_choice}: " + scissors + "\n You win")
    else:
        print(f"Computer chose {computer_choice}: " + rock + "\n It's a draw")
elif player_choice == 1:
    print(f"You chose {player_choice}: " + paper)
    if computer_choice == 0:
        print(f"Computer chose {computer_choice}: " + rock + "\n You win")
    elif computer_choice == 1:
        print(f"Computer chose {computer_choice}: " + paper + "\n It's a draw")
    else:
        print(f"Computer chose {computer_choice}: " + scissors + "\n You lose")
elif player_choice == 2:
    print(f"You chose {player_choice}: " + scissors)
    if computer_choice == 0:
        print(f"Computer chose {computer_choice}: " + rock + "\n You lose")
    elif computer_choice == 1:
        print(f"Computer chose {computer_choice}: " + paper + "\n You win")
    else:
        print(f"Computer chose {computer_choice}: " +
              scissors + " \n It's a draw")
else:
    print("Invalid Choice. ")
