name = "Samarkand"
print(name[5:9])
# range == starting point and ending point
print(name[:5])
# from the start till the point
print(name[6:])
# from the point till the end

print(name[-3:])
print(name[-7:-4])

text = "Hello World Bye World"
# print(text.upper())
# print(text.lower())
# b = text.lower()
# print(b)
# print(len(text))
# print(len(text.strip()))
# removes starting space and ending space
# print(text.replace("l", "😀"))
text2 = text.split(" ")
print(text2)

# A = "Hello"
# B = "World"
# space = " "
# C = A + space + B
# print(C)

# text = "Age:"
# age = 18
# print(f"{text} {age}")


# age = 18
# text = "Age: {}"
# print(text.format(age))

text = "My name is Huniddin, Scores: Eng {}, Phy {}, Math {}"
math = 20
eng = 10
phy = 5
print(text.format(eng, phy, math))

# 1 to 13 slides
