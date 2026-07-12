 #Create a random number guessing game with python.

import random

n = random.randint(1,10)

guess = int(input("Please guss your number between 1 and 10 :"))

if n == guess:
    print("you are right")

else:
    print("sorry your guess is wrong.")

print("The number is ",n)

'''
Please guss your number between 1 and 10 :5
you are right
The number is  5

Please guss your number between 1 and 10 :8
sorry your guess is wrong.
The number is  1
'''