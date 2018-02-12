# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from nltk.classify import NaiveBayesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB



train_data =["Apple already plans to buy back 100 billion in shares, including 16 billion worth last quarter",
			"Fortunately, there are low-chillapple varieties for temperate climates",
			"Apple's cash stash currently sits at a whopping 145 billion but only 43 billion is in the U.S.",
			"The apple is the pomaceous fruit of the apple tree, species Malus domestica in the rose family (Rosaceae)",
			"Apples are often eaten raw, but can also be found in many prepared foods (especially desserts) and drinks.",
			"The Apple I, Apple's first product, was sold as an assembled circuit board and lacked basic features such as a keyboard, monitor, and case.",
			"The Apple II was chosen to be the desktop platform for the first 'killer app' of the business world",
			"Mac OS X, based on NeXT's OPENSTEP and BSD Unix was released on March 24, 2001, after several years of development. Aimed at consumers and professionals alike, Mac OS X aimed to combine the stability, reliability and security of Unix with the ease of use afforded by an overhauled user interface. To aid users in migrating from Mac OS 9, the new operating system allowed the use of OS 9 applications through Mac OS X's Classic environment.[76] \
			On May 19, 2001, Apple opened the first official Apple Retail Stores in Virginia and California.[77] On July 9, they bought Spruce Technologies, a DVD authoring company. On October 23 of the same year, Apple announced the iPod portable digital audio player, and started selling it on November 10. The product was phenomenally successful  over 100 million units were sold within six years.[78][79] In 2003, Apple's iTunes Store was introduced, offering online music downloads for 0.99 a song and integration with the iPod",
			"At the Worldwide Developers Conference keynote address on June 6, 2005, Steve Jobs announced that Apple would begin producing Intel-based Mac computers in 2006.[83] On January 10, 2006, the new MacBook Pro and iMac became the first Apple computers to use Intel's Core Duo CPU. By August 7, 2006 Apple had transitioned the entire Mac product line to Intel chips, over one year sooner than announced.[83] The Power Mac, iBook, and PowerBook brands were retired during the transition; the Mac Pro, MacBook, and MacBook Pro became their respective successors.[84][85] On April 29, 2009, The Wall Street Journal reported that Apple was building its own team of engineers to design microchips",
			"After years of speculation and multiple rumored 'leaks', Apple announced a large screen, tablet-like media device known as the iPad on January 27, 2010. The iPad runs the same touch based operating system that the iPhone uses and many of the same iPhone apps are compatible with the iPad. This gave the iPad a large app catalog on launch even with very little development time before the release. Later that year on April 3, 2010, the iPad was launched in the US and sold more than 300,000 units on that day, reaching 500,000 by the end of the first week.[101] In May of the same year, Apple's market cap exceeded that of competitor Microsoft for the first time since 1989.",
			"Though the forbidden fruit of Eden in the Book of Genesis is not identified, popular Christian tradition has held that it was an apple that Eve coaxed Adam to share with her.The origin of the popular identification with a fruit unknown in the Middle East in biblical times is found in confusion between the Latin words mlum (an apple) and mƒlum (an evil), each of which is normally written malum.[33] The tree of the forbidden fruit is called 'the tree of the knowledge of good and evil' in Genesis 2:17, and the Latin for 'good and evil' is bonum et malum",
			"Commercially popular apple cultivars are soft but crisp. Other desired qualities in modern commercial apple breeding are a colourful skin, absence of russeting, ease of shipping, lengthy storage ability, high yields, disease resistance, common apple shape, and developed flavour.[36] Modern apples are generally sweeter than older cultivars, as popular tastes in apples have varied over time. Most North Americans and Europeans favour sweet, subacid apples, but tart apples have a strong minority following.[40] Extremely sweet apples with barely any acid flavour are popular in Asia[40] and especially India",
			"In the wild, apples grow readily from seeds. However, like most perennial fruits, apples are ordinarily propagated asexually by grafting. This is because seedling apples are an example of 'extreme heterozygotes', in that rather than inheriting DNA from their parents to create a new apple with those characteristics, they are instead significantly different from their parents",
			"The Apple I, Apple's first product, was sold as an assembled circuit board and lacked basic features such as a keyboard, monitor, and case. The owner of this unit added a keyboard and a wooden case.\
			Apple was established on April 1, 1976, by Steve Jobs, Steve Wozniak and Ronald Wayne[1] to sell the Apple I personal computer kit, a computer single handedly designed by Wozniak. The kits were hand-built by Wozniak[24][25] and first shown to the public at the Homebrew Computer Club.[26] The Apple I was sold as a motherboard (with CPU, RAM, and basic textual-video chips), which is less than what is today considered a complete personal computer.[27] The Apple I went on sale in July 1976 and was market-priced at $666.66 ($2,690 in 2013 dollars, adjusted for inflation)",
			"By the end of the 1970s, Apple had a staff of computer designers and a production line. The company introduced the Apple III in May 1980 in an attempt to compete with IBM and Microsoft in the business and corporate computing market.[40]\
Jobs and several Apple employees, including Jef Raskin, visited Xerox PARC in December 1979 to see the Xerox Alto. Xerox granted Apple engineers three days of access to the PARC facilities in return for the option to buy 100,000 shares (800,000 split-adjusted shares) of Apple at the pre-IPO price of $10 a share.[41] Jobs was immediately convinced that all future computers would use a graphical user interface (GUI), and development of a GUI began for the Apple Lisa.",
			"Since the 1930s, the Excelsior Experiment Station at the University of Minnesota has introduced a steady progression of important apples that are widely grown, both commercially and by local orchardists, throughout Minnesota and Wisconsin. Its most important contributions have included 'Haralson' (which is the most widely cultivated apple in Minnesota)",
			"Cultivars vary in their yield and the ultimate size of the tree, even when grown on the same rootstock. Some cultivars, if left unpruned, will grow very large, which allows them to bear much more fruit, but makes harvesting very difficult. Depending on the tree density (number of trees planted per unit surface area), mature trees typically bear 40â€“200 kilograms (88â€“440 lb) of apples each year, though productivity can be close to zero in poor years. Apples are harvested using three-point ladders that are designed to fit amongst the branches.",
			"There are five species of aphids commonly found on apples: apple grain aphid, rosy apple aphid, apple aphid, spirea aphid and the woolly apple aphid. The aphid species can be identified by their colour, the time of year when they are present and by differences in the cornicles, which are small paired projections from the rear of aphids"]


train_labels = ["computer-company","fruit","computer-company","fruit","fruit","computer-company","computer-company","computer-company","computer-company","computer-company","fruit","fruit","fruit","computer-company","computer-company","fruit","fruit","fruit"]

test_data=["Apple began working on the Apple Lisa in 1978","The Apple board of directors instructed Sculley to 'contain' Jobs and limit his ability to launch expensive forays into untested products.",
			"The apple forms a tree that is small and deciduous, generally standing 6 to 15 feet (1.8 to 4.6 m) tall in cultivation and up to 30 feet (9.1 m) in the wild.",
			"Apples were brought to North America by colonists in the 17th century",
			"The Newton was Apple's first foray into the PDA markets",
			"In 2002, Apple purchased Nothing Real for their advanced digital compositing application Shake,",
			"She points out that buckets of apples were found in the Oseberg ship burial site in Norway"]

vectorizer = TfidfVectorizer()
vectorized_train_data= vectorizer.fit_transform(train_data)
vectorized_test_data = vectorizer.transform(test_data)

# classifier = LinearSVC()
# classifier.fit(vectorized_train_data,train_labels)

# results = classifier.predict(vectorized_test_data)
# for result in results:
# 	print result


print "********************"
classifier2 =LinearSVC()
classifier2.fit(vectorized_train_data,train_labels) 
results = classifier2.predict(vectorized_test_data)
for result in results:
	print result

