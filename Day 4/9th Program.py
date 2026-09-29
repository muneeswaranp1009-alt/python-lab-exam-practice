#9. Write a program to demonstrate functions in Python Library using Pandas

import pandas as pd 

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Marks': [85, 90, 78, 92]
}

df =pd.DataFrame(data)
print("\nData frame :\n",df)

print("\nShapes :",df.shape)
print('Column Names :',df.columns.tolist())

print('\nFilter(Age > 25):\n',df[df['Age'] > 25])

df['Pass'] = df['Marks'] > 80
print('\nAdding new Column:\n',df)

print('\nSorting :\n',df.sort_values('Marks',ascending=False))

print('\nAverage Mark :',df['Marks'].mean())