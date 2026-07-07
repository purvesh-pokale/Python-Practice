#print all the factors of the number

num = int(input("Enter the number :"))

print(f"Factors of the {num} :")
for i in range(1,num+1):
    if num % i == 0:
        print(i)

'''
o/p

Enter the number :87
Factors of the 87 :
1
3
29
87
'''