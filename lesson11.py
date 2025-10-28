# y = [x for x in range(100, 1100, 100)]
# print(y)

# even nums
# y = [x for x in range(10) if x % 2 == 0]
# print(y)
# odd nums
# j = [x for x in range(10) if x % 2 != 0]
# print(j)
# squere of nums
# z = [x**2 for x in range(10)]
# print(z)

# makes items uppercase and adds to new list
# fruits = ["apple", "banana", "cherry", "mango"]
# new_list = [x.upper() for x in fruits]
# print(new_list)


# replace everthing with hello
# new_list2 = ["hello" for x in fruits]
# print(new_list2)

# new_list3 = [x if x != "banana" else "orange" for x in fruits]
# print(new_list3)

# asc - low to high | start to end
# des - high to low | end to start
# uppercase first lowercase second

# sorted = ["a", "A", "b", "B"]
# sorted.sort(reverse=True)
# print(sorted)

# sorted2 = ["a", "A", "b", "B"]
# sorted2.sort()
# print(sorted2)

# sorted_nums = [1, -1, 10, -9, 2, 4, 0, ]
# sorted_nums.sort()
# print(sorted_nums)


# sorted_nums2 = [1, -1, 10, -9, 2, 4, 0, ]
# sorted_nums2.sort(reverse=True)
# print(sorted_nums2)

# sorted3 = ["A", "c",  "b", "C", "B", "a"]
# sorted3.sort(key=str.lower)
# print(sorted3)


# iterable only

# a = [10, 20, 30]
# b = a.copy()
# print(b is a)
# print(b)

# b[1] = 25
# print(a)
# print(b)

# b = list(a)

# print(b)

# b = [1, 2, 3]
# + only same iterable element can join
# print(a + b)

# b.extend(a)
# print(b)

# 1.30 22th october