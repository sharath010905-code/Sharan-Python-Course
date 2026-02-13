import pandas as pd 
import matplotlib.pyplot as plt


df=pd.read_csv('student.txt')
print(df)

print(df["Marks"].sum())
print(df["Marks"].min())
print(df["Marks"].max()) 

print("reterive with condition")

greater_than70=df[df["Marks"]>70]
print(f"studnets {greater_than70}")

print("----------graph-------")
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()