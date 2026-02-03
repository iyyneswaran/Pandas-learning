# joins => left, right, outer , inner
# merge similar to joins

# consider two datasets A and B:
# for left join, whatever data present in both A and B is ignored and whatever unique datas that present only in the B is also ignored
# therefore the data which is available only in the A is considered

# right join is the opposite of left join


# Outer join: everything of A and B is included
# inner join: only the common data in A and B is included

# merge: all the data present in both A and B is included

import pandas as pd
import numpy as np

department_info = {
    "Department": ['HR', 'IT', 'Finance'],
    "Location": ['New York', 'San Francisco', 'Chicago'],
    "Manager": ['Laura', 'Steve', 'Nina']
}

df1 = pd.DataFrame(department_info)

data = {
    "Name": ['Iyynes', 'Adithya', 'Deepa', 'Muthu', 'Sri', 'Gobika', np.nan, 'Iyynes'],
    "Age": [20, 15, 18, np.nan, 19, 18, np.nan, 20], 
    "Department": ['Full-stack', np.nan, 'UI/UX', 'Backend', 'Frontend', 'AI', np.nan, 'Full-stack'],
    "Salary": [90000, 70000, 80000, 90000, np.nan, 55000, np.nan, 90000]
}

df2 = pd.DataFrame(data)


print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))

print("\n")
print("\n")
print("\n")

print(pd.merge(df1, df2, on='Department'))