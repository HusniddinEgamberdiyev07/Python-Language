# range(start, end+1, step)

# for num in range(0, 26, 5):
#     print(num)
# else:
#     print("End")

# else false statement
# if true staement


# Nested loops

# list1 = [1, 2, 3]
# list2 = ["A", "B", "C"]

# for i in list1:
#     for j in list2:
#         print(i, j)
#     else:
#         print("Inner loop ended")
# else:
#     print("Outer loop ended")

# print("------------------------------------------------")

# for i in range(0, len(list1)):
#     for j in range(0, len(list2)):
#         print(list1[i], list2[j])
#     else:
#         print("Inner loop ended")
# else:
#     print("Outer loop ended")


# print("------------------------------------------------")

# num = int(input("How many tables: "))
# for i in range(2, num+2):
#     print("\n")
#     print(f"Table of {i} \n")
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i*j}')

# h = 5
# for i in range(h, 0, -1):
#     print("@" * i)


h = 10
sum = ""
for i in range(1, h+1):
    sum += str(i)
    print(sum)

