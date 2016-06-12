from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
result = []





""" Distinguish Iris Setosa"""

plength = features[:, 2]
is_setosa = (target == 0)

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

#print('Maximun of setosa: {0}.'.format(max_setosa))
#print('minimum of others: {0}.'.format(min_non_setosa))
for a in features[:, 2]:
    if  a < 2.0:
        print('Iris Setosa')
        result.append(0)
    #else: print('Iris Virginica or Veriscolour')

"""Distinguish Iris Virginica from Iris Versicolor """
features = features[~is_setosa]
target1 = target[~is_setosa]
virginica = (target1 == 2)

best_acc =-1.0
for fi in range(features.shape[1]):
    thresh = features[:, fi].copy()
    #thresh.sort()

    for t in thresh:
        pred = (features[:, fi] > t)
        acc = (pred == virginica).mean()
        #print(acc)
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
for a in features[:, best_fi]:
    if  a > best_t:
        print('Iris Virginica')
        result.append(2)
    else:
        print('Iris Veriscolour')
        result.append(1)



""" Model Test result"""
Accuracy = (result == target).mean()
print('Model Accuray is %f' % Accuracy) 

