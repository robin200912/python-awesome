import pandas as pd

a = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
b = pd.DataFrame({
                  'column1': {'d1': 1, 'd2': 2, 'd3': 3},
                  'column2': {'d1': 4, 'd2': 5, 'd3': 4}
                })
data = {
    'c2': [4, 5, 6],
    'c1': [7, 8, 9]
}
c = pd.DataFrame(data, index=['d1', 'd2', 'd3'], columns=['c1', 'c2'])

print a
print b
print c
print c.columns
print c.index

a['column3'] = [7, 8, 9]
print a

print b['column1']
print b.ix['d2']
b.ix['d4'] = [4, 4]
print b

b['column4'] = pd.Series({'d1': 7, 'd2': 9, 'd3': 8})
print b

del c['c1']
print c
print c.values
print c.T
 
