import pandas as pd

df  = pd.read_json("students_data.json")
# Display concise summary of the DataFrame
print(df.info())

"""
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   ID       4 non-null      float64
 1   Name     5 non-null      object 
 2   Age      5 non-null      int64  
 3   Subject  5 non-null      object 
 4   Marks    5 non-null      int64  
dtypes: float64(1), int64(2), object(2)
memory usage: 332.0+ bytes
None
"""