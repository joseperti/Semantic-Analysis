# URL de guia: http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
#
#

import nltk

def divideTweetInWords(tweetIn):
    datos = [e.lower() for e in tweetIn.split() if len(e) >= 3]
    return datos

def divideTweetInWordsSent(tweetsIn):
    tweets = []
    for k in tweetsIn:
        datos = datos = [e.lower() for e in k[0].split() if len(e) >= 3]
        tweets.append([datos,k[1]])
    return tweets

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    print(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
	    document_words = set(document)
	    features = {}
	    for word in word_features:
	        features['contains(%s)' % word] = (word in document_words)
	    return features

tweetsIn = [["I love this car",'positive'],
    ["This view is amazing",'positive'],
    ["I feel great this morning",'positive'],
    ["I am so excited about the concert",'positive'],
    ["He is my best friend",'positive'],
    ["I do not like this car", "negative"],
    ["This view is horrible", "negative"],
    ["I feel tired this morning", "negative"],
    ["I am not looking forward to the concert", "negative"],
    ["He is my enemy", "negative"]
    ]

tweets = divideTweetInWordsSent(tweetsIn)
#print(tweets)
words_in_tweets = get_words_in_tweets(tweets)
print(words_in_tweets)
word_features = get_word_features(words_in_tweets)

#Vemos que palabras se encuentran en el documento
k = extract_features(divideTweetInWords("I love this car"))
print(k)

#Entrenamiento
training_set = nltk.classify.apply_features(extract_features, tweets)

#Entrenamos el clasificador
classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'Larry is my enemy'
print(classifier.classify(extract_features(tweet.split())))
