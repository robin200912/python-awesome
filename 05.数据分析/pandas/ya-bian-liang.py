import pandas as pd

a = pd.DataFrame({
    'a': ['a', 'b', 'c'],
    'b': ['b', 'c', 'c']
})

print a
b = pd.get_dummies(a['a'])
print b
print pd.get_dummies(a['b'])
print pd.concat([a['a'], b], axis=1) 
