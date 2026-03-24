#display number from 1-10

i = 1
while (i<=10):
    print(i)
    i+=1
print()

#display number from 10-1
i=10
while(i>=1):
    print(i,end=" ")
    i-=1

print()

#display number from 1 - 30 divisible by 3
i=1
while i<=30:
    if i%3==0:
        print(i)
    i+=1
print()

# print cubes of number from 1 to 5
i=1
while i<=5:
    print(f"{i} = {i**3}")

    i+=1

print()

#print Odd number from 1 to 10
i = 1
print("Odd number:")
while i<=10:
    if i%2 != 0:
        print(i)

    i+=1
print()

#Calculate the product of number from 1 to 5
num= int(input("Eter the number :"))
i=1
pro=1
while i<=num:
    pro*=i     #pro=pro*i

    i+=1

print(f"product of number from 1 to {num} is {pro}")

'''
o/p
Eter the number :12
479001600
'''














