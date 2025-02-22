# To check a greatest number
a=int(input("enter a number a:")) 
b=int(input("enter a number b:")) 
c=int(input("enter a number c:")) 
if a>b:
    print("A is greater number")
elif b>c:
    print("B is greater number")
else:
    print("C is greater number")

# # check if a year is leap or not:

year = int(input("Enter a year to check leap or not"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
    print(f"{year} is a Leap Year")
else: 
    print(f"{year} is not a Leap Year")


# # grade of a student based on the marks they score:

marks = int(input("Enter marks"))
if marks >= 80 and marks <=100:
    print("Grade A")
elif marks >= 70 and marks <=89:
    print("Grade B")
elif marks >= 60 and marks <=79:
    print("Grade C")
elif marks < 60:
    print("Fail")
else:
    print("Not a number")


# # program to check if three sides length form a valid triangle:

a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("It will form a valid triangle")
else:
    print("It will not form a valid triangle")