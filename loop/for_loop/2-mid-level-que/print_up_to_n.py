#Print natural number up to n  in frward and reverse order.

n = int(input("Enter the number :"))

for i in range(1,n+1):
    print(i)

'''
o/p

Enter the number :5
1
2
3
4
5

'''


n = int(input("Enter the number :"))

for i in range(n,-1,-1):
    print(i)


'''
o/p
Enter the number :5
5
4
3
2
1
0
'''