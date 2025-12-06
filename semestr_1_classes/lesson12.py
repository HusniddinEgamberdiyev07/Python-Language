# data structures:
# list  -> is a collection which is ordered and changeable.Create with []
# tuple -> is a collection which is ordered and unchangeable.Create with ()
# why ordered if I enter ["apple", "banana", "oragnge"] it will give output ["apple", "banana", "oragnge"]
# set
# dictionry
# They can store multiple values

fruits = ("Apple", "Banana", "Orange")
print(type(fruits))

# Tuple also allows duplicate items
nums = [1, 2, 3, 1] 
print(nums)
t_nums = (1, 2, 3, 1)
print(t_nums)

# Tuple itesm indexed. It starts from 0.
# (1, 2, 3, 1) -> tuple
#  0  1  2  3  -> indexes
print(t_nums[0])
print(t_nums[2])

# tuples are unchangeable. We can't add, remove or change items.

nums2 = [10, 20, 30]
nums2[1] = 50
print(nums2)

t_nums2 = (10, 20, 30)
# t_nums2[1] = 50 -> error

print(len(nums2))

# create a tuple with only one item but you have to put comma.
tuple1 = (1)
print(tuple1)
print(type(tuple1))     # -> type int

tuple2 = ("Apple", )
print(type(tuple2))     # -> type tuple

# Can have differant types of elemnets
tuple3 = ("Hello", 1.2, 10, True, [1, 2, 3])
tuple3[4][0] = "heheheh"
print(tuple3)

# tuple constructor
tuple_c = tuple(tuple3)
print(tuple_c)
new_list = list(tuple_c)
print(new_list)

# two types of indexing
# positive -> starts with 0
# negative -> starts with -1

tuple4 = ("a", "b", "c", "d")
print(tuple4[0])
print(tuple4[-4])
print(tuple4[-2:])
print(tuple4[-3:-1])

# Check if item exists

if "a" in tuple4:
    print("a come in")
else:
    print("a is not here")


if "g" in tuple4:
    print("g come in")
else:
    print("g is not here")

# You can change tuple with the force
tuple5 = (1, 2, 3)
list_tuple = list(tuple5)
list_tuple[0] = 10
list_tuple.append("wow")
list_tuple.remove(3)
tuple5 = tuple(list_tuple)
print(tuple5)

# adding tuple to tuple
tuple6 = (100, )
tuple5+=tuple6 #compound operator
print(tuple5)
