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


# to check the unique values

unique_Age = df['Age'].unique()
print(unique_Age)

# to count the unique values
print(df['Age'].value_counts())