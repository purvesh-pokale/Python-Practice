#write a program to calculate 3 to the power 4
#and take the base value and exponent from user

n = int(input("Enter the Base value :"))
m = int(input("Enter the exponent value :"))
result=1
i=1

while i<=m:
    result*=n

    i+=1

print(f"{n} power of {m} equal to {result}.")

'''
o/p
Enter the Base value :5
Enter the exponent value :9
5 power of 9 equal to 1953125.
'''