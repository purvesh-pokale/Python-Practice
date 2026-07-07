#Reverse the string without using in build function

str = input("Enter the string :")

b = ""

for i in range(len(str)-1,-1,-1):
    b = b + str[i]  # i is the index number ,str[i] access the char  

print(b)

'''
o/p

hsevrup
'''