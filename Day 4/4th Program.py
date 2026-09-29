#4. Write a python program using pivot function

import pandas as pd

data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04'],
    'Team': ['CSK', 'MI', 'CSK', 'MI'],
    'Venue': ['Chennai', 'Mumbai', 'Mumbai', 'Chennai'],
    'Runs': [180, 195, 165, 175]
}

df = pd.DataFrame(data)
print("\nOrginal Dataframe\n")
print(df)

pivot_df = df.pivot_table(
    index = 'Date',
    columns='Team',
    values='Runs'
)

print("\nReshaped DataFrame\n")
print(pivot_df)