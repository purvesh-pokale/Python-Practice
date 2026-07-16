s = "My mom is fine"

s1 = s.split()


for i in s1:
    
    rev = ""
    for j in i:
        rev = j + rev
    if rev == i:
        print(i)


s =" I am 25 year old my salary is 58000"

sum= 0

for i in s:
    if i.isdigit():
        sum = sum+int(i)

print(sum)
         
        

    



