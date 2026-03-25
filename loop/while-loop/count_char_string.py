#write the program to count occurrences of the character "s" in the string "success"

s = input("Enter a string :")
n = input("Enter the char you want to count :")
i=0
count = 0

while i < len(s):
    if s[i] == n:  #it takes each element by using indexing
        count +=1

    i += 1
    
print(f"{n} = {count}")

'''
o/p
Enter a string :success
Enter the char you want to count :s
s = 3
'''

