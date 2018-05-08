import pandas as pd
import numpy as np

a = pd.DataFrame({
    'a': np.arange(1, 4),
    'b': np.arange(4, 7),
    'c': np.arange(7, 10)
})
print a

a['a+1'] = a['a'].map(lambda x: x + 1)
a['b*2'] = a['b'].map(lambda x: x * 2)

print a 
