from sklearn import datasets, metrics
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

iris = datasets.load_iris()

#convert to dataframe
iris = pd.DataFrame(
    data = np.c_[iris['data'],
    iris['target']],
    columns = iris['feature_names'] + ['species']
)

print("Data awal iris : ")
print(iris) 

#remove spaces from column names
iris.columns = iris.columns.str.replace(' ', '')
iris.head()

x = iris.iloc[:, :3]
y = iris.species
sc = StandardScaler()
sc.fit(x)
x = sc.transform(x)

#Agglomerative Cluster
model = AgglomerativeClustering(n_clusters=3)
model.fit(x)

print(model.labels_) #cetak label hasil hierarchical clustering
iris['pred_species'] = model.labels_

#cetak akurasi dari hierarchical clustering
print("Akurasi : ", metrics.accuracy_score(iris.species, iris.pred_species))
print("Laporan Klasifikasi : ", metrics.classification_report(iris.species, iris.pred_species))


