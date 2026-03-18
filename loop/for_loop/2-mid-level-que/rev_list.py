#Print a list of numbers in reverse order using a loop.
list1=[20,30,40,50,60]
list2=[]
for i in list1:
    list2=[i]+list2

print("Reverse order list :",list2)
'''
o/p
Reverse order list : [60, 50, 40, 30, 20]
'''
