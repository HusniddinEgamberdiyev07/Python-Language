# -- Variables --

# variable name
# must start with letter or underscore
# it can contain letters, numbers, underscore
# case-sensitive

# num1, num2, num3 = 1, 2, 3 -> assingning values to multiple variables in one line
# num1, num2, num3 = 1 -> one value to multiple variables
# a, b. c = [1, 2, 3] -> unpack collection



# -- DataTypes --

# 1) Text type: str
# 2) Numeric types: int, float, complex
# 3) Sequence types: list, tuple, range
# 4) Mapping type: dict
# 5) Set types: set, frozenSet
# 6) Boolean type: bool
# 7) Binary types: bytes, bytearray, memoryview


# Getting the data type
# type()

# Converting data types
# int()
# float()
# bool()
# str()


# -- Strings --

# """ -> multiline string

# len() -> Length 

# "text"[0, 2] -> slicing. [start, end] end is not included.
# We can leave end or start if we want to.
# "text"[:3] -> slice till 3.
# "text"[0:] -> slice from 0.
# "text"[:] -> just returns text.

# "text".upper() -> makes everything uppercae.
# "text".lower() -> makes everything lowercase.
# "text".capitalize() -> makes first character uppercase.
# "Text Bye Die".casefold() -> International lower

# "text".center(20, "-") -> text has 4 characters and 20 - 4 = 16 and 16 / 2 = 8. Gives 8 space from left and 8 more from right
# If the total padding is odd, the extra space goes to the right.
# result: "--------text--------"

# Whitespace is the space before and after text.
# "   text ".strip() -> removes white spaces.
# result: text

# "text".replace("t", "a")  -> replace t to a in text
# result: aexa

# "hello, bye, die".split(",") -> when split finds "," it will cut the string and makes new string, puts it inside list. It does not include ","
# result: ['hello', ' bye', ' die']

# We can combine two strings using "+"
# "text " + " bye"
# result: "text  bye"

# "text".count("t") -> count t inside text.
# result: 2 

# Escape character:
# \' -> '
# \\ -> \
# \n -> new line
# \t -> tab
# \b -> backspace

# -- Boolean --

# True or False.

# Condition, function can return boolean value.

# isinstance("text", int) -> is "text" int


# -- Operators --

# 1) Arithmetic Operators
#       1) +
#       2) -
#       3) *
#       4) /
#       5) %
#       6) //
#       7) **

# 2) Assignment Operator
#       1) =

# 3) Comparison Operators
#       1) ==  |  equal.
#       2) !=  |  not equal.
#       3) >   |  greater than.
#       4) <   |  less than.
#       5) >=  |  greater than or equal.
#       6) <=  |  less than or equal.

# 4) Logical Operators
#       1) and   |   both true is true.
#       2) or    |   either true is true.
#       3) not   |   true is false. false is true.

# 5) Identity Operators
#       1) is       |   returns true if both variables are the same object.
#       2) is not   |   returns true if both variables are NOT the same object.

# 6) Membership Operators
#       1) is       |   returns true if variable is inside something.
#       2) is not   |   returns true if variable is NOT inside something.

# 7) Bitwise Operators
#       1) &    |  and
#       2) |    |  or
#       3) ^    |  xor
#       4) ~    |  not
#       5) <<   |  zero fill left shift
#       6) >>   |  signed right shift



# -- List --
# -- Set --
# -- Tuple --
# -- Dictionary --
# -- If --
# -- Loop --
# -- Functions --