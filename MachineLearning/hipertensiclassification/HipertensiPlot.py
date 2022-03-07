import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

HipertensiDataset = pd.read_csv('hipertensi.csv', names=['umur (tahun)', 'kegemukan(kg)', 'label'], header=0, sep=",")

sns.scatterplot(x='umur (tahun)', y='kegemukan(kg)', hue='label', data=HipertensiDataset).set_title ('sehat or hipertensi')
plt.figure(1)
plt.show()
