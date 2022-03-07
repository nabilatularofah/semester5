from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import cophenet, dendrogram, linkage
from scipy.spatial.distance import pdist
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()

#convert to dataframe
iris = pd.DataFrame(
    data = np.c_[iris['data'],
    iris['target']],
    columns = iris['feature_names'] + ['species']
)

#remove spaces from column names
iris.columns = iris.columns.str.replace(' ', '')
iris.head()

x = iris.iloc[:, :3]
y = iris.species
sc = StandardScaler()
sc.fit(x)
x = sc.transform(x)

#generete the link matrix
z = linkage(x, 'ward')
c, coph_dists = cophenet(z, pdist(x))

#calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Agglomerative Hierarchical Clustering Dendogram')
plt.xlabel('sample indeks')
plt.ylabel('distance')
dendrogram(
    z,
    leaf_rotation = 90.,    #rotates the x axis labels
    leaf_font_size = 8.,    #font size the x labels
)
plt.tight_layout()
plt.show()