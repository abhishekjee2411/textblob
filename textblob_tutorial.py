#TEXTBLOB

# http://textblob.readthedocs.io/en/dev/quickstart.html

from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
wiki.tags
#	[('Python', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('high-level', 'JJ'), ('general-purpose', 'JJ'), ('programming', 'NN'), ('language', 'NN')]


#-##########################
#-	NOUN-PHRASE EXTRACTION
#-##########################

>>> wiki.noun_phrases
#	WordList(['python'])


#-######################
#-	SENTIMENT ANALYSIS
#-######################

>>> testimonial = TextBlob("TextBlob is amazingly simple to use. What great fun!")
>>> testimonial.sentiment
#	Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
>>> testimonial.sentiment.polarity
#	0.39166666666666666
>>> testimonial.sentiment.subjectivity
#	0.4357142857142857


#-#################
#	TOKENIZATION
#-#################

>>> zen = TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
>>> zen.words
#	WordList(['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit', 'Simple', 'is', 'better', 'than', 'complex'])
>>> zen.sentences
#	[Sentence("Beautiful is better than ugly."), Sentence("Explicit is better than implicit."), Sentence("Simple is better than complex.")]

>>> zen.noun_phrases
#	WordList(['beautiful', 'explicit', 'simple'])

for sentence in zen.sentences:
    print (sentence,"\n",sentence.sentiment,"\n",sentence.subjectivity)
	
#	Beautiful is better than ugly.
#	 Sentiment(polarity=0.2166666666666667, subjectivity=0.8333333333333334)
#	 0.8333333333333334
#	Explicit is better than implicit.
#	 Sentiment(polarity=0.5, subjectivity=0.5)
#	 0.5
#	Simple is better than complex.
#	 Sentiment(polarity=0.06666666666666667, subjectivity=0.41904761904761906)
#	 0.41904761904761906


#-######################################
#-	WORDS INFLECTION AND LEMMATIZATION
#-######################################

>>> sentence = TextBlob('Use 4 spaces  per indentation level.')
>>> sentence.words
#	WordList(['Use', '4', 'spaces', 'per', 'indentation', 'level'])
>>> sentence.words[2].singularize()
#	'space'
>>> sentence.words[-1].pluralize()
#	'levels'


>>> from textblob import Word
>>> w = Word("octopi")
>>> w.lemmatize()
#	'octopus'
>>> w.lemmatize('octopus')
#	'octopus'


#-##########################
#-	WordNet INTEGRATION
#-##########################

>>> from textblob import Word
>>> from textblob.wordnet import VERB
>>> word = Word("octopus")
>>> print(word)
#	octopus
>>> word.synsets
#	[Synset('octopus.n.01'), Synset('octopus.n.02')]
>>> Word("hack").get_synsets(pos=VERB)
#	[Synset('chop.v.05'), Synset('hack.v.02'), Synset('hack.v.03'), Synset('hack.v.04'), Synset('hack.v.05'), Synset('hack.v.06'), Synset('hack.v.07'), Synset('hack.v.08')]
>>> Word("octopus").definitions
#	['tentacles of octopus prepared as food', 'bottom-living cephalopod having a soft oval body with eight long tentacles']

>>> from textblob.wordnet import Synset
>>> octopus = synset('octopus.n.02')
>>> octopus = Synset('octopus.n.02')
>>> shrimp = Synset('shrimp.n.03')
>>> octopus.path_similarity(shrimp)
#	0.1111111111111111


#-##########################
#-	WordLists
#-##########################

>>> animals = TextBlob("cat dog octopus")
>>> animals.words
#	WordList(['cat', 'dog', 'octopus'])
>>> animals.words.pluralize()
#	WordList(['cats', 'dogs', 'octopodes'])


#-##########################
#-	SPELLING CORRECTION
#-##########################

>>> b = TextBlob("I havv good spelling!")
>>> print (b.correct())
#	I have good spelling!

>>> from textblob import Word
>>> w = Word('falibility')
>>> w.spellcheck()
#	[('fallibility', 1.0)]


#-########################################
#-	GET WORD AND NOUN PHRASE FREQUENCIES
#-########################################

monty = TextBlob("We are no longer the Knights who say Ni. "
"We are now the Knights who say Ekki ekki ekki PTANG.")

monty.word_counts['ekki']
#	3

>>> monty.words.count('ekki')
#	3

>>> monty.words.count('ekki',case_sensitive=True)
#	2

>>> wiki.noun_phrases.count('python')
#	1


#-########################################
#-	TRANSLATION AND LANGUAGE DETECTION
#-########################################

en_blob