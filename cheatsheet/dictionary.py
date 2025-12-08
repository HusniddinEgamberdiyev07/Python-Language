# 📔 Dictionary

# Dictionary stores data i key-value pairs.

# Key based access -> You access values using keys, not indexes.
# Keys must be unique.
# Keys must be immutable.
# Values can be anything.



# 📖 Creating a dictionary.

# 1) Using curly braces.

student = {
    "name":"Husniddin",
    "age":17,
    "major":"AI"
}
print(student)

# 2) Using dict() constructor

student2 = dict(name="Husniddin", age=17, major="AI")
print(student2)



# 📖 Accessing values.

# dict_name["key name"]

print(student["name"])

# If key does not exist -> Error
# Use .get() to avoid Error.

print(student.get("name"))      # -> Husniddin
print(student.get("hight"))     # -> None



# 📖 Adding & upadting items.

# 1) Adding an item

# dict_name[new item name] = value

student["surname"] = "Egamberdiyev"
print(student)

# 2) Update an item

# dict_name[key which is already exists] = new_value

student["age"] = 18
print(student)



# 📖 Removing items.

# 1) pop(key) -> removes by key.

student.pop("age")
print(student)

# 2) popitem() -> removes last added pair.

student.popitem()
print(student)

# 3) del dict_name[key].

del student["major"]
print(student)

# 4) clear() -> removes all items.

print(student2)

student2.clear()

print(student2)

# 📖 Other methods.

user = {
    "name":"Husniddin",
    "email":"email@email.com",
    "password":"123456789"
}

# 1) .keys() -> shows all keys.

print(user.keys())

# 2) .values() -> shows all values.

print(user.values())

# 3) .items() -> shows items as pairs.

print(user.items())

# 3) .update() -> adds or updates multipe itesm.

user.update({"name":"hi", "email":"bye", "password":"die", "age":"None"})
print(user)

# 📖 Looping.

# 1) Loop keys.

for key in user:
    print(key)

# 2) loop values.

for value in user.values():
    print(value)

# 3) loop key and value

for key, value in user.items():
    print(key, value)



# 📖 Nested dinctionaries.

users = {
    "user1":{
        "name":"Husniddin",
        "email":"email@email.com",
        "password":"123456789"
    }
}

print(users["user1"]["name"])



# 📖 Copying.

# Copying dcitionary is the same as copying list.

# 1) Shallow copy -> can't copy nested dictionary.

user = {
    "name":"Husniddin",
    "email":"email@email.com",
    "password":"123456789"
}

# 1.1) .copy()
user2 = user.copy()
# 1.2) dict()
user3 = dict(user)

user["name"] = "Husniddin2"

print(user)
print(user2)
print(user3)

# 2) Deep copy -> can copy nested dictionary.

import copy

users2 = copy.deepcopy(users)

users["user1"]["name"] = "Husniddin2"

print(users)
print(users2)