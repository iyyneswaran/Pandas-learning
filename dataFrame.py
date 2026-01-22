import pandas as pd

fruits = {
    'Apples': [30, 21, 15, 12],
    'Bananas': [21, 34, 30, 35],    
    'Cherries': [15, 25, 30, 45]
}

fruits = pd.DataFrame(fruits, index=['2018 Sales', '2019 Sales', '2020 Sales', '2021 Sales'])

print(fruits)