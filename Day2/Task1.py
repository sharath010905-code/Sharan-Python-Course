n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements in the array: ").split()))

mode = "none"

for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count += 1
    if count > 1:
        mode = i
        break

print("The mode of the array is", mode)