tuple1 = (1, 2, 30)

list_tuple = list(tuple1)
list_tuple.remove(30)
tuple1  = tuple(list_tuple)

print(tuple1)

# packing and unpacking

tuple2 = (10, 20, 30, 40) # -> packing

# item1 = tuple1[0]
# item2 = tuple1[1]
# item3 = tuple1[2]
# item4 = tuple1[3]

(item1, item2, item3, item4) = tuple2   # -> unpacking
print(item1, item2, item3, item4)

gifts = ("gift1", "gift2", "gift3", "gift4")
# (person1, person2, *person3) = gifts
# (person1, *person2, person3) = gifts
(*person1, person2, person3) = gifts
print(person1, person2, person3)

nums = (10, 20, 30, 40, 50)
# p1 = nums[0:2]
# p2 = nums[2:4]
# p3 = nums[4]
# print(p1, p2, p3)

for i in range(len(nums)):
    print(nums[i])

# joining two tuple

tuple3 = (10, 20, 30)
tuple4 = (40, 50)
tuple_c = tuple3 + tuple3
print(tuple_c)

# multiply tuple

tuple_m = tuple3*3
print(tuple_m)