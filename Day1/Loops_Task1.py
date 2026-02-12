for i in range(1, 4):
    print("* " * i)
# output 
# *
# * *
# * * *
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# output
# 1
# 1 2
# 1 2 3
for i in range(1, 4):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
# output
# A
# AB
# ABC
rows = 5
cols = 6

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# output
# * * * * * *
# *         *
# *         *
# *         *
# * * * * * *


