"""
============================
Gaussian Naive Bayes
============================

A classification example using Gaussian Naive Bayes (GaussianNB).

"""

################################################################################
# import some data to play with

# The IRIS dataset
from scikits.learn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

################################################################################
# GaussianNB
from scikits.learn.naive_bayes import GaussianNB
gnb = GaussianNB()

y_pred = gnb.fit(X, y).predict(X)

print "Number of mislabeled points : %d" % (y != y_pred).sum()
