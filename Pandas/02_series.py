import pandas as pd

# Create a Series from a list
# pd.Series(data, index=None, dtype=None, name=None, copy=False, fastpath=False)
s = pd.Series([10, 20, 30, 40, 50], name='scores')
print(s)

# access by index
print(s[2])   # Output: 30

# Create a Series with custom index
s = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
print(s)

# access by label
print(s['B'])   # Output: 20

#  access by position
print(s.iloc[2])   # Output: 20

#  access by label
print(s.loc['A'])   # Output: 20

# aggregation functions
print("sum :",s.sum())  # Output: 60
print("mean: ",s.mean()) # Output: 20.0
print("max:",s.max())  # Output: 30
print("min:",s.min())  # Output: 10
print("count:",s.count())  # Output: 5
print(s.value_counts())  # Count occurrences of each value