# i = 0
# while i <= 5:
#     if i == 3:
#         break
#     print(i)
#     i+=1

# it will stop the loop after break

# print("---------------------------")

# j = -1

# while j < 5:
#     j+=1
#     if j == 3:
#         continue
#     print(j)

# it will jump from continue to the loop

# print("---------------------------")
# print("Factorial")


# num = int(input("Enter positive num: "))
# factorial = 1

# if num == 0:
#     factorial = 1
# elif num < 0:
#     print("Gimme positive")
#     factorial = "None"
# else:
#     for i in range(num, 1, -1):
#         factorial*=i

# print(factorial)

# import random

# s_num = random.randint(1, 100)
# guess = 0 
# while guess != s_num:
#     guess = int(input("Enter a number 1 to 100: "))
#     if guess > s_num:
#         print("Too high")
#     elif guess < s_num:
#         print("Too low")
#     else:
#         print(f"You found it {guess} == {s_num}")


# i = 1
# while i < 6:
#     print(i)
#     i+=1
# else:
#     print("i is bigger than 6")

fruits = ["apple", "banana", "orange", "cherry"]

for fruit in fruits:
    if fruit == "orange":
        break
    print(fruit)
