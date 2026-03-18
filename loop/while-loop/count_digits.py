#Count the number of digits in a number using a while loop.
n=83947
count=0
while n>0:
    r=n%10
    count=count+1
    n=n//10

print("number of digits in number :",count)

'''
o/p
number of digits in number : 5
'''
