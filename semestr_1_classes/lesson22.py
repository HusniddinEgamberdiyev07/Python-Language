# for i in range(1, 6):
#     print(i, end="\t")
# print("\n")


# matrix = [[1, 2, 3], [1, 0, 1], [0, 2, 3]]

# for row in matrix:
#     for element in row:
#         print(element,  " ")
#     print()

# for i in range(1, 10, 1):
#     print(i, end=" ")
#     if i % 3 == 0:
#         print()

# j=0
# for i in range(2, 11, 1):
#     print(i, end=" ")
#     j+=1
#     if j == 3:
#         print()
#         j=0


# -- Lambda --

# lambda arguments : expression
# many arguments 
# one expression

# x = lambda a, b, c: a + b + c
# print(x(10, 2, 1))
# print(x(3, 2, 1))

# SI = lambda P, T, R : (P*T*R)/100
# print(SI(1000, 12, 1))


# nterms = 10
# n1, n2 = 0, 1

# count = 0
# sum = n1

# while count<nterms:
#     print(n1)
#     nth = n1+n2
#     n1=n2
#     n2=nth
#     count+=1