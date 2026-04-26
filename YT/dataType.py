#Numerical Data Type

a = 12
b = -12
print(type(a))
print(type(b))
'''
<class 'int'>
<class 'int'>

'''

c = 5.5
d = 12/3
print(type(c))
print(type(d))
'''
<class 'float'>
<class 'float'>
'''

e = 35j
f = 23+35j
print(type(e))
print(type(f))
'''
<class 'complex'>
<class 'complex'>
'''

st1 = '12345 dhndsodkn  #$&!~^*()'
st2 = "didns 2113  @%!&@^@"
print(type(st1))
print(type(st2))

'''
<class 'str'>
<class 'str'>
'''

#####################################################

#LIST 

marks = [24,35,42,44,23,37]
print(marks)
print(type(marks))
print(len(marks))
'''
[24, 35, 42, 44, 23, 37]
<class 'list'>
6
'''
#indexing
print(marks[1])
#o/p :- 35
print(marks[4])
#o/p :- 23

#negative indexing
print(marks[-1])
#o/p :- 37
print(marks[-4])
#o/p :- 42


#slicing
colours =["black","blue","red","yellow","pink","sky bule","white","orange","peach"]

print(colours[2:6])
#o/p :-['red', 'yellow', 'pink', 'sky bule']
print(colours[:4])
#o/p :-['black', 'blue', 'red', 'yellow']
print(colours[4:])
#o/p :-['pink', 'sky bule', 'white', 'orange', 'peach']

#reverse of list 
print(colours[:-1])
#o/p :- ['black', 'blue', 'red', 'yellow', 'pink', 'sky bule', 'white', 'orange']
print(colours[6:3:-1])
#o/p:- ['white', 'sky bule', 'pink']


#concatenation

l1 = [20,30,40]
l2 = [50,60,70]

print("concat_list",l1+l2)
#o/p :- concat_list [20, 30, 40, 50, 60, 70]

concat_list =l1+[50,60,70,80]
print("concat_list",concat_list)
#o/p :- concat_list [20, 30, 40, 50, 60, 70, 80]

print("concat_list :",[20,30,40]+[50,60,70])
#o/p :- concat_list [20, 30, 40, 50, 60, 70]

#list is mutable data type 
#we modify by using indexing

colours =["black","blue","red","yellow","pink"]
colours[1]="white"
print(colours)
#o/p :- ['black', 'white', 'red', 'yellow', 'pink']

#modify by slicing
colours[2:4]=["white","peach"]
print(colours)
#o/p :- ['black', 'white', 'white', 'peach', 'pink']

#Mutable 
#modify using indexing
l1 = [10,20,30,40,50]
l1[2]=3
print(l1)

l1[1:4]=[2,3,4]
print(l1)

# Nested list
l2 = [10,20,30,[40,50],60,70,[80,90,[100,110]]]
#print 80,70,100

print(l2[6][0])    #80
print(l2[5])       #70
print(l2[6][2][0]) #100


#Method of list
#.append() : add single elemeant in the last of the elemaent
names =["purvesh","shrushti","om","aman"]
names.append("hari")
print(names)

#.extend() : add list to another list 
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1.extend(l2)
print(l1)

#.insert(): adds element at specific position
num =[1,2,4,5,6]
num.insert(2,3)
print(num)

#clear(): empties the list
num =[1,2,3,4,5]
num.clear()
print(num)

#pop(): deletes element by index value
colours =["black","blue","red","yellow","pink"]
colours.pop(3)
print(colours)

# remove() : deletes elements by giving element itself
colours.remove("red")
print(colours)
print("-"*50)

############################################################################


#String:-

char = 'a'
print(char)
print(type(char))

word = "purvesh"
print(word)
print(len(word))

word2 = "I am from Amravati"
print(word2)
print(len(word2))

#Accessing using indexing & slicing

#indexing
word = "New York"
print(word[4])

#slicing
print(word[2:6])  #o/p: w Yo

#step slicing
print(word[::2])  #o/p: NwYr

#String is immutable

#Concatenation: joining of string
first_name = "Purvesh"
last_name = "Pokale"

full_name = first_name + " " + last_name
print(full_name)


#Method of String

#case conversion
#.lower()
country = "INDIA"
print(country.lower())

#.upper()
country = "india"
print(country.upper())

#.capitalize()
country = "india"
print(country.capitalize())


#countent checker
#.isapha()
s = "purvesh"
print(s.isalpha())

#.isdigit()
s2= "2003"
print(s2.isdigit())

#.isalnum() :combination of both not allows spical character
s3 = "purvesh2003"
print(s3.isalnum())


#.split() : it returns list of subtring according to the separato provided
#syntax : .split(sep =" ")  by default split takes space as separetor if we dident put any thinf in " " this
#         .split()

data = "Hello all I live in Pune"
print(data.split())

info = "hello, my, name, is. purvesh"
print(info.split(sep=","))

#.join()
data =["hello","all","good","afternoon"]
print("-".join(data))