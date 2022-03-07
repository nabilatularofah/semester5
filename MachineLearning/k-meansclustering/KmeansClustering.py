from sklearn import datasets, metrics
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris() #mengambil dataset iris dari sklearn

#convert to dataframe
iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['species'])

print("Data awal iris : ")
print(iris) #cetak header kolo sebelum dirubah spasi (nama kolom masih pake spasi)

#remove spaces from column name
iris.columns = iris.columns.str.replace(' ', '')    #menghilnagkan spasi pada header kolom
iris.head() #update nama header kolom yang baru tanpa spasi

x = iris.iloc[:, :3]    #independent variables, dimana data mulai dari kolom 0 s.d 3
y = iris.species    #depenedent varibles, dimana adalah lebel berupa kolom species
sc = StandardScaler()
sc.fit(x)
x = sc.transform(x)

#K-Means Cluster
model = KMeans(n_clusters=3, random_state=11)    #terapkan  model ke algoritma K-Means
model.fit(x)
print("label hasil clustering KMeans adalah : ")
print(model.labels_)    #cetak lebel hasil pembuatan oleh K-Means

#menambahkan data ke dataframe yang ada untuk kolom pred_species hasil clustering K-Means
iris['pred_species'] = np.choose(model.labels_, [1,0,2]).astype(np.int64)

#mencetak akurasi prediksi clustering dam laporan klasifikasi
print("Accuracy :", metrics.accuracy_score(iris.species, iris.pred_species))
print("Classification report :", metrics.classification_report(iris.species, iris.pred_species))

#mencetak score homogenety hasil cluster antara species prediksi dengan species aktual
#jika bernilai mendekasi 0.0 amka homogen(bagus), jika mendekati 1.0 maka tidak homogen (jelek)
print("homogeneity score : ", metrics.homogeneity_score(y, iris['pred_species']))

#menghitung score homogeneity dan completeness dan V-Measure sekaligus
#sebuahk klaster memenuhi homogeneitas jika semua klasternya hanya berisi titik data yang merupakan anggota dari satu kelas
#semua klaster memenuhi completeness jika semua titik data yang menjadi anggota kelas tertentu adalah elemen dari klaster yang sama
# #kedua skor (V-Measure) memiliki nilai positif antar 0.0 dan 1.0, nilai yang lebih besar diinginkan (bagus)
print("homogeneity, completeness, v-measure : ", metrics.homogeneity_completeness_v_measure(y, iris['pred_species'], beta=1.0))

print("cetak data iris denga full rows:")
pd.set_option('display.max_rows', None) #menghilangkan default cetak max rows dari pandas
print(iris) #emncetak semua baris data, bandingkan kolom species (aktual) dengan pred_species (hasil cluster)

print("cetak data iris dengan sampel acak sebesar 0.3 :")
print(iris.sample(frac=0.3))
