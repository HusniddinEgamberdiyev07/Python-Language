# in and not in are membership operator

# >> code
# students = ["Sardor", "Husniddin"]
# print("Husniddin" in students)
# print("Jo'rabek" in students)
# print("Jo'rabek" not in students)
# print("Husniddin" not in students)
# << code

# datastructure is arranging data in an order.
# It will be easy to access the data.
# It has two types
# Primitive and non primitive data structure
# Linear and non linear data structure
# primitive data structure can store only one value
# non primitive data structure can store only multiple values
# list, tuple, set, dictionaries

# lest createion syntax:
# variable name = [entry1, entry2]
# list is changeable
# allows duplicate values
# we can store multiple type of values in one list

# >> code
# fruits = ["Apple", "Orange", "Banana"]
# numbers = [1, 4, 5, 3, 6, 1]
# print(type(fruits))
# print(numbers)
# print(len(numbers))
# print(numbers[0])
student = ["Husniddin", "Freshman in CS", 10, 30, 25, True]
# nums = [10, 20, 30, 40, 50]
# nums[1] = 25
# nums[2] = 35
# nums[3] = 45
# print(nums)
# nums[1:4] = [25, 35, 45]
# print(nums)

# print(student[0])
# print(student[2])
# print(student[-6])
# print(student[2:5])
# print(student[-4:-1])
# print(student[:2])
# print(student[2:])
# if "Husniddin" in student:
#     print("Husniddin is there")
# else:
#     print("Husniddin is not there")

# print(student)
# student[2] = "muhaaaaa"
# y = student
# print(y)
i = 0
new_list = []
while i < len(student):
    i += 1
    if student[i] == 10:
        newListS = student[: i + 1]
        newListE = student[i + 1:]
        newListS.append(25)
        newListS.extend(newListE)
        new_list = newListS
        break
print(new_list)
# << code
