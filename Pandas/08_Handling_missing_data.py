import pandas as pd

"""
What is Missing Data ?
NaN → Not a Number (most common)
None → Python null value
NaT → Not a Time (for datetime)
"""
data = {
    'Name': ['Aarav', 'Priya', None,'boss'],
    'Age': [18, None, 20, None],
    'Marks': [None, 90, 78,90]
}

df = pd.DataFrame(data)
print(df)

# print(df.isna())   # returns a boolean DataFrame
# print(df.isna().sum()) # returns count of missing values in each column
"""
Output:
    Name    Age  Marks
0  False  False   True
1  False   True  False
2   True  False  False
3  False   True  False
Name     1
Age      2
Marks    1
dtype: int64
"""

# print(df.dropna(axis=0, inplace=False))  # drop column having missing values
# print(df.dropna(axis=1))  # drop row having missing values
# df.dropna(how="all")  # Drop only if ALL values are missing

# df.fillna(900, inplace=True) # fill all missing values with a singl value
# print(df)

# df['Age'].fillna(df.Age.mean(), inplace=True)
# df['Marks'].fillna(df.Marks.mean(), inplace=True)
# print(df)

