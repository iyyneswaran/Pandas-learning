import pandas as pd
import numpy as np

# Data Frame 
data = {
    "Name": ['Iyynes', 'Adithya', 'Deepa', 'Muthu', 'Sri', 'Gobika', np.nan],
    "Age": [20, 15, 18, np.nan, 19, 18, np.nan],
    "Department": ['Full-stack', np.nan, 'UI/UX', 'Backend', 'Frontend', 'AI', np.nan],
    "Salary": [90000, 70000, 80000, 90000, np.nan, 55000, np.nan]
}

df = pd.DataFrame(data)
df['Promoted Salary'] = df['Salary'] + 15000
print(df)

# to check the number of null values
print('\n True for null and vice versa \n', df.isnull(), sep='\n') #returns true of false

# to count the null values
print('\n Count of null values in each column \n', df.isnull().sum(),sep='\n')

df.dropna()
# or 
df.dropna(how='any') #drops the row with any null value, I mean if there's a single null value then the row is eliminated.

print("\n Dataset without null values \n", df.dropna(how='any'))

# to drop the rows with all values as null:
df.dropna(how='all')
print('\n dataset without all values in a row as null', df.dropna(how='all'), sep='\n')