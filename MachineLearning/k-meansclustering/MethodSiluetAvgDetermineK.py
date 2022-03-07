from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.metrics import silhouette_score, silhouette_samples

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

score = []
for n_clusters in range(2, 10):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(x)
    score.append(silhouette_score(x, kmeans.labels_))

#set the size of the pyplot
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(score)
plt.grid(True)
plt.ylabel("Silhouette Score")
plt.xlabel("k")
plt.title("Silhouette for K-means")

#initialize the clusterer with n_clusters value and a random generator
model = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=0)
model.fit_predict(x)
cluster_labels = np.unique(model.labels_)
n_clusters = cluster_labels.shape[0]

#compute the silhouette score for each sample
silhouette_vals = silhouette_samples(x, model.labels_)

plt.subplot(1, 2, 2)
y_lower, y_upper = 0,0
yticks = []
cmap = cm.get_cmap("Spectral")
for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[model.labels_ == c]
    c_silhouette_vals.sort()
    y_upper = y_lower + len(c_silhouette_vals)
    color = cmap(float(i) / n_clusters)
    plt.barh(range(y_lower, y_upper), c_silhouette_vals, facecolor=color, edgecolor=color, alpha=0.7)
    yticks.append((y_lower + y_upper) / 2)
    y_lower = y_upper + 10

silhouette_avg = np.mean(silhouette_vals)

plt.yticks(yticks, cluster_labels + 1)

#the vertical line for average silhouette score of all teh values
plt.axvline(x=silhouette_avg, color='red', linestyle='--')

plt.ylabel('Cluster')
plt.xlabel('Silhouette coefficient')
plt.title("Silhouette for K-means")
plt.show()
