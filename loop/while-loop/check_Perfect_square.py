# write a program to check if a given number is a perfect square or not

num=int(input("Enter a number to check :"))

i=1
is_perfect_square = False

while i*i <=num:
    if i * i == num:
        is_perfect_square = True
        break

    i+=1

if is_perfect_square:
    print(f"{num} is a perfect square.")

else:
    print(f"{num} is not a perfect square.")

'''
o/p
Enter a number to check :16
16 is a perfect square.

Enter a number to check :94
94 is not a perfect square.
'''