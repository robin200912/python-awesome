import pandas as pd

a = pd.DataFrame({
    'date': ['5-1', '5-1', '5-2', '5-2'],
    'item': ['price', 'sum', 'price', 'sum'],
    'value': [4.2, 44, 5.5, 66]
})
print a

b = a.pivot('date', 'item', 'value')
print b 

