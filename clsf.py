
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk

sentences = ([
		("Apple already plans to buy back 100 billion in shares, including 16 billion worth last quarter","computer-company"),
		("There are five species of aphids commonly found on apples: apple grain aphid, rosy apple aphid, apple aphid, spirea aphid and the woolly apple aphid. The aphid species can be identified by their colour, the time of year when they are present and by differences in the cornicles, which are small paired projections from the rear of aphids","fruit"),
		("The Apple I, Apple's first product, was sold as an assembled circuit board and lacked basic features such as a keyboard, monitor, and case. The owner of this unit added a keyboard and a wooden case.\
			Apple was established on April 1, 1976, by Steve Jobs, Steve Wozniak and Ronald Wayne[1] to sell the Apple I personal computer kit, a computer single handedly designed by Wozniak. The kits were hand-built by Wozniak[24][25] and first shown to the public at the Homebrew Computer Club.[26] The Apple I was sold as a motherboard (with CPU, RAM, and basic textual-video chips), which is less than what is today considered a complete personal computer.[27] The Apple I went on sale in July 1976 and was market-priced at $666.66 ($2,690 in 2013 dollars, adjusted for inflation)","computer-company"),
		("Commercially popular apple cultivars are soft but crisp. Other desired qualities in modern commercial apple breeding are a colourful skin, absence of russeting, ease of shipping, lengthy storage ability, high yields, disease resistance, common apple shape, and developed flavour.[36] Modern apples are generally sweeter than older cultivars, as popular tastes in apples have varied over time. Most North Americans and Europeans favour sweet, subacid apples, but tart apples have a strong minority following.[40] Extremely sweet apples with barely any acid flavour are popular in Asia[40] and especially India","fruit"),
		("After years of speculation and multiple rumored 'leaks', Apple announced a large screen, tablet-like media device known as the iPad on January 27, 2010. The iPad runs the same touch based operating system that the iPhone uses and many of the same iPhone apps are compatible with the iPad. This gave the iPad a large app catalog on launch even with very little development time before the release. Later that year on April 3, 2010, the iPad was launched in the US and sold more than 300,000 units on that day, reaching 500,000 by the end of the first week.[101] In May of the same year, Apple's market cap exceeded that of competitor Microsoft for the first time since 1989.","computer-company")
	])


#featuresets = [(get_features(n),g) for (n,g) in names]


sentences = list(sentences)
classifier = nltk.NaiveBayesClassifier.train(sentences)

print (classifier.classify(gender_features(raw_input("Enter a name: "))))