import pandas as pd
import numpy as np

a = pd.DataFrame({
    'a': np.arange(1, 4),
    'b': np.arange(4, 7),
    'c': np.arange(7, 10),
    'd': np.random.uniform(-5, 5, 3)
})
print a

b = (a - a.min()) / (a.max() - a.min())
print b

c = (a - a.mean()) / a.std()
print c

d = a / 10 * np.ceil(np.log10(a.abs().max()))
print d 
