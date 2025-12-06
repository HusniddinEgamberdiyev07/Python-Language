car = {
    "brand":"ford",
    "electric":False,
    "year":1964,
    "colors":["red", "white", "blue"]
}
print(car)
print(car["year"])
print(car.get("year"))
print(car.keys())
car["color"]="white"
car["price"]="30000$"
print(car)
print(car.keys())
print(car.values())
print(car.items())

if "brand" in car:
    print("It is there")
else:
    print("It is not there")

# both keys and values
for i in car:
    print(i, car[i])

for i in car.items():
    print(i[0], i[1])

for a,b in car.items():
    print(a, b)

# print values
for i in car:
    print(car[i])

for i in car.values():
    print(i)

# print keys
for i in car:
    print(i)

for i in car.keys():
    print(i)


for i in car.items():
    print(f"key: {i[0]}, value: {i[1]}")

car.update({"year":2020})
print(car)

car["year"] = 2000
print(car)

# update can change and add
car.update({"canFly":False, "year":0})
print(car)

# remove update
car.pop("canFly")
print(car)

del car["color"]
print(car)

car.clear()
print(car)

# student = {
#     "name":"Husniddin",
#     "rollNum":"1A",
#     "paranets":["G'ulom", "Feruza"],
#     "city":"Samarkand",
#     "phoneNumber":["+998887100742"],
#     "program":"B.CS",
#     "department":"AI",
#     "cources":["math", "physics", "pspp", "icte"]
# }

# print(student)
# print(type(student))
# print(student["name"])
