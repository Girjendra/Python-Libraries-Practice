import pandas as pd

data = {
    'Name': ['Aarav', 'Priya', 'Rahul','boss'],
    'Age': [18, 23, 20, 18],
    'Marks': [82, 90, 78,90],
    "salary":[40000, 35000, 50000,90000]
}

df = pd.DataFrame(data)
print(df)

print(df.groupby("Age")["salary"].sum())
print(df.groupby("Age").agg({"Marks":["mean","sum"], "salary":["max", "min"]}))
print(df.groupby("Age")["salary"].sum().sort_values(ascending=True))