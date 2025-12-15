import pandas as pd


df1 = pd.DataFrame({
    'Name': ['Strom, Mrs. Wilhelm (Elna Matilda Persson)', 'Navratil Mr. Michel ("Louis M Hoffman)', 'Minahan, Miss. Daisy E', 'Navratil Mr. Michel ("Louis M Hoffman)'],
    'Age': [29, 36.5, 33, 36.5],
    'Sex': ['female', 'male', 'female', 'male']
})


print(df1.drop_duplicates())

print(df1.groupby('Age').size())
print(df1.groupby("Name").sum())
print(df1.groupby['Age','Sex'].size())