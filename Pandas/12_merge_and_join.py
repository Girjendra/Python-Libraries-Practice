import pandas as pd

df = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Neha", "Rahul"]
})

df2 = pd.DataFrame({
    "stud_ID": [1, 2, 4],
    "Marks": [80, 90, 85]
})

# df = pd.merge(df1, df2, on="culumn_name", how="type of join")

# print(pd.merge(df1, df2, on="ID", how="inner"))
# print(pd.merge(df1, df2, on="ID", how="left"))
# print(pd.merge(df1, df2, on="ID", how="right"))
# print(pd.merge(df1, df2, how="cross")) # no on="ID" in cross
# print(pd.merge(df1, df2, on="ID", how="outer"))

# when column name are different
# print(pd.merge(df1, df2, left_on="ID", right_on="stud_ID", how="inner"))
# print(pd.merge(df1, df2, left_on="ID", right_on="stud_ID", how="left"))
# print(pd.merge(df1, df2, left_on="ID", right_on="stud_ID", how="right"))
# print(pd.merge(df1, df2, left_on="ID", right_on="stud_ID", how="outer"))

# Join Types-> it Joins based on the index by default
# print(df1.join(df2, how="inner"))
# df1.join(df2, how="left")
# df1.join(df2, how="right")
# df1.join(df2, how="outer")
# print(pd.merge(df1, df2, left_index=True, right_index=True))