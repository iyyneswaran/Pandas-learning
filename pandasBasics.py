import pandas as pd

calories = pd.Series([420, 380, 390, 500, 600, 235], index=['apple', 'banana', 'orange', 'mango', 'kiwi', 'pine apple'], name='Calories')
print(calories['apple'])


# print(calories.iloc['apple']) #error arise here, becuase we cant  use iloc here

print(calories.iloc[3])