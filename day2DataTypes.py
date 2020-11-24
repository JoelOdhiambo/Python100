# num_char = len(input("What is your name? "))
# # type-cast num_char to a string
# new_num_char=str(num_char)
# print("Your name has " + new_num_char + " characters")
# calculate the sum of a two digit number
# two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
# print(int(two_digit_number[0])+int(two_digit_number[1]))

# BMI Calculator
# BMI=weight(kg)/height(m)
# height = input("Enter your height in meters: ")
# weight = input("Enter your weight in kilograms: ")
# print(int(float(height)))
# bmi = int(weight)/float(height)**2
# print(int(bmi))

# the round function
# print(round(8/3,4))

# print(14//3)
# result=4/2
# result/=2
# print(result)

# f-String
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}!!")

# age left in days, months and weeks calculator.
# Max age is 90
# x=365
# y=52
# z=12

# age=input("What is your age? ")

# integer_age=int(age)

# days_left=(90-integer_age)*x
# weeks_left=(90-integer_age)*y
# months_left=(90-integer_age)*z

# print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")


# Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to the Tip calculator. ")
bill=float(input("What was the total bill? "))
tip=input("What percentage tip would you like to give? 10, 12 or 15? ")
payers=input("How many people will split the bill? ")

bill_int=int(bill)
tip_int=int(tip)
payers_int=(int(payers))

bill_total=round(((bill_int/payers_int)*(1+(tip_int/100))),2)
message=f"Each person should pay ${bill_total}"

print(message)
