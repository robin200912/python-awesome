import pandas as pd

a = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})

a.to_json('test.json')

b = pd.read_json('test.json')
print type(b)
print b 
