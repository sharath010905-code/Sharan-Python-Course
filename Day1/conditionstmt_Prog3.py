input_data = input("Enter the dimensions of the chocolate (n m): ")
n, m = input_data.split()
n = int(n)
m = int(m)
if (n * m - 1) % 2 == 1:
    print("Yes")
else:
    print("No")
