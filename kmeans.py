import  matplotlib.pyplot as plt
import numpy as np 
from sklearn.cluster import KMeans

plt.style.use('ggplot')

X = np.array([[1,2],
			[1.5,1.5],
			[5,8],
			[8,8],
			[1,0.6],
			[9,11]

	])


plt.scatter(X[:,0],X[:,1],s=50,linewidths=5,zorder=10)
plt.show()



classifier = KMeans(n_clusters=2)

classifier.fit(X)

centroids = classifier.cluster_centers_
labels = classifier.labels_


colors = ["g.","r.","c.","y."]

for i in range(len(X)):
	plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)

plt.scatter(centroids[:,0],centroids[:,1],marker="x",s=150,linewidths=5,zorder=10)
plt.show()