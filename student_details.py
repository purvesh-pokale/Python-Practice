'''
Question:

Write a program to print the details of a student. The student's details consist of his/her name, age, CGPA, and grade.

Input Format

The input consists of one string, one integer, one float, and one character. The string corresponds to the name of a student. The integer corresponds to the age of a student. The float corresponds to the CGPA of a student. The character corresponds to the grade of a student.

Constraints

The CGPA (float value) should be printed with 2 decimal places.

Output Format

The output prints all the details of a student. Refer to the sample Output.

Sample Input 0

Rajeev
20
8.6467
B
Sample Output 0

Name: Rajeev
Age: 20
CGPA: 8.64
Grade: B
Sample Input 1

Meera
18
9.123
A
Sample Output 1

Name: Meera
Age: 18
CGPA: 9.12
Grade: A
'''
name=input()
age = int(input())
cgpa = float(input())
grade = input()

cgpa = int(cgpa * 100) / 100  #is used to truncate a floating-point number to 2 decimal places (cut extra digits withoutrounding).
                              #ex.cgpa = 8.4679 [first->8.4679x100=846.79]
                              #                 [second-> int converte 846.79 in to 846]
                              #                 [third-> 846/100=8.46]

print("Name:",name)
print("Age:",age)
print(f"CGPA: {cgpa:.2f}")
print("Grade:",grade)

'''
o/p
purvesh
21
8.946
A+
Name: purvesh
Age: 21
CGPA: 8.94
Grade: A+
'''