import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Neha", "Rahul"]
})

df2 = pd.DataFrame({
    "stud_ID": [1, 2, 4],
    "Marks": [80, 90, 85]
})

# Concatenation means joining DataFrames or Series along rows or columns.
# df = pd.concat([df1, df2], axis=0,join="type of join", ignore_index=True/False)

print(pd.concat([df1, df2], axis=0,join="outer"))
"""
    ID   Name  stud_ID  Marks   
0  1.0   Amit      NaN    NaN   
1  2.0   Neha      NaN    NaN   
2  3.0  Rahul      NaN    NaN   
0  NaN    NaN      1.0   80.0   
1  NaN    NaN      2.0   90.0   
2  NaN    NaN      4.0   85.0
"""
print(pd.concat([df1, df2], axis=1,join="inner", ignore_index=True))
"""
   0      1  2   3
0  1   Amit  1  80
1  2   Neha  2  90
2  3  Rahul  4  85
"""

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5])

print(pd.concat([s1, s2], ignore_index=True))
"""
0    1
1    2
2    3
3    4
4    5
dtype: int64
"""

print(pd.concat([s1, s2]))
"""
0    1
1    2
2    3
0    4
1    5
dtype: int64
"""

# Merge combines DataFrames based on one or more common columns or keys, similar to SQL joins.
# Join combines DataFrames based on their index or a key column (less commonly).
# Concat stacks DataFrames along rows or columns without matching keys.