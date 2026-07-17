str1=input("Enter the string to check palindrome :")
def pal(s):
    if s[:]==s[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome. ")
    return s

pal1=pal(str1)


str1=input("Enter the string to check palindrome :")
pal = lambda s :"string is palindrome" if s[:]==s[::-1] else "string is not palindrome. "
print(pal(str1))

num=int(input("Enter the number to check it is even or odd :"))
check_even_odd =lambda n : f"{n} is a even number" if n%2==0 else f"{n} is a odd number"
print(check_even_odd(num))