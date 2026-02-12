table=int(input("Enter the table name:"))
limit=int(input("Enter the table limit:"))
for i in range(1,limit+1):
    print(table,"*",i,"=",table*i)