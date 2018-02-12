from nltk.corpus import twitter_samples

from nltk.tag import pos_tag_sents , pos_tag
from nltk.tokenize import sent_tokenize , word_tokenize

from nltk.corpus import stopwords

tweets = twitter_samples.strings('positive_tweets.json')
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

tweets_tagged = pos_tag_sents(tweets_tokens)





ajdectives_count = 0
nouns_count = 0


for tweet in tweets_tagged:
	for (word,id) in tweet:
		tag = id
		if tag == 'JJ':
			ajdectives_count += 1
			
		elif tag == 'NN':
			nouns_count += 1

			


print("Total no of adjectives found {}".format(ajdectives_count))
print("Total no of nouns found {}".format(nouns_count))
