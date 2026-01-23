import numpy as np
import pandas as pd

ser = pd.Series(['a', np.nan, 1, np.nan, 2])
print(ser.notnull().sum())