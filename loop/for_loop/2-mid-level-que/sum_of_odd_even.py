'''
Print the sum of all even & odd numbers in a range
separately.
'''
num = int(input("Enter the number for range :"))

even_sum = 0
odd_sum = 0
for i in range(1,num+1):
    if i % 2 == 0:
        even_sum +=i
    else:
        odd_sum +=i

print(f"sum of all even number in range is {even_sum}")
print(f"sum of all odd number in range is {odd_sum}")

'''
o/p
Enter the number for range :10
sum of all even number in range is 30
sum of all odd number in range is 25
'''
