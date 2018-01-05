from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

# Part-Of-Speech tagging
wiki.tags
#--	[('Python','NNP'),('is','VBZ'),('a','DT'),('high-level','JJ'),('general-purpose','JJ'),('programming','NN'),('language','NN')

wiki.noun_phrases

#**********************************************************************
#  Resource ←[93mbrown←[0m not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#  ←[31m>>> import nltk
#  >>> nltk.download('brown')
#  ←[0m
#  Searched in:
#    - 'C:\\Users\\abhishek.jee/nltk_data'
#    - 'C:\\nltk_data'
#    - 'D:\\nltk_data'
#    - 'E:\\nltk_data'
#    - 'C:\\Python34\\nltk_data'
#    - 'C:\\Python34\\lib\\nltk_data'
#    - 'C:\\Users\\abhishek.jee\\AppData\\Roaming\\nltk_data'
#**********************************************************************
#
#Traceback (most recent call last):
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 80, in __load
#    try: root = nltk.data.find('{}/{}'.format(self.subdir, zip_name))
#  File "C:\Python34\lib\site-packages\nltk\data.py", line 673, in find
#    raise LookupError(resource_not_found)
#LookupError:
#**********************************************************************
#  Resource ←[93mbrown←[0m not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#  ←[31m>>> import nltk
#  >>> nltk.download('brown')
#  ←[0m
#  Searched in:
#    - 'C:\\Users\\abhishek.jee/nltk_data'
#    - 'C:\\nltk_data'
#    - 'D:\\nltk_data'
#    - 'E:\\nltk_data'
#    - 'C:\\Python34\\nltk_data'
#    - 'C:\\Python34\\lib\\nltk_data'
#    - 'C:\\Users\\abhishek.jee\\AppData\\Roaming\\nltk_data'
#**********************************************************************
#
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "C:\Python34\lib\site-packages\textblob\decorators.py", line 35, in decorated
#    return func(*args, **kwargs)
#  File "C:\Python34\lib\site-packages\textblob\en\np_extractors.py", line 109, in train
#    train_data = nltk.corpus.brown.tagged_sents(categories='news')
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 116, in __getattr__
#    self.__load()
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 81, in __load
#    except LookupError: raise e
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 78, in __load
#    root = nltk.data.find('{}/{}'.format(self.subdir, self.__name))
#  File "C:\Python34\lib\site-packages\nltk\data.py", line 673, in find
#    raise LookupError(resource_not_found)
#LookupError:
#**********************************************************************
#  Resource ←[93mbrown←[0m not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#  ←[31m>>> import nltk
#  >>> nltk.download('brown')
#  ←[0m
#  Searched in:
#    - 'C:\\Users\\abhishek.jee/nltk_data'
#    - 'C:\\nltk_data'
#    - 'D:\\nltk_data'
#    - 'E:\\nltk_data'
#    - 'C:\\Python34\\nltk_data'
#    - 'C:\\Python34\\lib\\nltk_data'
#    - 'C:\\Users\\abhishek.jee\\AppData\\Roaming\\nltk_data'
#**********************************************************************
#
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Python34\lib\site-packages\textblob\decorators.py", line 24, in __get__
#    value = obj.__dict__[self.func.__name__] = self.func(obj)
#  File "C:\Python34\lib\site-packages\textblob\blob.py", line 459, in noun_phrases
#    for phrase in self.np_extractor.extract(self.raw)
#  File "C:\Python34\lib\site-packages\textblob\en\np_extractors.py", line 138, in extract
#    self.train()
#  File "C:\Python34\lib\site-packages\textblob\decorators.py", line 38, in decorated
#    raise MissingCorpusError()
#textblob.exceptions.MissingCorpusError:
#Looks like you are missing some required data for this feature.
#
#To download the necessary data, simply run
#
#    python -m textblob.download_corpora
#
#or use the NLTK downloader to download the missing data: http://nltk.org/data.html
#If this doesn't fix the problem, file an issue at https://github.com/sloria/TextBlob/issues.

import nltk
nltk.download('brown')

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial.sentiment
testimonial.sentiment.polarity

zen = TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex")
zen.words
zen.sentences

for sentence in zen.sentences:
	print (sentence.sentiment)
	
sentence = TextBlob('Use 4 spaces per indentation level.')
sentence.words
sentence.words[2].singularize()
sentence.words[-1].pluralize()

from textblob import Word
w = Word("octopi")
w.lemmatize()

#**********************************************************************
#  Resource ←[93mwordnet←[0m not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#  ←[31m>>> import nltk
#  >>> nltk.download('wordnet')
#  ←[0m
#  Searched in:
#    - 'C:\\Users\\abhishek.jee/nltk_data'
#    - 'C:\\nltk_data'
#    - 'D:\\nltk_data'
#    - 'E:\\nltk_data'
#    - 'C:\\Python34\\nltk_data'
#    - 'C:\\Python34\\lib\\nltk_data'
#    - 'C:\\Users\\abhishek.jee\\AppData\\Roaming\\nltk_data'
#**********************************************************************
#
#Traceback (most recent call last):
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 80, in __load
#    try: root = nltk.data.find('{}/{}'.format(self.subdir, zip_name))
#  File "C:\Python34\lib\site-packages\nltk\data.py", line 673, in find
#    raise LookupError(resource_not_found)
#LookupError:
#**********************************************************************
#  Resource ←[93mwordnet←[0m not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#  ←[31m>>> import nltk
#  >>> nltk.download('wordnet')
#  ←[0m
#  Searched in:
#    - 'C:\\Users\\abhishek.jee/nltk_data'
#    - 'C:\\nltk_data'
#    - 'D:\\nltk_data'
#    - 'E:\\nltk_data'
#    - 'C:\\Python34\\nltk_data'
#    - 'C:\\Python34\\lib\\nltk_data'
#    - 'C:\\Users\\abhishek.jee\\AppData\\Roaming\\nltk_data'
#**********************************************************************
#
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "C:\Python34\lib\site-packages\textblob\decorators.py", line 35, in decorated
#    return func(*args, **kwargs)
#  File "C:\Python34\lib\site-packages\textblob\blob.py", line 147, in lemmatize
#    pos = _wordnet.NOUN
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 116, in __getattr__
#    self.__load()
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 81, in __load
#    except LookupError: raise e
#  File "C:\Python34\lib\site-packages\nltk\corpus\util.py", line 78, in __load
#    root = nltk.data.find('{}/{}'.format(self.subdir, self.__name))
#  File "C:\Python34\lib\site-packages\nltk\data.py", line 673, in find
#    raise LookupError(resource_not_found)
#LookupError:
#**********************************************************************
#  Resource ←[93mwordnet←[0m not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#  ←[31m>>> import nltk
#  >>> nltk.download('wordnet')
#  ←[0m
#  Searched in:
#    - 'C:\\Users\\abhishek.jee/nltk_data'
#    - 'C:\\nltk_data'
#    - 'D:\\nltk_data'
#    - 'E:\\nltk_data'
#    - 'C:\\Python34\\nltk_data'
#    - 'C:\\Python34\\lib\\nltk_data'
#    - 'C:\\Users\\abhishek.jee\\AppData\\Roaming\\nltk_data'
#**********************************************************************
#
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Python34\lib\site-packages\textblob\decorators.py", line 38, in decorated
#    raise MissingCorpusError()
#textblob.exceptions.MissingCorpusError:
#Looks like you are missing some required data for this feature.
#
#To download the necessary data, simply run
#
#    python -m textblob.download_corpora
#
#or use the NLTK downloader to download the missing data: http://nltk.org/data.html
#If this doesn't fix the problem, file an issue at https://github.com/sloria/TextBlob/issues.

import nltk
nltk.download('wordnet')