

def avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

print(avg(5,5,5))

'''
o/p:
5.0
'''


#WAF to print the length of a list. ( list is the parameter)


cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

'''
0/p
6
4
'''

'''
def print_len(lst):
    print(len(lst))

a=input("Enter the list to find it's length :").split()

print_len(a)

o/p:
Enter the list to find it's length :65 34 5
3


'''

#WAF to print the elements of a list in a single line. ( list is the parameter)

def print_list(lst):
    for i in lst:
        print(i,end= " ")

print_list(cities)
print()

'''
o/p
delhi gurgaon noida pune mumbai chennai
'''

'''
#WAF to find the factorial of n. (n is the parameter)

def print_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    return(fact)

num = int(input("Enter the number to find factorial : "))

print(print_fact(num))

o/p:

Enter the number to find factorial : 4
24
'''

#WAF to convert USD to INR.


#WAR to check even odd number

def check_even_odd(n):
    if n % 2 == 0:
        print("Even number")

    else:
        print("Odd number")

num = int(input("Enter the number :"))

check_even_odd(num)

'''
o/p
Enter the number :33
Odd number

Enter the number :34
Even number
'''