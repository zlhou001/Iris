from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

fig, ax = plt.subplots()

for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax.scatter(features[target ==t,0], features[target == t, 1], marker = marker, c =c)

ax.set_xlabel('sepal length in cm')
ax.set_ylabel('sepal width in cm')
plt.show()
