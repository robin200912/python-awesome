from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

print X
print y

knn = KNeighborsClassifier()
knn.fit(X, y)

# validate
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print scores
print scores.mean()
