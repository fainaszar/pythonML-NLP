import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

from matplotlib import style
from sklearn import preprocessing, cross_validation
from sklearn.cluster import KMeans

style.use('ggplot')



df = pd.read_excel('titanic.xls')
df.drop(['body','name'],1,inplace=True)
df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)



def handel_non_numerical_data(df):
	columns = df.columns.values

	for column in columns:
		text_digit_vals={}

		def convert_to_int(val):
			return text_digit_vals[val]


		if df[column].dtype != np.int64 and df[column].dtype != np.float64:
			column_contents = df[column].values.tolist()
			unique_elements = set(column_contents)
			x=0
			for unique in unique_elements:
				if unique not in text_digit_vals:
					text_digit_vals[unique]=x
					x+=1


			df[column] = list(map(convert_to_int,df[column]))

	return df


df = handel_non_numerical_data(df)

df.drop(['sex','boat'],1,inplace=True)




X = np.array(df.drop(['survived'],1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['survived'])

classifier = KMeans(n_clusters=2)
classifier.fit(X)

correct = 0 

for i in range(len(X)):
	to_be_predicted = np.array(X[i].astype(float))
	to_be_predicted = to_be_predicted.reshape(-1,len(to_be_predicted))
	prediction = classifier.predict(to_be_predicted)

	if prediction[0] == y[i]:
		correct += 1


print(correct/len(X)) 