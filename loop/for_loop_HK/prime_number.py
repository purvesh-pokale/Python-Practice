'''
A prime number is divisible only by 1 and itself. You are given a positive integer. Write an algorithm to find all the prime numbers from 2 to the given positive number

Input Format

The input consists of an integer.

Constraints

1 < n< 109

Output Format

Print space-separated integers representing the prime numbers till the given positive number.

Sample Input 0

11
Sample Output 0

2 3 5 7 11
Explanation 0

For the given number the list of special numbers is [2, 3, 5, 7, 11]

Sample Input 1

30
Sample Output 1

2 3 5 7 11 13 17 19 23 29
Explanation 1

For the given number the list of special numbers is [2,3, 5, 7, 11, 13, 17, 19, 23, 29]
'''

n = int(input("Enter the number:"))

for num in range(2, n + 1):
    prime = True
    
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        print(num, end=" ")

'''
o/p
Enter the number:11
2 3 5 7 11
'''