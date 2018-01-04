# nlp.py

#Import data and tagger
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents

#Load the strings from a particular json file into a list named "tweets"
tweets = twitter_samples.strings('positive_tweets.json')

#Load tokenized tweets
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

#Tag tagged tweets
tweets_tagged = pos_tag_sents(tweets_tokens)

#Set accumulators
JJ_count = 0
NN_count = 0

#Loop through the list of tweets
for tweet in tweets_tagged:
	for pair in tweet:
		tag = pair[1]
		if tag == 'JJ':
			JJ_count += 1
		if tag == 'NN':
			NN_count += 1
			
#Print the total numbers for the adjectives and nouns
print ("Total number of adjectives :",JJ_count)
print ("Total number of nouns :",NN_count)

