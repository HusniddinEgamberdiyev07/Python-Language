# sets -> {}

# sets are unoredered, unchangeable, unindexed, duplicates are not allowed, can store any type
# tuples are ordered, unchangeable, indexed, duplicates are allowed, can store any type
# lists are ordered, changeable, indexed, duplicates are allowed, can store any type

a = {10, 20, 30, 10, 10}
print(a)

print(type(a))
print(len(a))

x = set(a)
x2 = set((190, 1, 89))
print(x)
print(x2)

for i in a:
    print(i)

print(10 in a)

# you can't modifie it
# but you can add new items and remove them
a.add(1000)
print(a)
a.remove(20)
print(a)

# to add items from one set to another set or another iterable
b=(200, 300, 400)
a.update(b)
print(a)

a.update(["muhhahahaa", "wooow", "husniddin"])
a.update(("hi", "bye"))
print(a)
a.remove("husniddin")
print(a)

# husniddin is the student we can't tell someone else as husniddin but we can add new students or remove him
ri = a.pop()
print(ri)
print(a)

# del a -> will delete variable too
# print(a) -> error

a.clear()   # -> will remove all items
print(a)

# dicard won't show error if that item does not exist

c = {10, 30, 50}
c.discard(60)
print(c)