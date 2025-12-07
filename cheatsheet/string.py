# 📔 String 



# It can include letters, numbers, symbols, spaces.

# It can be created using '  or ". Both are the same.

print('Hello')
print("Hello")

# Multi-line string can be created using """ or '''.

print("""Python is not
    a snake
    it is programming language""")



# 📖 Strings are indexed.

#  0  1  2  3  4  5  6  7  8  9
#  H  e  l  l  o  W  o  r  l  d
# -10 -9  -8 -7 -6 -5 -4 -3 -2 -1

txt = "HelloWorld"
print(txt[-7])  # l
print(txt[7])   # r



# 📖 String slicing

# [start : end] -> end is not included.
print(txt[0:5]) # ->  Hello.
print(txt[5:10]) # ->  World.

# We can drop end and start if we want to.
print(txt[5:]) # -> World. From 5 take everything.
print(txt[:5]) # -> Hello. From 0 to 5 take everything.



# 📖 Strings are iterable (It means we loop through it).
for char in txt:
    print(char)



# 📖 String immutable (It means we can't change it after they are created)
# But we can manipulate it using:
# 1) Concatenation.
# 2) Slicing.
# 3) Formatting.



# 📖 Concatenating and repeating strings

# 1) Strings can be combined using "+" operator.
txt1 = "Hello "
txt2 = "World"
txt3 = txt1 + txt2  # -> Hello World
print(txt3)

# 2) Strings can be repeated using "*" operator.
# Repeating Hello 3 times:
print("Hello "*3)    # -> Hello Hello Hello



# 📖 Formatting strings.

name = "Alice"
age = 22

# 1) f-string.
info = f"Name: {name}, age: {age}"
print(info)

# 2) format()
info2 = "Name: {}, age: {}".format(name, age)
print(info2)



# 📖 Membership testing.

# in keyword can check substring is inside another string.
txt4 = "Hello World"
print("World" in txt4)  # -> True
print("Bye" in txt4)    # -> False



# 📖 String Methods.

# 1. Case Conversion:
print("Hello World".lower())        # -> hello world. Lowercases everything.
print("Hello World".upper())        # -> HELLO WORLD. Uppercases everything.
print("hello woRld".title())        # -> Hello World. Capitalizes each word.
print("Hello World".capitalize())   # -> Hello world. Uppercase only first word's first letter.
print("Hello World".casefold())     # -> hello world. Stronger lowercase.

# 2. Search & Find
print("Hello World".find("Wo"))     # -> 6. returns index of substring. Only first one.
print("Hello World".find("o"))      # -> 4. We have two o but it will give us 4 first o's index.
print("Hello World".find("aaa"))    # -> -1. We don't have aaa so it returns -1.

print("Hello World".index("Wo"))    # -> 6. Same as index but returns an error if it can't find it.
# print("Hello World".index("aaa")) -> Error

print("Hello World".count("o"))     # -> 2. Counts how many substrings we have.
print("Hello World".count("l"))     # -> 3.

print("Hello World".startswith("H"))
print("Hello World".endswith("d"))

print("text".isalpha())        # -> True. Only letters.
print("123".isdigit())         # -> True. Only digits.
print("text123".isalnum())     # -> True. Letters and digits.
print("  ".isspace())          # -> True. Only whitespaces.


# 3. Splitting & Joining

print("hello, bye, die".split(","))     # -> ['hello', ' bye', ' die']. when split finds "," it will cut the string and makes new string, puts it inside list. It does not include ","

print("".join(["h", "e", "l", "l", "o"]))       # -> hello. list string to string.
print("1 ".join(["h", "e", "l", "l", "o"]))     # -> h1 e1 l1 l1 o

# 4. Alignment & Formatting

# "text".center(20, "-") -> text has 4 characters and 20 - 4 = 16 and 16 / 2 = 8. Gives 8 space from left and 8 more from right
# If the total padding is odd, the extra space goes to the right.

print("text".center(20, "-"))   # -> --------text--------

# "text".ljust(20, "-") -> 20-4=16. 16 "-" after text.
print("text".ljust(20, "-"))    # -> text----------------

# "text".rjust(20, "-") -> 20-4=16. 16 "-" before text.
print("text".rjust(20, "-"))    # -> ----------------text

# 5. Replace & Modify

print("text".replace("t", "a"))     # -> aexa. Replace all "t" with "a".

# Whitespace is the space before and after text.
print("   text ".strip())           # ->text. Removes white spaces.
print("   text ".rstrip())          # -> Removes right side white spaces
print("   text ".lstrip())          # -> Removes left side white spaces