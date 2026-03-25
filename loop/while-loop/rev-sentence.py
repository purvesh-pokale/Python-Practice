# write a program to reverse each word in the sentance using while loop

s = input("Enter the sentance :")

words = s.split()

# if I enter purvesh pokale
#['purvesh' , 'pokale']
# i=purvesh

for i in words:
    l = len(i) - 1

    while l>=0:
        print(i[l], end= " ")

        l -= 1
    
'''
o/p
Enter the sentance :purvesh pokale
h s e v r u p e l a k o p 
'''



