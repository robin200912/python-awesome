import pandas as pd
import numpy as np

a = pd.DataFrame({
    'a': np.arange(1, 4),
    'b': np.arange(4, 7),
    'c': np.arange(7, 10),
})

a.rename(index={0: '00'}, columns={'a': 'aa'}, inplace=True)
print a 
