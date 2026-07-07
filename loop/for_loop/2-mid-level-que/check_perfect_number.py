'''
Accept a number and check if it a perfect number or not.
A number whose sum of factors is equal to the number itself

Ex - 6 = 1, 2, 3 = 6
'''

num = int(input("Enter the number :"))

sum = 0

for i in range(1,num):
    if num % i == 0:
       sum += i

if sum == num :
    print(f"{num} is a perfect number.")  
else :
    print(f"{num} is not a perfect number.")

'''
o/p
Enter the number :6
6 is a perfect number.

Enter the number :9
9 is not a perfect number.

Enter the number :28
28 is a perfect number.
'''