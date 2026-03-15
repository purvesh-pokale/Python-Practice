# Count the number of vowels in a string. 

s=input("Enter the string :")
count=0
for i in s :
    
    if i in "aeiouAEIOU":
        count=count+1

print(count)

'''
o/p

Enter the string :purvesh
2
'''

