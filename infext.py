"""Python program on Information Extraction using NLP"""
import nltk,re,pprint

def ie_process(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]

	return sentences


sentence = ie_process("The two friends , faizan and uzair are CS students")
grammar = "NP:{<DT>?<JJ>*<NN>}"

#cp = nltk.RegexpParser(grammar)
#result = cp.parse(sentence[
print(nltk.ne_chunk(sentence[0]))
#result.draw()

