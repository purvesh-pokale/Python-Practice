#write a program to count the number of consonants in word "learing" 

word = "learing"
count = 0

i = 0

while i < len(word):
    if word[i] not in "aeiouAEIOU": #it check by using indexing

        count+=1

    i+=1

print("Number of consonants in word :",count)

'''
o/p
Number of consonants in word : 4
'''