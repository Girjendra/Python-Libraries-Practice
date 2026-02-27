import pandas as pd

data = {
    'Name': ['Aarav', 'Priya', 'Rahul','boss'],
    'Age': [18, 23, 20, 18],
    'Marks': [82, 90, 78,90],
    "salary":[40000, 35000, 50000,90000]
}

df = pd.DataFrame(data)
print(df)

# print(df.sort_values(by=["Age", "Marks"], ascending=[True,False], inplace=False)) # Sorting by Values
# print(df.sort_values(by="Marks", ascending=False, inplace=False)) # Sorting by Values
# print(df.sort_index(ascending=False)) # Sorting by index

print(df["Age"].mean())
print(df["Marks"].mean())
print(df[["Marks", "Age", "salary"]].mean())
print(df.agg({
    'Marks': ["mean", "sum", "max", "min"],
    'Age':["mean", "sum", "max", "min"]
}))