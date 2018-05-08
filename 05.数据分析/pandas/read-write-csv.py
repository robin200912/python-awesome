import pandas as pd

a = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
}, index=['d1', 'd2', 'd3'])
a.index.name = 'dd'

print a
a['d'] = pd.Series({'d1': 4, 'd2': 4})
print a

a.to_csv('test.csv')

b = pd.read_csv('test.csv')
print b

b = pd.read_csv('test.csv', names=['dd', 'a1', 'a2', 'a3', 'a4'], index_col=['dd']
                ,header=None)
print b
print b.index
print b.columns


e = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
}, index=['d1', 'd2', 'd3'])

e.to_csv('test2.csv', index=False, columns=['a', 'c'])
f = pd.read_csv('test2.csv')
print f 


