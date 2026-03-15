
#18. Print Fibonacci series up to 10 terms using for loop. 

a=0
b=1
print(a)
print(b)
for i in range(1,11):

    c=a+b
    print(c)
    a,b=b,c

'''
o/p
0
1
1
2
3
5
8
13
21
34
55
89
'''