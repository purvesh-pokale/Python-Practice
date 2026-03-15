'''
The Goal: Calculate a total based on a condition.
The Task: Imagine you are a teacher. You have a list of student marks: [55, 80, 40, 95, 30, 70].
Write a loop that calculates the sum of only the marks that are 50 or above (the passing marks).
'''
marks= [55, 80, 40, 95, 30, 70]

sum=0

for i in marks:
    
    if i>=50:
        sum = sum +i

print(f"sum of marks that are 50 or above is {sum}.")

'''
o/p
sum of marks that are 50 or above is 300.
'''

#Task 2.
'''
Count how many students passed (>= 50)

Count how many failed

Find total marks of passed students
'''
marks= [55, 80, 40, 95, 30, 70]

sum=0
count=0
count1=0
for i in marks:
    
    if i>=50:
        sum = sum +i
        count+=1
    elif i<50:
        count1+=1

print("total student pass =",count)
print(f"sum of marks of passed student is {sum}.")
print("total studen fail =",count1)

'''
o/p
total student pass = 4
sum of marks of passed student is 300.
total studen fail = 2
'''
