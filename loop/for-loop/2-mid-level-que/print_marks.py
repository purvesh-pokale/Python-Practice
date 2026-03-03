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
