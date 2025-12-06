# nums = [1, 2, 3, 4, 5, 6, 7]
# for num in nums:
#     print(num)

# for i in range(0, len(nums), 1):
#     print(nums[i])

# print(nums[len(nums) - 1])

# i = 0
# while i < len(nums):
#     print("index "+str(i))
#     print(nums[i])
#     i += 1
#     print("index "+str(i))

# do while action bulyotganida tekshiradi

# name = "Husniddin"
# i = 1
# while i < 11:
#     print(name + str(i))
#     i += 1

# for i in range(1, 11):
#     print(name + " " + str(i))

# for num in range(1, 11):
#     print(num)

# for i in range(1, 11, 2):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i += 2

# j = 2
# while j < 11:
#     print(j)
#     j += 2

# a = [10, 20, 30, 40]
# b = [print(i) for i in a]
# print(b)
# print(len(b))
# c = [x for x in range(1, 11)]
# print(c)


# def check(fruit):
#     if "a" not in fruit:
#         return fruit


fruits = ["apple", "banana", "kiwi", "cherry", "mango", "kiwi"]
# a_fruits = [check(fruit) for fruit in fruits]
a_fruits = []

# print(a_fruits)

for fruit in fruits:
    if "a" not in fruit:
        a_fruits.append(fruit)

print(a_fruits)
