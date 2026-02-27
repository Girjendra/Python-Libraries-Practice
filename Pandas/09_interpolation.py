import pandas as pd
# Interpolation : interpolation is used to estimate missing values (NaN) based on existing 
#                 data patterns instead of deleting or filling with constants.
# df.interpolate(method="linear")

data = {
    'Name': ['Aarav', 'Priya', None,'boss'],
    'Age': [18, None, 20, None],
    'Marks': [None, 90, 78,90]
}

df = pd.DataFrame(data)
print(df)

# | axis     | Meaning                                   |
# | -------- | ----------------------------------------- |
# |  axis=0  | **Column-wise (vertical)** ⬇️ *(default)* |
# |  axis=1  | **Row-wise (horizontal)** ➡️              |

df['Age'] = df['Age'].interpolate(method='linear', axis=0)
print(df)