import pandas as pd

df = pd.read_csv("students_data.csv")

# Accessing shape and columns attributes
print(df.shape)
print(df.columns)

# print(df.index)
print(df.dtypes)

"""
Output:
(5, 5)
Index(['ID', 'Name', 'Age', 'Subject', 'Marks'], dtype='object')
RangeIndex(start=0, stop=5, step=1)
ID          int64
Name       object
Age         int64
Subject    object
Marks       int64
dtype: object
"""