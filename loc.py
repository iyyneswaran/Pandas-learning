import pandas as pd

calories = pd.Series([420, 380, 390, 500, 600, 235], index=['apple', 'banana', 'orange', 'mango', 'kiwi', 'pine apple'], name='Calories')

# loc is label based indexing

print(calories.loc['apple'])

# accessing multiple values using loc 
print(calories.loc[['apple', 'banana', 'orange']])

# In label based indexing your start as well as stop value both are included in the output.
print(calories['banana':'kiwi'])
