# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


def loadDataSet():

	#Function to load data from the text files and append them to the list

	train_data = list()
	train_labels = list()
		
	with open("apple-computers.txt","r") as File:
		reader = File.readlines()
		for line in reader:
			train_data.append(line)
			train_labels.append("computer-company")

	with open("apple-fruit.txt","r") as File:
		reader = File.readlines()
		for line in reader:
			train_data.append(line)
			train_labels.append("fruit")


	return train_data , train_labels


if __name__ == '__main__':
	
	train_data,train_labels = loadDataSet()

	#Vectorizing the training data
	vectorizer = TfidfVectorizer()
	vectorized_train_data= vectorizer.fit_transform(train_data)

	test_data=[]
	N = int(raw_input())
	if N <= 100:
	    for i in range(N):
	        line = raw_input()
	        test_data.append(line)
	        
	    #Vectorizing the test data 
	    vectorized_test_data = vectorizer.transform(test_data)


	    #Defining a Linear SVC Classifer using the sklearn module and trainig it to fit lables to the train_data
	    classifier = LinearSVC()
	    classifier.fit(vectorized_train_data,train_labels)


	    #Stroring the result for each input in the form of a list
	    results = classifier.predict(vectorized_test_data)

	    #Printing the resluts (Predicted Label)
	    for result in results:
	        print result
