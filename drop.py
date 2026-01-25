import pandas as pd
import numpy as np

# Data Frame 
data = {
    "Name": ['Iyynes', 'Adithya', 'Deepa', 'Muthu', 'Sri', 'Gobika'],
    "Age": [20, 15, 18, np.nan, 19, 18],
    "Department": ['Full-stack', np.nan, 'UI/UX', 'Backend', 'Frontend', 'AI'],
    "Salary": [90000, 70000, 80000, 90000, np.nan, 55000]
}

df = pd.DataFrame(data)
print(df)

df.drop('Age', axis=1, inplace=True) #erase the table in place, when inplcae = True
print(df)


# to find the shape of the dataframe:
print(df.shape)

# info
print(df.info())

# describe: to get statistical summary
print(df.describe())