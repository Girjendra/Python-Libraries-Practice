import pandas as pd

data = {
    'Name': ['Aarav', 'Priya', 'Rahul','boss'],
    'Age': [18, 19, 20,18],
    'Marks': [85, 90, 78,90]
}

# pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
df = pd.DataFrame(data)
# print(df)

# print("Single column (Series):")
# print(df['Name'])                # Single column: returns a Series of names
# Output:
# 0    Aarav
# 1    Priya
# 2    Rahul
# Name: Name, dtype: object

# print("\nMultiple columns (DataFrame):")
# print(df[['Name', 'Marks']])     # Multiple columns: returns a DataFrame with selected columns
# Output:
#     Name  Marks
# 0  Aarav     85
# 1  Priya     90
# 2  Rahul     78

# print("\nRow by label/index value (loc=1):")      # df.loc[row_label, column_label]
# print(df.loc[1])                                  # Row by Label-based indexing -> second row as Series
# Output:
# Name     Priya
# Age         19
# Marks       90
# Name: 1, dtype: object

# print("\nRow by integer position (iloc=0):")  # df.iloc[row_position, column_position]
# print(df.iloc[0])                             # Row by Integer-position based indexing (0-based) -> first row as Series
# Output:
# Name    Aarav
# Age        18
# Marks      85
# Name: 0, dtype: object

# getting shape of dataframe
# print("shape:",df.shape)

# adding a new column
# df["Grade"] = ["A", "B", "C", "D"]
# df.insert(3, 'Grade',  ["A", "B", "C", "D"]) # df.insert(loc, column, value)
# print("After adding Grade column:")
# print(df)

# grouping by Age and calculating mean Marks
# print("Mean Marks grouped by Age:")
# print(df.groupby('Age')['Marks'].mean())

#  accessing columns
# print(df.loc[0, 'Age'])
# print(df.iloc[0, 1])

# print(df.loc[0:1, ['Age', 'Marks']])   # Both start and end are inclusive
# print(df.iloc[0:2,1:3])  #Slicing is start inclusive, end exclusive

# deleting a column
# df.drop('Age', axis=1, inplace=True)
# df.drop(columns=['Age', 'Name'], inplace=True) # or MUltiple
# df.drop(columns='Age', inplace=True) # or single
# print("After deleting Age column:")
# print(df)

# deleting a row
# print("After deleting row with index 0:")
# print(df.drop(1))