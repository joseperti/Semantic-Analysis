# URL de guia: http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
#
#

import nltk

def divideTweetInWords(tweetIn):


def divideTweetInWordsSent(tweetsIn):
    tweets = []
    for k in tweetsIn:
        datos = k[0].split(" ")
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
    ["He is my best friend",'positive']]

tweets = divideTweetInWords(tweetsIn)
#print(tweets)
words_in_tweets = get_words_in_tweets(tweets)
print(words_in_tweets)
word_features = get_word_features(words_in_tweets)
extract_features()

print(word_features)