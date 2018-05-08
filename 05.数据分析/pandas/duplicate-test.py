import pandas as pd

a = pd.DataFrame({
    'a': [1, 2, 1],
    'b': [4, 5, 4],
    'c': [7, 8, 8]
})
print a

a.drop_duplicates(['a', 'b'], inplace=True, keep='last')
print a
 
