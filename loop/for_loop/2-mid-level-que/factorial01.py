#Print the factorial of a number

num = int(input("Enter the number :"))

fact = 1 

for i in range(1,num+1):
    fact = fact*i

print(f"the factorial of the {num} is {fact}")

'''
Enter the number :2
 the factorial of the 2 is 2

 Enter the number :3
 the factorial of the 3 is 6

 Enter the number :4
the factorial of the 4 is 24
'''