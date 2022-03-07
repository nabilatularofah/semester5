import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#meload dataset dari file cvs dan mengekstrak fitur dan label classnya
irisdataset = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_widht', 'petal_length', 'petal_widht', 'label'], header=0)
fitur = irisdataset.iloc[:, 0:2].values
label = irisdataset.iloc[:, -1].values

#mengambil alhoritma K Nearest Neighbors sebagai model
model = KNeighborsClassifier(n_neighbors=3)

#latih model menggunakan data yang dimasukan
model.fit(fitur, label)

#prediksi dengan data yang dimasukan
lengthinput = input("berapa panjang sepal ? \n " + ">>>")
widhtinput = input ("berapa lebar sepal ? \n " + ">>>")
lengthdata = float(lengthinput)
widhtdata = float(widhtinput)

prediksinya = model.predict([[lengthdata,widhtdata]])
if prediksinya == 0 :
    print ("Iris-setosa")
elif prediksinya == 1 :
    print ("Iris-versicolor")
else :
    print ("Iris-virginica")