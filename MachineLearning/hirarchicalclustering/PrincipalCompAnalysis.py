from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
x = iris.data

#standardize data
x_std = StandardScaler().fit_transform(x)

#create covariance matrix
cov_mat = np.cov(x_std.T)

print('Covariance matrix \n%s' % cov_mat)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
print('Eigenvectors \n%s' % eig_vecs)
print('\nEigenvalues \n%s' % eig_vals)

#sort eigenvalues in descending order
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]

#selecting the number of principal components
tot = sum(eig_vals)
var_exp = [(i / tot) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print("Cummulative Variance Explained", cum_var_exp)

#plotting the graphics
plt.figure(
    figsize = (6, 4)
    )

plt.bar(
    range(4),
    var_exp,
    alpha = 0.5,
    align = 'center',
    label = 'Individual explaind variance'
    )
plt.step(
    range(4),
    cum_var_exp, where = 'mid',
    label = 'Cummulative explained variance'
)
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc = 'best')
plt.tight_layout
plt.show()