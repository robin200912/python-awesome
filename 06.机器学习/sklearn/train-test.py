import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sklearn.datasets import make_classification
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVC


X, y = make_classification(
    n_samples=300, n_features=2,
    n_redundant=0, n_informative=2,
    random_state=22, n_clusters_per_class=1,
    scale=100)

X = preprocessing.scale(X)
plt.scatter(X[:, 0], X[:, 1], c=y)

# test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
m = SVC()
m.fit(X_train, y_train)
print m.score(X_test, y_test)

plt.show()

