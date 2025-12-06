# -- Copying dict --

# car = {
#     "brand":"ford",
#     "electric":False,
#     "year":1964,
#     "colors":["red", "white", "blue"]
# }
# car2 = car.copy()
# print(car2)

car = {
    "brand":"ford",
    "electric":False,
    "year":1964,
    "colors":["red", "white", "blue"]
}
car2 = dict(car)
print(car2)



# -- Nested dict --

# dict1={
#     "dict2":{
#         "dict3":{}
#     }
# }

myFamily={
    "child1":{
        "name":"Husniddin",
        "year":2007
    },
    "child2":{
        "name":"Ramziddin",
        "year":2005
    },
    "child3":{
        "name":"Marjona",
        "year":2003
    }
}

print(myFamily["child1"]["name"])
