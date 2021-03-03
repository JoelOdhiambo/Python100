import random
# fruits={"Apple","Peach","Pear"}
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# Calculating the average height for students
# student_heights = input("Input a list of student heights ").split()
# sum=0
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# #   print(n)
#   sum=sum+student_heights[n]

# avg=int(round(sum/(n+1)))

# print(avg)

# Highest Score
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score=0
# for score in student_scores:
#     if score > highest_score:
#         highest_score=score
# print(f"The higest score in the class is {highest_score}")

# sum=0
# for number in range(1,101):
#     sum+=number
# print(sum)

# Sum of even numbers from 1 to 100
# sum=0
# for number in range(0,101,2):#0 to 2
#     sum+=number
# print(sum)

# The Fizz Buzz Problem
# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz") 
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number) 
   
# Password Generator
# letters,symbols,numbers,generate password,Thonny
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passwordElements=[]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for l in range(nr_letters):
    random.shuffle(letters)
    print(letters[l])
    passwordElements.append(letters[l])
print("\n")

for n in range(nr_numbers):
    random.shuffle(numbers)
    passwordElements.append(numbers[n])
    print(numbers[n])
print("\n")

for s in range(nr_symbols):
    random.shuffle(symbols)
    passwordElements.append(symbols[s])
    print(symbols[s])
print("\n")

random.shuffle(passwordElements)
for x in passwordElements:
    print (x)
# print("Here is your password: ")
