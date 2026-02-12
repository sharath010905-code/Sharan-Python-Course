# Multiplication table
# Enter table name 5
# Enter the limit 10

# Op:
# 5*1 =5
# 5*2 = 10
# .
# .
# 5*10= 50
# Do you want to continue press yes else no
num = int(input("Enter table name: "))
limit = int(input("Enter the limit: "))

for i in range(1, limit + 1):
    print(num, "*", i, "=", num * i)