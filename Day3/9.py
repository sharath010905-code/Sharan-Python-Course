import numpy as np

seats = np.zeros((10, 10), dtype=int)

seats[0][1] = 1
seats[2][3] = 1
seats[2][5] = 1
seats[4][4] = 1
seats[7][8] = 1

total_booked = 0
for i in range(10):
    for j in range(10):
        if seats[i][j] == 1:
            total_booked += 1

row = 2
row_booked = 0
for j in range(10):
    if seats[row][j] == 1:
        row_booked += 1

print("Total booked seats:", total_booked)
print("Booked seats in 3rd row:", row_booked)