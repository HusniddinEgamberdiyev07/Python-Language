fruits  = ["apple", "banana", "cherry", "orange", "kiwi"]
# new_fruits = [x for x in fruits if "a" in x]

# syntax
# new_list = [expression for item in iterable if condition]

new_fruits = [x for x in fruits if x != "apple"]
print(new_fruits)

nums = [num for num in range(100) if num%10 == 0]
print(nums)

square_nums = [num**2 for num in range(11)]
print(square_nums)

even_nums = [num for num in range(21) if num%2 == 0]
odd_nums = [num for num in range(21) if num%2 != 0]

print(even_nums)
print(odd_nums)

first_letters = [fruit[0] for fruit in fruits]
print(first_letters)

upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

length_fruits = [f"{fruit}'s length is {len(fruit)}" for fruit in fruits]
print(length_fruits)

replace_vowels_wow = ["wow" if x in "aouie" else x for x in fruits[0]]
print(replace_vowels_wow)

# fruit = "Apple"
# fruit = fruit.replace("A", "Muhhhaaa")
# print(fruit)

