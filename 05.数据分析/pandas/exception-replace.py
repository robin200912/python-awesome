import pandas as pd
import numpy as np


a = pd.DataFrame(np.random.randn(1000, 5))
print a.describe()

a[np.abs(a) > 3] = np.sign(a) * 3
print a.describe() 
