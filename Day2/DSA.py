# ========================================================
#         DSA  
# ========================================================

# --------------------------------------------------------
# INTRODUCTION 
# --------------------------------------------------------
# DSA = Data Structures + Algorithms

# Time Complexity → How time grows as input size (n) grows  
# Space Complexity → How much extra memory your algorithm uses

# Common Complexities:
# O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)

# --------------------------------------------------------
#  PROBLEM 1 — FIND LARGEST NUMBER IN A LIST
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Given a list of integers, return the largest element.

# SAMPLE INPUT:
# -------------
# [10, 5, 20, 8]

# SAMPLE OUTPUT:
# --------------
# 20

# LOGIC:
# ------
# - Assume first element is maximum  
# - Loop through each number  
# - If a number is bigger → update max  
# - Return the max at the end  

# PYTHON CODE:
# ------------
def find_largest(nums):
    max_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num
    
    return max_val

# Example
print(find_largest([10, 5, 20, 8]))   # Output: 20


# TIME COMPLEXITY (DETAILED):
# ---------------------------
# We visit each element exactly once → O(n)

# SPACE COMPLEXITY:
# -----------------
# We use only 1 extra variable (max_val) → O(1)
# Constant space.



# --------------------------------------------------------
#  PROBLEM 2 — COUNT EVEN NUMBERS IN A LIST
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Given a list of integers, count how many are even.

# SAMPLE INPUT:
# -------------
# [2, 7, 8, 10]

# SAMPLE OUTPUT:
# --------------
# 3

# LOGIC:
# ------
# - Initialize counter = 0  
# - Loop through numbers  
# - If num % 2 == 0, increment counter  
# - Return count  

# PYTHON CODE:
# ------------
def count_even(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1
    
    return count

# Example
print(count_even([2, 7, 8, 10]))   # Output: 3


# TIME COMPLEXITY:
# ----------------
# Loop runs n times → O(n)

# SPACE COMPLEXITY:
# -----------------
# Only a counter variable used → O(1)



# --------------------------------------------------------
#  PROBLEM 3 — REVERSE A STRING (WITHOUT slicing)
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Reverse a given string manually.

# SAMPLE INPUT:
# -------------
# "hello"

# SAMPLE OUTPUT:
# --------------
# "olleh"

# LOGIC:
# ------
# - Start from last index  
# - Append characters one by one  
# - Build a new reversed string  

# PYTHON CODE:
# ------------
def reverse_string(text):
    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    
    return reversed_text

# Example
print(reverse_string("hello"))   # Output: "olleh"


# TIME COMPLEXITY:
# ----------------
# Loop runs n times → O(n)

# SPACE COMPLEXITY:
# -----------------
# We create a new string of size n → O(n)



# --------------------------------------------------------
#  PROBLEM 4 — CHECK IF STRING IS PALINDROME
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# A palindrome reads the same forward & backward.

# SAMPLE INPUT:
# -------------
# "level"

# SAMPLE OUTPUT:
# --------------
# True

# LOGIC:
# ------
# - Reverse the string manually  
# - Compare reversed with original  
# - If equal → palindrome  

# PYTHON CODE:
# ------------
def is_palindrome(s):
    reversed_s = ""

    # reverse manually
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]

    return reversed_s == s

# Example
print(is_palindrome("level"))   # Output: True


# TIME COMPLEXITY:
# ----------------
# Reversing takes n steps → O(n)  
# Comparison also takes n steps → O(n)

# Total = O(n)

# SPACE COMPLEXITY:
# -----------------
# We store reversed string → O(n)



# --------------------------------------------------------
#  PROBLEM 5 — LINEAR SEARCH (FIND INDEX OF TARGET)
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Return the index of the target number.  
# If not found → return -1.

# SAMPLE INPUT:
# -------------
# nums = [4, 9, 2, 7]  
# target = 2

# SAMPLE OUTPUT:
# --------------
# 2

# LOGIC:
# ------
# - Loop through each index  
# - If nums[i] == target → return i  
# - If loop ends without finding → return -1  

# PYTHON CODE:
# ------------
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Example
print(linear_search([4, 9, 2, 7], 2))   # Output: 2


# TIME COMPLEXITY:
# ----------------
# Worst case → target at end or not present  
# We check all n elements → O(n)

# Best case → target at index 0 → O(1)

# SPACE COMPLEXITY:
# -----------------
# No extra space used → O(1) 

# ==========================================



# --------------------------------------------------------
#  PROBLEM 6 — FIND SECOND LARGEST ELEMENT
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Given a list of integers, return the second largest element.

# SAMPLE INPUT:
# -------------
# [10, 40, 30, 20]

# SAMPLE OUTPUT:
# --------------
# 30

# LOGIC:
# ------
# - First find the largest element.
# - Initialize second largest as something very small.
# - Loop again OR track both largest & second largest in one loop.
# - Update them accordingly.

# PYTHON CODE:
# ------------
def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

# Example
print(second_largest([10, 40, 30, 20]))   # Output: 30


# TIME COMPLEXITY:
# ----------------
# Single loop → O(n)

# SPACE COMPLEXITY:
# -----------------
# Only two extra variables → O(1)



# --------------------------------------------------------
#  PROBLEM 7 — COUNT FREQUENCY OF EACH ELEMENT
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Given a list, count how many times each element appears.

# SAMPLE INPUT:
# -------------
# [1, 2, 2, 3, 3, 3]

# SAMPLE OUTPUT:
# --------------
# {1: 1, 2: 2, 3: 3}

# LOGIC:
# ------
# - Create an empty dictionary.
# - Loop through list.
# - If number not seen → set frequency = 1.
# - If already seen → increment its count.
# - Return dictionary.

# PYTHON CODE:
# ------------
def count_frequency(nums):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    return freq

# Example
print(count_frequency([1, 2, 2, 3, 3, 3]))  
# Output: {1: 1, 2: 2, 3: 3}


# TIME COMPLEXITY:
# ----------------
# Each element processed once → O(n)

# SPACE COMPLEXITY:
# -----------------
# Dictionary stores all unique elements → O(k)
# (k = number of distinct values, worst-case k = n)



# --------------------------------------------------------
#  PROBLEM 8 — MERGE TWO SORTED LISTS (NO LIBRARIES)
# --------------------------------------------------------

# DESCRIPTION:
# ------------
# Given two sorted lists, merge them into a single sorted list.

# SAMPLE INPUT:
# -------------
# A = [1, 3, 5]
# B = [2, 4, 6]

# SAMPLE OUTPUT:
# --------------
# [1, 2, 3, 4, 5, 6]

# LOGIC:
# ------
# - Use two pointers: i for A, j for B.
# - Compare A[i] and B[j].
# - Append smaller value to new list.
# - Move that pointer forward.
# - If one list ends → copy remaining elements.

# PYTHON CODE:
# ------------
def merge_sorted_lists(A, B):
    i = j = 0
    merged = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    # add remaining
    while i < len(A):
        merged.append(A[i])
        i += 1

    while j < len(B):
        merged.append(B[j])
        j += 1

    return merged

# Example
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
# Output: [1, 2, 3, 4, 5, 6]


# TIME COMPLEXITY:
# ----------------
# We traverse both lists once → O(n + m)

# SPACE COMPLEXITY:
# -----------------
# We create a merged l