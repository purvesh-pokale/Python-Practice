
s = "i am 25 years old my salary is 58000"
num = 0

for ch in s:
    if ch.isdigit():
        num = num + int(ch)
print(num)