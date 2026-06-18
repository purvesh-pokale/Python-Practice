'''
Q2. Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender)
'''
gen=input("Please tell your gender :")

if gen == "M" or "m" or "male":
    print("Good Morning Sir")
elif gen == "F" or "f" or "female":
    print("Good morning mam")
else:
    print("Unidentified gender")
    