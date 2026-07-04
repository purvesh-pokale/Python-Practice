'''
Q2. Accept the gender from the user as char and print the
respective greeting message
Ex - Good morning sir (on the basis of gender)
'''
gen = input("Enter the gender :")

if gen ==  "male" or gen ==  "Male" or  gen == "M" or gen == "m":
    print("Good morning sir")
elif gen == "female" or gen ==  "Female" or gen ==  "F" or gen == "f":
    print("Good morning mam")
else:
    print("Unidentified gender")

    