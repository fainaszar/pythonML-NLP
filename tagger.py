#-*- coding: utf-8 -*-
import nltk
import os
from nltk import pos_tag
from nltk.chunk import conlltags2tree
from nltk.tree import Tree
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


# st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
# 						'/usr/share/stanford-ner/stanford-ner.jar',
# 						encoding = 'utf-8')


sentences = """
	If Hyeon Chung still thinks he can take a wander down Seoul's busy Myeongdong Street unrecognised, he'll do well to reassess that after becoming the first Korean to reach a Grand Slam semifinal on Wednesday. MORE: All the latest scores and results
	]To broaden its audience, British left-leaning news site The Canary has been converting all its text articles to audio since last September. In time, it plans to make its audio articles available on voice assistant devices like Google Home and Amazon Echo, where publishers are increasingly
"""
# tokenized_text = word_tokenize(text)
# tagged_text = nltk.pos_tag(tokenized_text)

# pridicted_text = nltk.ne_chunk(tagged_text)


# multiline_string = nltk.chunk.tree2conllstr(pridicted_text)
# listed_pos_and_ne = rmultiline_string.split()

# del listed_pos_and_ne[1::3]
# listed_ne = listed_pos_and_ne


# for n,i in enumerate(listed_ne):

# 	if i == "B-PERSON":
# 		listed_ne[n] = "PERSON"

# 	if i == "I-PERSON":
# 		listed_ne[n] = "PERSON"

# 	if i == "B-ORGANIZATION":
# 		listed_ne[n] = "ORGANIZATION"
# 	if i == "I-ORGANIZATION":
# 		listed_ne[n] = "ORGANIZATION"
# 	if i == "B-LOCATION":
# 		listed_ne[n] = "LOCATION"
# 	if i == "I-LOCATION":
# 		listed_ne[n] = "LOCATION"
# 	if i == "B-GPE":
# 		listed_ne[n] = "LOCATION"
# 	if i == "I-GPE":
# 		listed_ne[n] = "LOCATION"

# print listed_ne


def process_text(sentences):
	

	token_text = word_tokenize(sentences)

	return token_text


def nltk_tagger(token_text):
	tagged_words = nltk.pos_tag(token_text)
	ne_tagged = nltk.ne_chunk(tagged_words)
	return (ne_tagged)


def bio_tagger(ne_tagged):
	bio_tagged=[]
	prev_tag = "O"
	for token, tag in ne_tagged:
		if tag == "O": #O
			bio_tagged.append((token, tag))
			prev_tag = tag
			continue
		if tag != "O" and prev_tag == "O": # Begin NE
			bio_tagged.append((token, "B-"+tag))
			prev_tag = tag
		elif prev_tag != "O" and prev_tag == tag: # Inside NE
			bio_tagged.append((token, "I-"+tag))
			prev_tag = tag
		elif prev_tag != "O" and prev_tag != tag: # Adjacent NE
			bio_tagged.append((token, "B-"+tag))
			prev_tag = tag
		

	return bio_tagged



def stanford_tree(bio_tagged):
	tokens,ne_tags = zip(*bio_tagged)
	pos_tags = [pos for token,pos in pos_tag(tokens)]

	conlltags = [(token,pos,ne) for token,pos,ne in zip(tokens,pos_tags,ne_tags)]
	ne_tree = conlltags2tree(conlltags)


def structure_ne(ne_tree):
	ne= []

	for subtree in ne_tree:
		if type(subtree) == Tree:
			ne_label = subtree.label()
			ne_string = " ".join([token for token,pos in subtree.leaves()])
			ne.append((ne_string,ne_label))


	return ne



def nltk_main():
	print(structure_ne(nltk_tagger(process_text(sentences))))


if __name__ == '__main__':
	nltk_main()