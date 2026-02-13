import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vehicle_sales.csv")

print(df)
print(df.shape)

print("\nRegion wise sales:")
print(df.groupby("Region")["Units_Sold"].sum())

print("\nCity wise sales:")
print(df.groupby("City")["Units_Sold"].sum())

print("\nCategory wise sales:")
print(df.groupby("Category")["Units_Sold"].sum())

print("\nVehicle wise sales:")
print(df.groupby("Vehicle_Type")["Units_Sold"].sum())

print("\nTotal revenue by category:")
print(df.groupby("Category")["Revenue"].sum())

print("\nTop selling city:")
print(df.groupby("City")["Units_Sold"].sum().idxmax())

print("\nEV sales only:")
print(df[df["Category"] == "EV"])

df.groupby("Category")["Units_Sold"].sum().plot(kind="bar")
plt.title("Vehicle Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Units Sold")
plt.show()

df.groupby("Region")["Revenue"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Region Wise Revenue Share")
plt.show()