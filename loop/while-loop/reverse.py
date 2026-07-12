#Accept a number and print its reverse.
a = int(input("Enter the number :"))

rev = 0

while a>0:
    rev = rev* 10 + a % 10
    a = a // 10

print("Reverse of the given number is :",rev)


'''
Enter the number :273846
Reverse of the given number is : 648372
'''