# write a program to reverse each word in the sentance using while loop

s = input("Enter the sentance :")

words = s.split()

# if I enter purvesh pokale
#['purvesh' , 'pokale']
# i=purvesh

for i in words:
    l = len(i) - 1      # lenth of word to apply the indexing

    while l>=0:
        print(i[l], end= " ")   #print the char i[4] means last element

        l -= 1                  #ex l= 4 here l=4-1=>3 , l=3-1=>2 ....
    
'''
o/p
Enter the sentance :purvesh pokale
h s e v r u p e l a k o p 
'''



