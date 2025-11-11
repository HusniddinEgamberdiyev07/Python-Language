# compiler and interpreter->translates high level to low level language (Machine language)
# compiler -> tanslates whole file once. If there is error it will continue translating
# interpreter -> translates line by line. If there is an error it will stop
# python uses interpreter

# -- Conditional statements -- 

# 2 types of control ( Control structure )
# 1) conditional if and switch
# 2) looping for and while

# equal ==
# not equal !=
# greater than >
# greater than or equal >=
# less than <
# less than or equal <=


# -- If statement --

# intentation -> empty space

# syntax
# if condition:         -> true statement
#     code
# elif condition:       -> if if or elif doesn't get execute elif will be executed
#     code
# else:                 -> if anything gets executed it will get executed
#     code



# num = 10
# if num > 5:
#     print(f"{num} is greater than 5")




# sum of two number greater than hundred

# num1 = 10
# num2 = 91
# sum = num1 + num2
# if sum > 100:
#     print(f"{sum} is greater than 100")


# num1 = 100
# num2 = 33

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num1} is less than {num2}")

num1 = "10"
print(type(11))
if type(num1) == int:
    if num1 % 2 == 0:
        print(f"{num1} is even")
    elif num1 % 2 != 0:
        print(f"{num1} is odd")
else:
    print("It is not number")
