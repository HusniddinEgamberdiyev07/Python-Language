
# Why do we need functions 
# To remove repeated code blocks and automation
# Cleaner code and easy to debbug

# We use def key word to create function
# def means define 
# defining functions

def sayMsg():
    print("Hi")

# sayMsg()

# Every function will return something.
# print(sayHi("Husniddin")) -> this will return None.
# Until I call function it will not be executed.

# Functions can have inputs or not.
# If function has inputs when we call it we have to give those inputs

def sayHi(name):
    print(f"Hello! {name}")

# sayHi("Husniddin")

# name -> is parameter.Parameters are variables.
# "Husniddin" -> is argument. Arguments are values.

def printSomething(msg):
    print(msg)

# printSomething("Hahahahahahahaha")
# printSomething(500)
# printSomething(500+100+100+450)

def sum(a, b):
    printSomething(a+b)

# sum(10, 10)

# Arbitrary Arguments, *args
# I dunno how many parameters I need.
# *name -> this is tuple

def something(*thing):
    print(thing[0])
    print(thing)
    print(type(thing))

# something("hi", "bye", "die", "why")

def addNums(*nums):
    sum = 0
    for num in nums:
        sum += num
    print(sum)

# addNums(1, 2, 3, 4, 5)


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def inputMine(num=0, IsNum=True):
    inp = 0
    if IsNum:
        inp = int(input(f"Enter a number for {num}: "))
    else:
        inp = input(f"Enter a operation: ")

    return inp

def calculotor(num1, num2, operation):
    result = 0

    if   operation == "+": result = add(num1, num2)
    elif operation == "-": result = subtract(num1, num2)
    elif operation == "*": result = multiply(num1, num2)
    elif operation == "/": result = divide(num1, num2)
    else: print("We do not have this operation. Sorry.")

    print(result)

calculotor(5, 2, "-")
calculotor(5, 2, "+")
calculotor(5, 2, "*")
calculotor(5, 2, "/")
calculotor(inputMine(1), inputMine(2), inputMine(IsNum=False))
