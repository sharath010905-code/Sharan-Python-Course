import numpy as np

matrix = np.zeros((10, 10), dtype=int)

matrix[0][2] = 1
matrix[2][3] = 1
matrix[2][5] = 1
matrix[4][6] = 1
matrix[7][1] = 1

print("10 x 10 Matrix:")
print(matrix)

total_booked = 0
for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            total_booked += 1

row = 2
row_count = 0
for j in range(10):
    if matrix[row][j] == 1:
        row_count += 1

print("Total booked seats:", total_booked)
print("Booked seats in 3rd row:", row_count)