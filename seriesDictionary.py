import pandas as pd

fruit_protein = { 
    "Avacado": 2.0,
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
}

s2 = pd.Series(fruit_protein, name='Protein')
# print(s2)


# conditional selection
# print(s2>1)
#returns true or false

# logical operators

# AND operator: 
# True and True => True
# True and False => False
# False and False => False

# AND => &
# OR => |
# NOT ~

# OR operator
# True or True => True
# True or False => True
# False or False => False

# and operator
print(s2[(s2>0.5) & (s2<2)])

# or operator
print(s2[(s2>0.5) | (s2<2)])

# not operator
print(s2[~(s2>1)])

