# INTRODUCTION:
# -------------
# A Python dictionary is a data structure that stores data in the form of
# KEY : VALUE pairs.

# It is similar to:
# - English dictionary → Word : Meaning  
# - Real life → RollNo : StudentName  
# - Programming → ID : Data  

# Example:
# --------
student = {
    "name": "John",
    "age": 20,
    "marks": 85
}

# Dictionaries are extremely powerful because:
# - They provide VERY FAST lookup (O(1))
# - They allow easy updates
# - They allow flexible data formats


# =======================================================================
# KEY PROPERTIES:
# =======================================================================

# 1) Dictionary is **unordered** (Python 3.7+ preserves insertion order,
#    but it should not be relied on for logic).

# 2) Keys must be **unique**.

# 3) Keys must be **immutable**:
#    - ✔ integers
#    - ✔ strings
#    - ✔ tuples
#    - ✘ lists
#    - ✘ sets

# 4) Values can be ANYTHING:
#    - int, float, string
#    - list, tuple, dict
#    - custom objects

# 5) Dictionary is **mutable** (we can modify it).


# =======================================================================
# INTERNAL WORKING (BEGINNER-FRIENDLY EXPLANATION)
# =======================================================================

# How does Python retrieve values so fast?

# When you do:
# value = dict[key]

# Python does NOT search one by one.  
# Instead, Python uses **hashing**.

# -------------------------------------------------------
# WHAT IS HASHING?
# -------------------------------------------------------
# A hash is a unique number created from the key using a hash function.

# Example:
# hash("apple") → 892374982374  
# hash("banana") → 671456512334  

# Python stores dictionary items in a special table called **Hash Table**.

# -------------------------------------------------------
# HOW WORKS INTERNALLY:
# -------------------------------------------------------
# 1) When you add a key:
#    → Python calculates its hash  
#    → Stores value in a position based on hash  

# 2) When you access key:
#    → Python again generates hash  
#    → Directly jumps to memory position  
#    → Returns value instantly  

# No looping, no searching → **O(1) time**.

# This is why dictionaries are super fast.


# =======================================================================
# COMMON OPERATIONS
# =======================================================================

# 1) Create dictionary:
# ---------------------
d = {"name": "Ram", "age": 22}

# 2) Access value:
# ----------------
d["name"]

# 3) Add new pair:
# ----------------
d["city"] = "Delhi"

# 4) Update value:
# ----------------
d["age"] = 25

# 5) Delete key:
# --------------
del d["city"]

# 6) Check if key exists:
# -----------------------
"name" in d

# 7) Get list of keys:
# --------------------
d.keys()

# 8) Get list of values:
# ----------------------
d.values()

# 9) Loop through dictionary:
# ---------------------------
for key, value in d.items():
    print(key, value)