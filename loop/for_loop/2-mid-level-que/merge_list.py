#Merge two lists into one using a loop.
l1=[10,20,30,40]
l2=[50,60,70,80,90]
l3=[]

for i in l1:
    l3.append(i)

for j in l2:
        l3.append(j)

print(l3)

#by using while
l4=[]
i=0

while i< len(l1):
      l4.append(l1[i])   #in  while i is an work as index  not value
      i+=1

j=0
while j< len(l2):
      l4.append(l2[j])
      j+=1

print(l4)
'''
o/p
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''