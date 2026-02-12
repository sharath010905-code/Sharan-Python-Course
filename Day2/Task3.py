n = int(input())
arr = list(map(int, input().split()))

if n < 2:
    print("Not applicable")
else:
    largest = arr[0]
    second_largest = None

    for i in range(1, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest:
            if second_largest is None or arr[i] > second_largest:
                second_largest = arr[i]

    if second_largest is None:
        print("Not applicable")
    else:
        print(second_largest)