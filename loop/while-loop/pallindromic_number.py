'''Accept a number and check if it is a pallindromic number (If
number and its reverse are equal)'''

a = int(input("Enter the number to check pallindrom :"))

rev = 0

copy = a

while a > 0:
    rev = rev*10 + a% 10
    a = a // 10

if copy == rev:
    print("Number is Pallindrom")
else :
    print("Number is not Pallindrom")

'''
Enter the number to check pallindrom :121
Number is Pallindrom

Enter the number to check pallindrom :5764
Number is not Pallindrom
'''