import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

irisdataset = pd.read_csv('iris.csv',names = ['sepal_length', 'sepal_widht','petal_length','petal_widht','label'],header = 0, sep =',')

sns.scatterplot (x = 'sepal_length', y = 'sepal_widht', hue = 'label', data = irisdataset).set_title('Sepal Length & Sepal Widht')
plt.figure(1)
plt.show()