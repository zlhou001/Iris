from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

fig1, ax1 = plt.subplots()
for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax1.scatter(features[target ==t,0], features[target == t, 1], marker = marker, c =c)

ax1.set_xlabel('sepal length in cm')
ax1.set_ylabel('sepal width in cm')
plt.show()
plt.savefig('sepal_length_with_sepal_length.pdf')

fig2, ax2 = plt.subplots()
for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax2.scatter(features[target ==t,0], features[target == t, 2], marker = marker, c =c)

ax2.set_xlabel('sepal length in cm')
ax2.set_ylabel('petal length in cm')
plt.show()
plt.savefig('sepal_length_with_petal_length.pdf')

fig3, ax3 = plt.subplots()
for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax3.scatter(features[target ==t,0], features[target == t, 3], marker = marker, c =c)

ax3.set_xlabel('sepal length in cm')
ax3.set_ylabel('petal width in cm')
plt.show()
plt.savefig('sepal_length_with_petal_width.pdf')

fig4, ax4 = plt.subplots()
for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax4.scatter(features[target ==t,1], features[target == t, 2], marker = marker, c =c)

ax4.set_xlabel('sepal width in cm')
ax4.set_ylabel('petal length in cm')
plt.show()
plt.savefig('sepal_width_with_petal_length.pdf')

fig5, ax5 = plt.subplots()
for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax5.scatter(features[target ==t,1], features[target == t, 3], marker = marker, c =c)

ax5.set_xlabel('sepal width in cm')
ax5.set_ylabel('petal width in cm')
plt.show()
plt.savefig('sepal_width_with_petal_width.pdf')

fig6, ax6 = plt.subplots()
for t, marker, c in zip(range(3), ">ox", "rgb"):
    ax6.scatter(features[target ==t,2], features[target == t, 3], marker = marker, c =c)

ax6.set_xlabel('petal length in cm')
ax6.set_ylabel('petal width in cm')
plt.show()
plt.savefig('petal_length_with_petal_width.pdf')
