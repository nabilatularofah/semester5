import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#meload dataset dari file csv dan mengekstrak fitur dan label classnya
irisdataset = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_widht', 'petal_length', 'petal_widht', 'label'], header=0)
fitur = irisdataset.iloc[:, 0:2].values
label = irisdataset.iloc[:, -1].values

#splitting the dataset into the training set dan test set
X_train, X_test, y_train, y_test = train_test_split(fitur, label, test_size = 1/3, random_state =0)
print("Data Training:")
print(X_train)
print("Data test:")
print(X_test)

#mengambil model K=3 Nearest Neighbor dan melatih model dengan X_train, y_train
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

#hitung akurasi dari model
akurasi = model.score(X_train, y_train)
print("Akurasi dari model adalah : {}".format(akurasi))