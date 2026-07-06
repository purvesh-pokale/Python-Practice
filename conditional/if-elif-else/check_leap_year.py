'''
Q5. Accept a year and check if it a leap year or not (google to
find out what is a leap year)
'''

year = int(input("Enter the your Year : "))

if year % 100 == 0 or year % 400 == 0:
    print("Its leap Year.")
elif year % 100 != 0 and year % 4 == 0:
    print("Its leap Year.")
else:
    print("Its oidrnary year.")

'''
o/p:
Enter the your Year : 1874
Its oidrnary year.

Enter the your Year : 1992
Its leap Year.

Enter the your Year : 2000
Its leap Year.S
'''