#3.  Classify age into child (<13), teenager (13-19), or adult (20+).

age = int(input("Enter the age of person :"))

if age <13:
    print("Person is child.")
elif age >= 13 and age <=19:
    print("Person is teenager.")
else:
    print("Person is adult.")

'''
Enter the age of person :30
Person is adult.

Enter the age of person :15
Person is teenager.

Enter the age of person :10
Person is child.
'''