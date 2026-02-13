import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Emplyoee.csv")

print(df.head())
print(df.tail(3))
print(df.shape)

avg_salary = df["Salary"].mean()
print("Average Salary =", avg_salary)

max_salary = df["Salary"].max()
print(df[df["Salary"] == max_salary])

min_salary = df["Salary"].min()
print(df[df["Salary"] == min_salary])

print(df["Department"].value_counts())

high_salary = df[df["Salary"] > 50000]
print(high_salary)

print(df[df["Department"] == "IT"])
print(df[df["Experience"] > 5])
print(df[(df["Age"] >= 25) & (df["Age"] <= 35)])

print(df[(df["Department"] == "HR") & (df["Salary"] > 40000)])
print(df[(df["Department"] == "Sales") & (df["Experience"] > 3)])
print(df[(df["City"] == "Chennai") & (df["Salary"] < 30000)])

print(df.sort_values(by="Salary"))
print(df.sort_values(by="Experience", ascending=False))

print(df.groupby("Department")["Salary"].mean())
print(df["City"].value_counts())

df["Salary Status"] = df["Salary"].apply(lambda x: "High" if x > 50000 else "Low")

def seniority(exp):
    if exp >= 10:
        return "Senior"
    elif exp >= 5:
        return "Mid"
    else:
        return "Junior"

df["Seniority"] = df["Experience"].apply(seniority)

print(df)

df["Department"].value_counts().plot(kind="bar")
plt.show()

df["City"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.show()

df.sort_values("Salary")["Salary"].plot()
plt.show()

high_salary.to_csv("high_salary.csv", index=False)
df.groupby("Department")["Salary"].mean().to_csv("dept_avg_salary.csv")