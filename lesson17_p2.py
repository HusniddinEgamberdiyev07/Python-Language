# User input
# Without input our programms will return same result every time
# Basic entering values a = 10
# You can ask the values in the run time with python with input function
# input will create textbox
# All data will be str

# a = input("Enter a number: ")
# b = input("Enter b number: ")
# print(type(a), a)
# print(type(b), b)
# a = int(a)
# b = int(b)
# print(type(a), a)
# print(type(b), b)
# c = a + b
# print(c)

list1 = "2 - 3".split(" ")
print(list1)

for i in list1:
    if i == "+":
        print("add")
    if i == "-":
        print("minus")