import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from HipertensivalidationModelKNN import HipertensiDataset

#meload dataset dari file cvs dan mengekstrak fitur dan label classnya
HipertensiDataset = pd.read_csv('hipertensi.csv', names=['umur (tahun)', 'kegemukan(kg)', 'label'], header=0)
fitur = HipertensiDataset.iloc[:, 0:2].values
label = HipertensiDataset.iloc[:, -1].values

#mengambil alhoritma K Nearest Neighbors sebagai model
model = KNeighborsClassifier(n_neighbors=3)

#latih model menggunakan data yang dimasukan
model.fit(fitur, label)

#prediksi dengan data yang dimasukan
umurinput = input("Umur anda ? \n " + ">>>")
beratinput = input ("berat badan anda ? \n " + ">>>")
umurdata = float(umurinput)
beratdata = float(beratinput)

prediksinya = model.predict([[umurdata,beratdata]])
if prediksinya == 0 :
    print ("Sehat walafiat")
elif prediksinya == 1 :
    print ("Kena hipertensi")
else :
    print ("gak tau ahh")