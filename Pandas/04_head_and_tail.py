import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json("students_data.json")

# Display the first 3 rows and the last 2 rows of the DataFrame and default is 5 for both
print(df.head(3))
print(df.tail(2))