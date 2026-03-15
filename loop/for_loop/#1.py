#1. DIsplay HI 5 times

for i in range(1,6):
    print("HI")

print()
'''
o/p
HI
HI
HI
HI
HI
'''
#2. print the multiplication table of 5
for i in range(1,11):
    print(f"{i}x5={i*5}")
print()
'''
1x5=5
2x5=10
3x5=15
4x5=20
5x5=25
6x5=30
7x5=35
8x5=40
9x5=45
10x5=50
'''
#3. find the sum of the first 10 natural number
sum=0
for i in range (1,11):
    n=sum
    sum = sum + i
    print(f"{i}+{n}={sum}")
print()
'''
o/p
1+0=1
2+1=3
3+3=6
4+6=10
5+10=15
6+15=21
7+21=28
8+28=36
9+36=45
10+45=55
'''
sum=0
for i in range (1,11):
    sum = sum + i
print(sum)
print()
'''
o/p
55
'''

#4. find the factorial of a given munber.
#ex. 5!=1x2x3x4x120

fact=1
for i in range(1,6):
    fact = fact*i
print(fact)
print()

'''
o/p
120
'''

#5. calculate the sum of even number from 1 to 50

sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i
print(sum)
print()

#6. print number from 1 to 10 along with their double(eg., 1->2,2->4)

for i in range(1,11):
    print(f"{i}={i*2}")
print()

#7. Print all numbers from 10 to 1 (reverse order). 

for i in range(10,0,-1):
    print(i)

print()
'''
o/p
10
9
8
7
6
5
4
3
2
1
'''

#8. Print all elements of a given list. 
lst=[1,2,3,4,5]

for i in lst:
    print(i)
print()
'''
o/p
1
2
3
4
5
'''

#9. Print the reverse of a string using a for loop. 
str1="purvesh"

for i in str1[::-1]:
    print(i)
print()


