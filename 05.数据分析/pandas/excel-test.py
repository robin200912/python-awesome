import pandas as pd

a = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})

a.to_excel('test.xls')

b = pd.ExcelFile('test.xls')
c = b.parse()
print type(c)
print c 

