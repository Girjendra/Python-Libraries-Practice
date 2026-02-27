import pandas as pd

df = pd.read_csv("students_data.csv",)
# print(df)

df = pd.read_json("students_data.json") 
# print(df)

# # openpyxl — Pandas uses it internally to handle excel files
df = pd.read_excel("students_data.xlsx")
# print(df)

# Creating a DataFrame from scratch
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'number_of_courses': [5, 3, 4]
}

df = pd.DataFrame(data, index=[4,3,6], columns=['Age', 'City'])
# print(df)

# Saving DataFrames to different file formats
# Format : .to_csv(filename, index=Boolean)
df.to_csv("students_data2.csv", index=False)
df.to_json("students_data2.json", orient='split')
df.to_excel("students_data2.xlsx")