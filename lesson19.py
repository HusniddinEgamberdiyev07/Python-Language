# subject1 = int(input("Enter subject1 marks: "))
# subject2 = int(input("Enter subject2 marks: "))
# subject3 = int(input("Enter subject3 marks: "))

# total = subject1 + subject2 + subject3
# avg = total / 3

# if avg >= 90:
#     grade = "A+"
# elif avg >= 80:
#     grade = "A"
# elif avg >= 70:
#     grade = "B"
# elif avg >= 60:
#     grade = "C"
# else:
#     grade = "F"

# print(f"subject1 marks: {subject1}")
# print(f"subject2 marks: {subject2}")
# print(f"subject3 marks: {subject3}")

# print("total", total)
# print("avg", avg)

# print(f"Your grade is {grade}")


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to voting")
# else:
#     print("You are not eligible to voting")


number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
number3 = int(input("Enter a number2: "))

if number1 > number2 and number1 > number3:
    print(f"{number1} is greater than {number2} and {number3}")
elif number2 > number1 and number2 > number3:
    print(f"{number2} is greater than {number1} and {number3}")
elif number3 > number1 and number3 > number1:
    print(f"{number3} is greater than {number2} and {number1}")
else:
    print(f"All are equal")