
# Write a program to count occurrence of each character in the word "programing"
# input : "programing"
# Expected output
'''
p : 1
r : 2
o : 1
g : 2
a : 1
m : 1
i : 1
n : 1
'''

word = "programing"

char_count ={}

for i in word:
    if i in char_count:
        char_count[i] +=1

    else:
        char_count [i] = 1

for char, count in char_count.items():
    print(char , ":" , count)

'''
o/p
p : 1
r : 2
o : 1
g : 2
a : 1
m : 1
i : 1
n : 1
'''