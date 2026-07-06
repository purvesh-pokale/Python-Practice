'''
If- elif ladder
. You cna also create if elif ladder using multiple conditions of
elif.
. For understanding solve this question
. take the input of temperature in celsius.
. Below 0C - "Freezing Cold
. 0C to 10C - "Very Cold
. 10C to 20℃ - "Cold
. 20C to 30C - "Pleasant
. 30C to 40C - "Hot
. Above 40C - "Very Hot 
'''
temp = int(input("Enter the Temperature :"))
if temp<=0:
    print("Freezing Cold")
elif temp>0 and temp<=10:
    print("very Cold")
elif temp>10 and temp<20:
    print("Cold")
elif temp>20 and temp<=30:
    print("Pleasant")
elif temp>30 and temp<=40:
    print("Hot")
elif temp>40:
    print("Very Hot")

'''
o/p
Enter the Temperature :0
Freezing Cold

Enter the Temperature :6
very Cold

Enter the Temperature :16
Cold

Enter the Temperature :26
Pleasant

Enter the Temperature :46
Very Hot
'''