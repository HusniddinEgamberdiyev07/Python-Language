import random
# if condition:
#   true statement
# elif condition
#   true statement
# else
#   false statement

# simple if
# if condition:
#   true statement
# else:
#   false statement

# short hand if
# if condition: code 

num1 = 100
num2 = 10
# if num1 > num2: print(f"{num1} is greater than {num2}")

# true statement if condition else false statement
# print(f"A) {num1} is greater than {num2}") if num1 > num2 else print(f"B) {num2} is greater than {num1}")

# if num1 > num2:
#     print("Num1")
# elif num2 > num1:
#     print("Num2")
# else:
#     print("=")


# true statement if condition else true statement if condition else false statement

def printNum(big, small, letter):
    print(f"{letter}) {big} is greater than {small}") 

printNum(num1, num2, "A") if num1 > num2 else print("=") if num1 == num2 else printNum(num2, num1, "B")

# we can use and, or, not in conditions
# condition1 and condition2

job=True
age=17
# if job and age>=18:
#     print("Marry")
# else:
#     print("Wait")

# print("Marry") if age>=18 and job else print("Wait")
# print("Marry") if age>=18 or job else print("Wait")

# nested if->if inside another if

first_y = False
second_y = False
third_y = False
fourth_y = False
if first_y:
    print("First")

    if second_y:
        print("Second")

        if third_y:
            print("Third")

            if fourth_y:
                print("Fourth")
                print("Graduated")
else:
    print("Fail")


if num1 > num2:
    print("A")

if num1 > num2:
    pass

print("Hello World")

