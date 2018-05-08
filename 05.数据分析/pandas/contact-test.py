import pandas as pd

a1 = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
})

a2 = pd.DataFrame({
    'd': [10, 11]
})

b = pd.concat([a1, a2], axis=1)
print b

a3 = pd.DataFrame({
    'd': [12, 13, 14]
})

c = b.combine_first(a3)
print c 
