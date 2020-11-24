# print("Welcome to the rollercoaster!!")
# height = int(input("What is your height? "))

# bill = 0
# if height >= 130:
#     print("You can ride he rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Please pay $5")
#     elif age <= 18:
#         bill = 12
#         print("Please pay $12")
#     elif age>=45 and age <=55:
#         print("Everything is going to be ok have a ride with us!")
#     else:
#         bill =15
#         print("Please pay $15")

#     wants_photo=input("Do you want a photo taken? Y or N. ")
#     if wants_photo == 'Y':
#         bill+=3 #same as bill = bill + 3

#     print(f"Your finall bill is ${bill}")
# else:
#     print("Sorry, height not allowed!")


# BMI Calculator 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = int(round((weight/height**2), 0))
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# Leap year Calculator
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#        if year % 400 == 0:
#         print("Leap year.")
#        else:
#         print("Not Leap Year.")
#     else :
#         print("Leap Year")

# else:
#     print("Not Leap Year.")


# Pizza Order

# CODE 1
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# small_pepperoni = 2
# large_med_pepperoni = 3
# ex_cheese = 1

# print("Welcome to Python Pizza !!")
# size = input(
#     "What size of pizza would you like? L for large M for medium S for small. ")
# pep = input("Do you want pepperoni? Y or N. ")
# cheese = input("Do you want extra cheese? Y or N. ")
# if size == 'L':
#     if pep == 'Y' and cheese == 'Y':
#         large_pizza = large_pizza+large_med_pepperoni+ex_cheese
#         print(f"Your final bill is: ${large_pizza}.")
#     elif cheese == 'Y':
#         large_pizza = large_pizza+ex_cheese
#         print(f"Your final bill is: ${large_pizza}.")
#     elif pep == 'Y':
#         large_pizza = large_pizza+large_med_pepperoni
#         print(f"Your final bill is: ${large_pizza}.")
#     else:
#         print(f"Your final bill is: ${large_pizza}.")

# if size == 'M':
#     if pep == 'Y' and cheese == 'Y':
#         medium_pizza = medium_pizza+large_med_pepperoni+ex_cheese
#         print(f"Your final bill is: ${medium_pizza}.")
#     elif cheese == 'Y':
#         medium_pizza = medium_pizza+ex_cheese
#         print(f"Your final bill is: ${medium_pizza}.")
#     elif pep == 'Y':
#         medium_pizza = medium_pizza+large_med_pepperoni
#         print(f"Your final bill is: ${medium_pizza}.")
#     else:
#         print(f"Your final bill is: ${medium_pizza}.")

# elif size == 'S':
#     if pep == 'Y' and cheese == 'Y':
#         small_pizza = small_pizza+small_pepperoni+ex_cheese
#         print(f"Your final bill is: ${small_pizza}.")
#     elif cheese == 'Y':
#         small_pizza = small_pizza+ex_cheese
#         print(f"Your final bill is: ${small_pizza}.")
#     elif pep == 'Y':
#         small_pizza = small_pizza+small_pepperoni
#         print(f"Your final bill is: ${small_pizza}.")
#     else:
#         print(f"Your final bill is: ${small_pizza}.")

# CODE 2
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill=0
# if size == 'S':
#     bill+=15
# elif size == 'M':
#     bill+=20
# elif size == 'L':
#     bill+=25

# if add_pepperoni== 'Y':
#     if size == 'S':
#         bill+=2
#     else:
#         bill+=3

# if extra_cheese == 'Y':
#     bill+=1
# print(f"Your final bill is ${bill}")


# # LOVE CALCULATOR
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_names=name1+name2
# combined_lower_case=combined_names.lower()
# t=combined_lower_case.count('t')
# r=combined_lower_case.count('r')
# u=combined_lower_case.count('u')
# e=combined_lower_case.count('e')

# l=combined_lower_case.count('l')
# o=combined_lower_case.count('o')
# v=combined_lower_case.count('v')
# e=combined_lower_case.count('e')

# col1=t+r+u+e
# col2=l+o+v+e


# score= int(str(col1)+str(col2))
# print(score)

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score > 40 and score < 50 :
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")



# TREASURE ISLAND GAME
print(''' 
                         +---------------------------+
                       +-|      TREASURE  ISLAND     |-+
                       | |            w e s        | |
                         | +-----------------------+ |
                           \__\                 /__/
                        ''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
move_init = input(
    "You are at a cross road. Where do you want to go. Type 'left' or 'right'. ").lower()
if move_init == 'left':
    # Game Continues...
    ship_init = input(
        "You arrive at a dock and the next ship arrives in 3 hours. Type 'swim' or 'wait'. ").lower()
    if ship_init == 'wait':
        # Game Continues...
        print("The ship docks at the next island's dock and you find an old man who gives you directions to where a castle with treasure is.")
        door_init = input(
            "The castle has three coloured doors. Choose a door to enter and get the treasure. Type 'red', 'yellow' or 'blue'.").lower()
        if door_init == 'yellow':
            # Game Continues...
            print("You Win!! The treasure is all yours.")
        elif door_init == 'blue':
            # Game Ends...
            print("You have been eaten by beasts!Oops..Game Over : ( ")
        elif door_init == 'red':
            # Game Ends...
            print("You have been burnt by fire!Oops..Game Over : ( ")
        else:
            # Game Ends...
            print("Game Over!!")
    else:
        # Game Ends...
        print("You have been attacked by trout. Game Over!!")
else:
    # Game Ends...
    print("You fell into a hole. Game Over!!!")
