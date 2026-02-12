# ==============================================================
#                 PYTHON INPUT 
# ==============================================================

# INTRODUCTION:
# -------------
# The input() function in Python is used to take input from the user.
# Whatever the user types → comes as a STRING by default.

# ==============================================================
# 1) BASIC INPUT
# ==============================================================

# SYNTAX:
# -------
value = input("Enter something: ")

# EXAMPLE:
# --------
name = input("Enter your name: ")
print("Hello,", name)


# ==============================================================
# 2) TAKING INTEGER INPUT
# ==============================================================

# EXPLANATION:
# -------------
# input() returns string → must convert to int

# EXAMPLE:
# --------
age = int(input("Enter your age: "))
print("You are", age, "years old.")


# ==============================================================
# 3) TAKING FLOAT INPUT
# ==============================================================

# EXAMPLE:
# --------
price = float(input("Enter price: "))
print("Final Price =", price)


# ==============================================================
# 4) TAKING MULTIPLE INPUTS IN ONE LINE (split)
# ==============================================================

# split() → breaks the input based on spaces  
# map() → converts each value into desired type  

# EXAMPLE 1 (two ints):
# ----------------------
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# INPUT:
# 10 20

# OUTPUT:
# 30

# EXAMPLE 2 (three floats):
# -------------------------
x, y, z = map(float, input("Enter three decimals: ").split())
print(x, y, z)


# ==============================================================
# 5) TAKING LIST INPUT
# ==============================================================

# CASE 1: List of integers
# ------------------------
nums = list(map(int, input("Enter numbers: ").split()))
print(nums)

# INPUT:
# 10 20 30 40

# OUTPUT:
# [10, 20, 30, 40]


# CASE 2: List of strings
# ------------------------
words = input("Enter words: ").split()
print(words)

# OUTPUT:
# ["hello", "world"]


# ==============================================================
# 6) TAKING COMMA-SEPARATED INPUT
# ==============================================================

# Split by comma → .split(",")

# Example:
# --------
data = input("Enter values: ").split(",")
print(data)

# INPUT:
# a,b,c

# OUTPUT:
# ['a', 'b', 'c']


# ==============================================================
# 7) ADVANCED: EVAL() FUNCTION
# ==============================================================

# eval() → evaluates expression as Python code  
# (⚠️ not safe for user-facing apps, but great for learning)

# EXAMPLE 1:
# ----------
x = eval("10 + 20")
print(x)     # Output: 30


# EXAMPLE 2: Taking math expression from user
# -------------------------------------------
expr = input("Enter expression (ex: 10+5*2): ")
result = eval(expr)
print("Result =", result)

# INPUT:
# 10+5*2

# OUTPUT:
# 20


# EXAMPLE 3: Evaluating list from user
# ------------------------------------
lst = eval(input("Enter a list: "))

# INPUT:
# [10,20,30]

# OUTPUT:
# [10, 20, 30]


# ==============================================================
# 8) USING input() WITH CONDITIONALS
# ==============================================================

# Example:
# --------
name = input("Enter name: ")
if name == "admin":
    print("Welcome Admin!")
else:
    print("Hello User!")


# ==============================================================
# 9) USING strip(), lstrip(), rstrip()
# ==============================================================

# strip()  → removes spaces from both sides  
# lstrip() → removes spaces from left  
# rstrip() → removes spaces from right  

# EXAMPLES:
# ---------
text = "   hello world   "

print(text.strip())   # "hello world"
print(text.lstrip())  # "hello world   "
print(text.rstrip())  # "   hello world"


# ==============================================================
# 10) STRING INPUT CLEANING
# ==============================================================

# lower()  → convert to lowercase  
# upper()  → convert to uppercase  
# title()  → first letter capital  

# Example:
# --------
s = input("Enter text: ").lower()
print("Cleaned text =", s)

# INPUT:
# HeLLo

# OUTPUT:
# hello


# ==============================================================
# 11) JOIN FUNCTION (opposite of split)
# ==============================================================

# Example:
# --------
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)

# OUTPUT:
# Python is awesome


# ==============================================================
# 12) REPLACE FUNCTION
# ==============================================================

# Example:
# --------
text = "I like Java"
text = text.replace("Java", "Python")
print(text)

# OUTPUT:
# I like Python


# ==============================================================
# 13) CHECK FUNCTIONS (isnumeric, isalpha, isalnum)
# ==============================================================

# EXAMPLE:
# --------
s = input("Enter string: ")

print(s.isalpha())   # a-z only
print(s.isnumeric()) # 0-9 only
print(s.isalnum())   # a-z + 0-9


# ==============================================================
# 14) FULL PROGRAM USING EVERYTHING
# ==============================================================

# Example:
# --------
# Take name, marks and calculate average of marks

name = input("Enter your name: ").title()
marks = list(map(int, input("Enter marks: ").split()))

average = sum(marks) / len(marks)

print("Student:", name)
print("Marks:", marks)
print("Average =", average)

# Sample Input:
# john
# 90 80 70

# Sample Output:
# Student: John
# Marks: [90, 80, 70]
# Average = 80.0