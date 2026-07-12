#Separate each digit of a number and print it on the new line.


a = int(input("Tell your number : "))

while a > 0:
    print(a % 10)
    a = a // 10

'''
Tell your number : 937528
8
2
5
7
3
9
'''