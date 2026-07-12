 #Create a random number guessing game with python.

import random

n = random.randint(1,10)

guess = int(input("Please guess your number between 1 and 10 :"))

if n == guess:
    print("you are right")

else:
    print("sorry your guess is wrong.")

print("The number is ",n)

'''
Please guss your number between 1 and 10 :5
you are right
The number is  5

'''


#tell the how many tries you take to guess
import random

n = random.randint(1,10)


tries = 0

while True:
    guess = int(input("Please guess your number between 1 and 10 :"))

    if n == guess:
        tries +=1
        print(f"Your are right you guessed the number is {tries} tries")
        break

    elif  n < guess :
        print("Please go lower.")
        tries +=1
    
    elif  n < guess :
        print("Please go higher.")
        tries +=1

    else:
        print("sorry your guess is wrong.")
        tries +=1


'''
o/p
Please guess your number between 1 and 10 :8
you are right
Your are right you guessed the number is 1 tries


Please guess your number between 1 and 10 :6
Please go lower.
Please guess your number between 1 and 10 :5
Your are right you guessed the number is 2 tries
'''