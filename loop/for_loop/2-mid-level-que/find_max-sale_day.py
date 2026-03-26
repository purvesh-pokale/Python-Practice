'''
Problem: Find the Day With Maximum Sales

Problem Statement:

Given the sales of N days, print the day number (1-indexed) with the highest sales.


Detailed Description:
You need to loop through all the N sales values.
Maintain two variables:
    maxValue → stores the highest sales found so far
    maxIndex → stores the index (day) of that highest sales
For each value:
    If the current value is greater than maxValue, update both:
        maxValue
        maxIndex
After checking all values:

    Print the day number, which is:

    maxIndex + 1

(because indexing starts from 0, but days start from 1)


Input Format:
First line: Integer N (number of days)
Second line: N space-separated integers (sales values)

Output Format:
Print a single integer → day number with maximum sales

Input:

7
1200 1500 900 1800 1600 1400 1300

Output:

4
'''

n = int(input("Enter the number of days :"))

sales = [int(x) for x in input("Enter the sales value: ").split()]

maxvalue = sales[0]
maxindex = 0

for i  in range(n):
    if sales[i] > maxvalue:
        maxvalue=sales[i]
        maxindex = i

print("max sales on a day :",maxindex+1)

'''
o/p
Enter the number of days :7
Enter the sales value: 1000 400 1200 5000 1000 630 500
max sales on a day : 4
'''