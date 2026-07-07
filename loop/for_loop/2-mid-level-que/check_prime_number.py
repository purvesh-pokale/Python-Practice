# check your number is prime or not

n = int(input("Check your number is prime or not :"))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count += 1

if count == 2:
    print("your number is prime.")
else:
    print("Your number is not prime.")

'''
o/p:
Check your number is prime or not :5
your number is prime.


Check your number is prime or not :6
Your number is not prime.
'''