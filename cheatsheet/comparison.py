# 📔 Python Collections Comparison: List vs Tuple vs Set

# -------------------------
# 📝 List
# ✅ Mutable (can change)
# ✅ Ordered (keeps insertion order)
# ✅ Indexed (access by position)
# ✅ Allows duplicates
# ❌ Slower for some operations vs tuple/set
fruits_list = ["🍎", "🍊", "🍌", "🍎"]
print("List:", fruits_list)
fruits_list.append("🥭")  # add
print("List after append:", fruits_list)

# -------------------------
# 📦 Tuple
# ❌ Immutable (cannot change)
# ✅ Ordered
# ✅ Indexed
# ✅ Allows duplicates
# ✅ Faster than list for iteration
fruits_tuple = ("🍎", "🍊", "🍌", "🍎")
print("Tuple:", fruits_tuple)
# fruits_tuple[0] = "🍏" -> ❌ Error
num1, num2, *rest = (1, 2, 3, 4)
print("Tuple unpacking:", num1, num2, rest)

# Convert tuple to list to modify
temp_list = list(fruits_tuple)
temp_list[0] = "🍏"
print("Tuple → List:", temp_list)

# -------------------------
# 🔹 Set
# ✅ Mutable
# ❌ Unordered (no index)
# ❌ Not indexed
# ✅ Unique elements only (duplicates removed)
fruits_set = {"🍎", "🍊", "🍌", "🍎"}  # 🍎 duplicate removed
print("Set:", fruits_set)
fruits_set.add("🥭")
print("Set after add:", fruits_set)
print("Is 🍌 in set?", "🍌" in fruits_set)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)           # {1,2,3,4,5}
print("Intersection:", a & b)    # {3}
print("Difference:", a - b)      # {1,2}
