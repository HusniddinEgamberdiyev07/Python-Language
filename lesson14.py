# clear removes only content.
# del deletes whole variable.

# union->it combines two sets and returns new set.
# update->inserts all items to another set.

# intersection_update->adds items if both sets have it.
# intersection-> is like intersection_update but it returns new set

# symmetric_difference_update->it will take if the item is not present in both sets
# symmetric_difference->it is the same as symmetric_difference_update but returns new set

set1  = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# set3 = set1.update(set2) -> None
print(set3)

set1.update(set2)
print(set1)

a={10, 20, 15, 30, 100, 40, 60}
b={20, 60, 80, 30, 25, 10}


# a.intersection_update(b)
# print(a)    # {10, 20, 60, 30}

# c = a.intersection(b)
# print(c)    # {10, 20, 60, 30}


# a.symmetric_difference_update(b)
# print(a)    # {15, 80, 25, 100, 40}

# c = a.symmetric_difference(b)
# print(c)    # {100, 40, 15, 80, 25}

