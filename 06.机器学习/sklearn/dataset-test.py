import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sklearn.datasets import make_regression, make_classification
import matplotlib.pyplot as plt

X, y = make_regression(100, n_features=1, n_targets=1, noise=10)

print X
print y

plt.scatter(X, y)

plt.show()

