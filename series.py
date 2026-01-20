import pandas as pd
s = pd.Series([1, 2, 3, 4, 5])
print(s)


index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
s.index = index
print(s)