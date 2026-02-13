import numpy as np
import pandas as pd
df=pd.read_csv('student.txt')
print(df)

print(df["Marks"].sum())
print(df["Marks"].min())
print(df["Marks"].max())