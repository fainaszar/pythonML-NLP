
import nltk
def gender_features(word):
	return {'last_letter': word[-1].encode('utf-8')}

names = ([
		('Burhan','male') , ('Faizan','male') , ('Muneer','male') , ('Shahid','male') , ('Sahil','male') , ('Nadeem','male'),
		('Suhail','male') , ('Aalam','male') , ('Umer','male') , ('Adnan','male'),('Wahid','male'),('Aamir','male'),
		('Anaab','female'), ('Taiba','female'), ('Rutba','female') , ('Rifat','female') , ('Maheen','female') ,('Zakiya','female'),
		('Mehvish','female'), ('Enub','female') , ('Asra','female'),('Koshiya','female'),('Kaif','female'),('Mugais','femalw')
	])


featuresets = [(gender_features(n),g) for (n,g) in names]



classifier = nltk.NaiveBayesClassifier.train(featuresets)

print (classifier.classify(gender_features(raw_input("Enter a name: "))))