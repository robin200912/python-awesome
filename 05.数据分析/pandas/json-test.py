import json
import pandas as pd


a = json.loads('[{"a": 1}]')
print a, type(a)

b = json.dumps(a)
print b, type(b)

c = pd.DataFrame(a)
print c 

