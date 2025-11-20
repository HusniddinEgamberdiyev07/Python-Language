# -- F-stirng --
# We use f string to add mathematical expressions inside a text

# num1 = 10
# num2 = 20
# print(f"the sum of {num1} and {num2} is {num1+num2}")

# student = {
#     "name":"Galety",
#     "grades" : {
#         "Math":10,
#         "Physics":10,
#         "PSPP":10
#     },
#     "department":"Bs in Cs"
# }

# print(f"My name is {student["name"]}, I am studying {student["department"]}, My grades are math={student['grades']['Math']}, pspp={student['grades']['PSPP']}, physics={student['grades']['Physics']}, total={student['grades']['Math']+student['grades']['Physics']+student['grades']['PSPP']}")



# Exchanging values
# If we want to exchange value we need third variable

# num1 = 10
# num2 = 20
# num3 = 30
# num3 = num1
# num1 = num2
# num2 = num3

# print(f"{num1} num1")
# print(f"{num2} num2")

# num1, num2, num3 = num3, num1, num2
# print(f"{num1} num1")
# print(f"{num2} num2")
# print(f"{num3} num2")


# word = input("Enter a word: ")
# vowels="1234567890"
# hasVowel = False

# for char in word.lower():
#     if char in vowels:
#         hasVowel = True
#         break

# if hasVowel:
#     print("Has")
# else:
#     print("Has not")

# for char in word.lower():
#     if char in vowels:
#         hasVowel = True
#         break

# if hasVowel:
#     print("Has")
# else:
#     print("Has not")


C=40
F=(C*9/5)+32
print(F)

k=10
m=k*0.621371
print(m)

base=10
height=6
area=1/2*base*height
print(area)

year=2028
if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")