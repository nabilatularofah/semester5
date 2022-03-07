from sklearn import datasets
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

iris = datasets.load_iris()
y = iris.target

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(
    fig,
    elev = -150,
    azim = 110
    )
x_reduced = PCA(n_components = 3).fit_transform(iris.data)
ax.scatter(
    x_reduced[:, 0],
    x_reduced[:, 1],
    x_reduced[:, 2],
    c = y,
    cmap = plt.cm.Paired
    )
ax.set_title("First three PCA direction")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])
plt.show()