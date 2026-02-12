for i in range(1,4):
    for j in range(i):
        print("*",end="");
    print();
for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="");
    print();
rows=4
col=5
for i in range(rows):
    for j in range(col):
        if i==0 or i==rows-1 or j==0 or j==col-1:
            print("*",end="");
        else:
            print(" ",end="");
    print();