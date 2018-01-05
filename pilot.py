from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

# Part-Of-Speech tagging
wiki.tags [('Python','NNP'),('is','VBZ'),('a','DT'),('high-level','JJ'),('general-purpose','JJ'),('programming','NN'),('language','NN')