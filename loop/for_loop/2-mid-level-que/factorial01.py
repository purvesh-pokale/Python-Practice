#Print the factorial of a number

num = int(input("Enter the number :"))

pro = 1 

for i in range(1,num+1):
    pro = pro*i

print(f"the factorial of the {num} is {pro}")

'''
Enter the number :2
 the factorial of the 2 is 2

 Enter the number :3
 the factorial of the 3 is 6
'''