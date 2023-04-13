# Write a logic to implement a simple calculator
# capable of computing two numbers entered by user
# as input
# Make sure the program can compute with either of
# the four mathematical operations


number_1 = int(input("Enter your first number\n"))
number_2 = int(input("Enter your second number\n"))

operation = input("Enter an operation\n")

if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    print(number_1 / number_2)
else:
    print("You have typed a wrong sign")


# Create a function to ascertain that the user has / eMobilis/ as
# username and / eMobilis@123/ as password. Henceforth, proceed
# to calculate the bmi of the user and display the results of the
# bmi as either 1. Underweight , 2. normal weight ,3. Overweight
# or 4. Obese
# Note: All the data should be provided by the user as input.
# Use the scale below for the bmi:
#   0----18---- Underweight
#   18.1 ----29-- normal weight
#   29.1 ---- 34--- Overweight
#   34.1 and above ---- Obese

    import re

    username = input("Enter your username\n")
    while True:
        try:
            username = input('Enter your name:')
            validate = re.findall(r'eMobilis', username)
            if not validate:
                raise ValueError
            else:
                print('you are a eMobilis user', validate[0])
                break
        except ValueError:
            print('You are not eMobilis user!')

    user_password = input("Enter your password\n")
    while True:
        try:
            username = input('Enter your password:')
            validate = re.findall(r'eMobilis@123', user_password)
            if not validate:
                raise ValueError
            else:
                print('you are a eMobilis@123 user', validate[0])
                break
        except ValueError:
            print('You are not eMobilis@123 user!')

    weight = int(input("Enter your weight\n"))
    height = int(input("Enter your height in metres\n"))

    bmi = weight / pow(height, 2)

    if bmi <= 18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")


# Create a class called Hesabu to accept all the properties that are
# necessary to calculate both simple interest of a loan borrowed
# and volume of any cylinder.
# Implement the respective functions to calculate the volume of a
# cylinder and SI of a loan borrowed.
# Note: All data should come from the user as input

from hesabu import Hesabu

try:
    h_principle = input("Enter the principle amount\n")
    h_rate = input("Enter the rate\n")
    h_time = input("Enter the time taken\n")

    Hesabu.create(principle=h_principle, rate=h_rate, time=h_time)
    print("Your loan is calculated")
except:
    print("Please check your data")

interests = Hesabu.select()

for hesabu in interests:
    print(hesabu.principle,hesabu.rate,hesabu.time,hesabu.interest)

try:
    h_pi = input("Enter the pi\n")
    h_radius = input("Enter the radius\n")
    h_height = input("Enter the height\n")

    Hesabu.create(pi=h_pi, radius=h_radius, height=h_height)
    print("Your volume is calculated")
except:
    print("Please your data")

volumes = Hesabu.select()

for hesabu in volumes:
    print(hesabu.pi,hesabu.radius,hesabu.height,hesabu.volume)

