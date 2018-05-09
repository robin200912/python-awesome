import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sklearn.datasets import make_classification
import matplotlib.pyplot as plt


X, y = make_classification(
    n_samples=300, n_features=2,
    n_redundant=0, n_informative=2,
    random_state=22, n_clusters_per_class=1,
    scale=100)

plt.scatter(X[:, 0], X[:, 1], c=y)

plt.show()

