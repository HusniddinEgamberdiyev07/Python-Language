# 📔 Set

# Unordered -> Items have no fixed position.
# Unindexed -> You can't access elements using indexes.
# Mutable -> You can add or remove items.
# Unique elements only -> duplicates are automatically removed.



# 📖 Creating a sets.

# 1) Using curly braces.

fruits = {"apple", "banana", "cherry"}

# 2) Using set constructor.

letters = set(["a", "b", "c", "d"])

# 3) Empty set.

# You cannot create an empty set using {} it creates dictionary.

empty_set = set()



# 📖 Adding elements.

# 1) Add
empty_set.add("hi")

print(empty_set)

# You can only add immutable items inside set (Numbers, string, tuples).

# empty_set.add([1, 2, 3]) -> this will give you an error.

# 2) Update -> Adds all elements from another iterable.

empty_set.update(["bye", "die"])

print(empty_set)

# 📖 Removing elements.

numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

# 1) Remove -> removes item, error if not found.

numbers.remove(5)
print(numbers)

# 2) Discard -> removes item, no error if not found.

numbers.discard(4)
numbers.discard(5)
print(numbers)

# 3) Pop -> removes random item.

numbers.pop()
print(numbers)

# 4) Clear -> removes all items

numbers.clear()
print(numbers)



# 📖 Set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1) Union -> All items.

print(a | b)
print(a.union(b))

# 2) Intersections -> Items in both.

print(a & b)
print(a.intersection(b))

# 3) Difference -> items a not in b.

print(a - b)
print(a.difference(b))

# 4) Symmetric Difference -> Items not in both.

print(a ^ b)
print(a.symmetric_difference(b))

# All of this has _update version.
# These are normal versions they will return new set.
# Update versions will change set directly.