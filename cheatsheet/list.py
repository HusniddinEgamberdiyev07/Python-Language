# 📔 List

# Mutable: items can be modified, replaced, or removed.
# Ordered: maintains the order which items are added.
# Index based: items are accessed using their position. (starting from 0 or -1)
# Can store mixed data types.

# 📖 Creating a list.

# 1) Using square brackets.

fruits = ["apple", "orange", "banana"]

print(fruits)

# 2) Using list() constructor.

# We can create a list by passing an iterable (It means we loop through it. Tuple, Set, String, List) to the list function.
letters = list("Hello World")
print(letters)      # -> ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

nums = list((1, 2, 3))      # -> We passed tuple
print(nums)                 # -> [1, 2, 3]. Now it is list.

# 3) Creating list with Repeated Elements.

a = [2]*5
print(a)        # -> [2, 2, 2, 2, 2]



# 📖 Accessing list elements.

# Elements in a list are accessed using indexes.
# Positive indexes starts with 0. Add 1.
# Negative indexes starts with -1. Add -1.

#        0  1  2  3
nums2 = [1, 2, 3, 4]
#       -4 -3 -2 -1

print(nums2[3])         # -> 4.
print(nums2[-3])        # -> 2.
print(nums2[1:3])       # -> [2, 3]. Elements from 1 to 3.



# 📖 Adding elements into list.

empty = []

# 1) append(element) -> Adds an element at the end of the list.

empty.append("bye")
print("append", empty)

# 2) insert(position, element) -> Adds an element at the specific position.

empty.insert(0, "hi")
print("insert", empty)

# 3) extend(elements) -> Adds multiple elements to the end of the list.

empty.extend(("get", "lost"))
print("extend", empty)

# 4) + -> Combine two lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("concatenate", list1 + list2)


# 📖 Removing elements from list.

nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1) remove(value) -> Removes by value. But only first one.

nums3.remove(4)
print("remove", nums3)

# 2) pop(index) -> Removes by index. If there is no index removes the last element.

nums3.pop(0)
print("pop with index", nums3)

nums3.pop()
print("pop without index", nums3)

# 3) del list[index] -> Removes an element by index. We can use [start:end].

del nums3[1]
print("del with one index", nums3)

del nums3[0:2]
print("del with [start:end]", nums3)

# 4) clear() -> Removes all Elements.

nums3.clear()
print("clear", nums3)



# 📖 Updating list elements.

nums4 = [1, 2, 3]
nums4[1] = "Bye"

print(nums4)

nums4[0] = "Hi"
nums4[2] = "Die"

print(nums4)



# 📖 Nested lists.

# A nested list is a list inside another list. We can access nested elements by chaining indexes.

#         0          1          2
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#          0, 1, 2    0, 1, 2    0, 1, 2

print(matrix[0][1])     # -> 2. matrix[0] is [1, 2, 3]. [1, 2, 3][1] is 2



# 📖 Iterating over lists.

fruits2 = ["apple", "orange", "banana"]

for fruit in fruits2:
    print(fruit)



# 📖 List comprehension.

# A list comprehension is a short, fast way to create lists.

# Syntax:

# 1) Basic

# [ new_item   for    item   in   iterable ]
#   create     loop   variable    data

# We are taking data using loop and storing in variable then creating new item using that variable.

nums5 = [ num for num in [1, 2, 3] ]
print(nums5)

nums5_square = [ num**2 for num in nums5 ]
print(nums5_square)

# 2) With condition if.

# [ new_item for item in iterable if condition ]

nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [ num for num in nums6 if num % 2 == 0]
print(even)

# 3) If and else

# [ new_item_if_true if condition else new_item_if_false for item in iterable ]

odd_even = [ "even" if num % 2 == 0 else "odd" for num in nums6]
print(nums6)
print(odd_even)

scores = [92, 80, 71, 60, 46]

grades = [( "A" if score >= 90 else "B" if score >= 70 else "C" if score >= 50 else "D" ) for score in scores]

print(grades)

# 4) nested loop

# [ [x, y] for x in iterable for y in iterable ]

nums7 = [1, 2, 3]
letters2 = ["a", "b", "c"]

nums_letters = [[num, letter] for num in nums7 for letter in letters2]
print(nums_letters)



# 📖 Sorting list.

numbers = [5, 2, 4, 3, 1]
numbers.sort()      # sort() -> changes the original list. Ascending.
print(numbers)

numbers2 = [5, 2, 4, 3, 1]
numbers2.sort(reverse=True)      # -> Descending.
print(numbers2)

names = ["ali", "John",  "bahodir", "Sam", "Bob"]
names.sort()    # ['Bob', 'John', 'Sam', 'ali', 'bahodir'] -> Uppercase first then lowercase. Ascending.

print(names)

names2 = ["ali", "john",  "bahodir", "Sam", "Bob", "Dialyn"]
names2.sort(key=str.lower)      # ['ali', 'bahodir', 'Bob', 'Dialyn', 'john', 'Sam'] -> Ignore case

print(names2)

languages = ["python", "c#", "javasrcipt", "java", "c++"]
languages.sort(key=len)     # ['c#', 'c++', 'java', 'python', 'javasrcipt'] -> Sort by length

print(languages)

numbers3 = [5, 2, 4, 3, 1]
sorted_nums3 = sorted(numbers3)     # sorted() -> Does not change the original list. Returns new list. Ascending.

print(sorted_nums3)

numbers4 = [5, 2, 4, 3, 1]
sorted_nums4 = sorted(numbers4, reverse=True)       # -> Descending.

print(sorted_nums4)



# 📖 Copying list.

# 1) Basic copy

list1 = [1, 2, 3]
list2 = list1       # list2 is another name pointing to the same list in memory.

list1.append(4)

print(list2)        # [1 ,2, 3, 4] -> we are printing list2 but it has new item 4 but we added 4 to list1.
                    # This happened because list2 is pointing to list1. It does not have it is own list.

list3 = list1.copy()    # Now list3 has it is own list and it is same as list1.
                        # But if we change list1 if will not effect list2

list1.remove(4)

print(list3)
print(list1)

# 2) Deep copy

a = [[1, 2], [3, 4]]

b = a.copy()    # We copied a to b. Now if I change a it will not effect b. Will it?

a[0][1] = "Haha it changed"

print(b)    # copy() will not copy nested lists. If we want to copy nested lists we should use copy.deepcopy().

import copy

c = copy.deepcopy(a)
a[0][0] = "It won't change c"

print(c)