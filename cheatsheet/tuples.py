# 📔 Tuples

# Immutable: items cannot be changed.
# Ordered: maintains the order which items are added.
# Index based: items are accessed using their position. (starting from 0 or -1)
# Can store mixed data types.



# 📖 Creating a tuple.

# 1) Using round brackets.

fruits = ("apple", "orange", "banana")

print(fruits)

# 2) Using tuple() constructor.

letters = tuple("Hello World")
print(letters)      # -> ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

# 3) Without Parentheses
# Python will automatically create tuples when you separate multiple values with commas.

nums = 1, 2, 3
print(nums)
print(type(nums))


# 📖 Accessing tuple elements.

# Elements in a tuple are accessed using indexes.
# Positive indexes starts with 0. Add 1.
# Negative indexes starts with -1. Add -1.

#        0  1  2  3
nums2 = (1, 2, 3, 4)
#       -4 -3 -2 -1

print(nums2[3])         # -> 4.
print(nums2[-3])        # -> 2.
print(nums2[1:3])       # -> (2, 3). Elements from 1 to 3.



# 📖 Concatenation of tuples.

# + operator can combine tuples.

tuple1 = (1, 2, 3)
tuple2 = ("hi", "bye", "die")
tuple3 = tuple1 + tuple2

print(tuple3)



# 📖 Deleting tuple.

del tuple3
# print(tuple3) -> Error



# Tuple unpacking.

tuple3 = (1, 2, 3)
num1, num2, num3 = tuple3

print(num1, num2, num3)

tuple4 = (1, 2, 3, 4, 5)

a, b, *c = tuple4         # a=1, b=2, c=[3,4,5]  -> first two assigned, rest goes to c
a2, *b2, c2 = tuple4      # a2=1, b2=[2,3,4], c2=5 -> first to a2, last to c2, middle to b2
*a3, b3, c3 = tuple4      # a3=[1,2,3], b3=4, c3=5 -> last two assigned, rest to a3

print(a, b, c)
print(a2, b2, c2)
print(a3, b3, c3)