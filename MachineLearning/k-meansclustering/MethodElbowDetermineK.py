from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist, pdist

iris = datasets.load_iris()

#convert to dataframe
iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['species'])

#remove spaces from column name
iris.columns = iris.columns.str.replace(' ', '')
iris.head()

x = iris.iloc[:, :3]    #independent variables
y = iris.species    #depenedent varibles
sc = StandardScaler()
sc.fit(x)
x = sc.transform(x)

K = range(1, 10)
KM = [KMeans(n_clusters=k).fit(x) for k in K]
centroids = [k.cluster_centers_ for k in KM]

D_k = [cdist(x, cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D, axis=1) for D in D_k]
dist = [np.min(D, axis=1) for D in D_k]
avgWithinSS = [sum(d)/x.shape[0] for d in dist]

#total with-in sum of square
wcss = [sum(d**2) for d in dist]
tss = sum(pdist(x)**2)/x.shape[0]
bss = tss-wcss
varExplained = bss/tss*100

kIdx = 10-1
##### plot ###
kIdx = 2

#elbow curve
#sset the size of the plot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(K, avgWithinSS, 'b*-')
plt.plot(K[kIdx], avgWithinSS[kIdx],marker='o', markersize=12, markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of square')
plt.title('Elbow for KMeans clustering')

plt.subplot(1, 2, 2)
plt.plot(K, varExplained, 'b*-')
plt.plot(K[kIdx], varExplained[kIdx], marker='o', markersize=12, markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Percentage of variance explained')
plt.title('Elbow for KMeanas clustering')

plt.tight_layout()
plt.show()