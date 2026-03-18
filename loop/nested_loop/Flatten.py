#Flatten a nested list [[1,2],[3,4],[5,6]] using nested loops.
list1 = [[1,2],[3,4],[5,6]]
for i in list1:
    for j in i:
        print(j)

'''
o/p
1
2
3
4
5
6
'''