n=int(input())
print("Enter n")
m=int(input())
print("Enter m")
print(f"The multiplication table of {n} is")
for i in range(1,m+1):
    print(f"{i}*{n}={i*n}")