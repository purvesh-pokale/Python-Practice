#Create a new list without duplicates using loop

data = [10, 20, 10, 30, 20, 40]
lst=[]

for i in data:
    if i not in lst:
        lst.append(i)

print("List without duplicates =",lst)

'''
o/p
List without duplicates = [10, 20, 30, 40]
'''