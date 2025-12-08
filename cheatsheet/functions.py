# 📔 Function

# Function is a code of block that performs a specific task. 
# It can accept inputs, produce output, and helps you structure code into reusable pieces.



# 📖 Creating functions.

# def name(parameters -> optional):
#       statement
#       return value -> optional

def showMsg():
    print("Hello World")

showMsg()


# 📖 Parameters and arguments.

# parameters named variable.
# arguments are value.

# 1) Positional parameters.

def sayInfo(name, age):
    print(f"name: {name}, age: {age}")

sayInfo("Husniddin", 18)    # -> Name is first then first argument goes to first parameter...

# 2) Keyword arguments.

sayInfo(age=18, name="Husniddin")   # -> order is not important. We tell which argument goes to which parameter.

# 3) Default parameter.

def sayInfo(name, age=0):
    print(f"name: {name}, age: {age}")

sayInfo("Husniddin")    # -> If we don't give value for age it will take default value 0.

# 4) Unpacking.

# 1) Unpacking a list into positional args.

list1 = [100, 2]

def sumNums(a, b):
    print(a+b)

sumNums(*list1)

# 2) Unpacking a dict into kwargs. 

def showUserInfo(name, age):
    print(name, age)

data = {"name":"Husniddin", "age":18}
showUserInfo(**data)

# 📖 Return values.

def sayHi(name):
    print(f"Hi {name}")

sayHi("Husniddin")
print(sayHi("Ali"))     # -> None

# We can write function without return but functions always returns something. 
# If we don't write return function will return None.

def sum(num1, num2):
    return num1 + num2

print(sum(1, 2))



# 📖 Special parameter types

# 1) *args -> Collects extra positional arguments. Stores as a tuple.

def showArgs(*nums):
    print(nums)

showArgs(1, 2, 3)

# 2) **kwargs -> Collects extra keyword arguments. Stores as a dictionary.

def showKwargs(**userInfo):
    print(userInfo)

showKwargs(name="Husniddin", age=18)

# 3) Using both args and kwargs

def both(a, b, *args, c, **kwargs):
    print("a", a)
    print("b", b)
    print("c", c)
    print("args", args)
    print("kwargs", kwargs)

both("hello", "bye", "die", c="c", name="ali")

# Order is important:

# Positional parameters -> default parameters -> *args -> keyword-only parameters -> **kwargs

# 4) Keyword-only arguments

# If you put parameter afte *args it will become keyword-only.

def f(a, *args, b):
    print("a", a)
    print("args", args)
    print("b", b)

f(1, 2, 3, 4, b=5)

# 📖 Lambda functions.

# lambda parameters: expression

# we can have many parameters but only one expression.
# it will return a value

add = lambda a, b : a+b
print(add(1, 2))

# You can use conditions inside lambda

odd_even = lambda num : "even" if num % 2 == 0 else "odd"
print(odd_even(2))
print(odd_even(1))