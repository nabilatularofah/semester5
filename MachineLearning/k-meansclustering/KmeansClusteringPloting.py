from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

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

#K-Means Cluster
model = KMeans(n_clusters=3, random_state=11)
model.fit(x)

#since its unsupervised the labels have been assigned
#not in line with the actual labels so convert all the 1s to 0s and 0s to 1s
#2's look fine
iris['pred_species'] = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)

#membuat ukuran gambar dengan sumbu 'ax1' berukuran 2x2
fig, ax1 = plt.subplots(2, 2, figsize=(22, 18), gridspec_kw={'hspace': 0.5, 'wspace':0.2})

colorplot = dict({0.0:'red', 0:'red', 1.0:'green', 1:'green', 2.0:'blue', 2:'blue'})

#plot sepal
sns.scatterplot(data=iris, x='sepallength(cm)', y='sepalwidth(cm)', hue='species', legend='full', ax=ax1[0, 0], palette=colorplot).set_title('Sepal (Actual)')
sns.scatterplot(data=iris, x='sepallength(cm)', y='sepalwidth(cm)', hue='pred_species', legend='full', ax=ax1[0, 1], palette=colorplot).set_title('Sepal (Predicted)')

#plot petal
sns.scatterplot(data=iris, x='petallength(cm)', y='petalwidth(cm)', hue='species', legend='full', ax=ax1[1, 0], palette=colorplot).set_title('Petal (Actual)')
sns.scatterplot(data=iris, x='petallength(cm)', y='petalwidth(cm)', hue='pred_species', legend='full', ax=ax1[1, 1], palette=colorplot).set_title('Petal (Predicted)')

#show the figure of plot
plt.show()