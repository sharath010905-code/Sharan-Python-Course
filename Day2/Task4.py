data = [(1,2,3), (4,5,6), (7,8,9)]
k = int(input("Enter k value: "))

if k < 0 or k >= len(data[0]):
    print("Invalid column index")
else:
    product = 1
    for t in data:
        product = product * t[k]

    print("Product of values in column", k, ":", product)