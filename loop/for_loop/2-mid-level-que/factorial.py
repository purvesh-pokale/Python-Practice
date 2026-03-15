#. Print factorial of a number using for loop. 
num=int(input("Enter the number :"))

pro=1
for i in range (1,num+1):
    
    pro= pro*i

print(f"factorial of {num} is {pro}")

'''
o/p

Enter the number :5
factorial of 5 is 120
'''