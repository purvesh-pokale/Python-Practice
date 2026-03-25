'''
print
*
* *
* * *
* * * *
* * * * *
'''

for r in range(1,6):
#we print coloum here so we have to take no. of row equal to no. of star
    for c in range(1,r+1):  
        print("*",end=" ")

    print()

'''
When r = 1 → inner loop runs 1 time → *
When r = 2 → inner loop runs 2 times → * *
When r = 3 → inner loop runs 3 times → * * *
'''