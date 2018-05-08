import pandas as pd
import numpy as np

a = pd.DataFrame(np.arange(20).reshape(5, 4))
print a
b = np.random.permutation(5)
print b

c = a.take(b)[:3]
print c 
