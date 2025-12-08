# swap two numbers
num1 = 1
num2 = 2
helper = num2
num2 = num1
num1 = helper

print(num1)
print(num2)

# swap two numbers without third variable

num3 = 10
num4 = 20
num3, num4 = num4, num3

print(num3)
print(num4)

# contains wovow or not 

word = "hll"
vowels = "aeouiAEUIO"
has_vowel = False

for letter in word:
    if letter in vowels:
        has_vowel = True
        break

if has_vowel:
    print("Has")
else:
    print("Has not")

# leap year

# (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# factorial

num = int(input("Enter positive num: "))
factorial = 1

if num == 0:
    factorial = 1
elif num < 0:
    print("Gimme positive")
    factorial = "None"
else:
    for i in range(num, 1, -1):
        factorial*=i

print(factorial)

# guessing game

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

# star

h = 5
for i in range(1, h):
    print("*" * i)

# matrix

matrix = [[1, 2, 3], [1, 0, 1], [0, 2, 3]]

for row in matrix:
    for element in row:
        print(element,  end=" ")
    print()


# fibonacci sequence

nterms = 10
n1, n2 = 0, 1

count = 0
sum = n1

if nterms<=0:
    print("No negative number")
elif nterms==1:
    print(n1)
else:
    while count<nterms:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1