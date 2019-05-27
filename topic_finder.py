import nltk
from nltk.tokenize import RegexpTokenizer
import re
import gender_guesser.detector as gender

# To find x most frequent words that are not numbers, punctuation marks, or stop words
def findxMostFreqWord (text,x):
    no_nums= re.sub(r'\d+', '', text)
    tokenizer = RegexpTokenizer(r'\w+')
    allWords = tokenizer.tokenize(no_nums)
    stopwords = nltk.corpus.stopwords.words('english')
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)
    mostCommon= allWordExceptStopDist.most_common(x)
    results=[]
    for word, index in mostCommon:
        results.append(word)
    return (results)


def gender_finder (name):
    d = gender.Detector(case_sensitive=False)
    return d.get_gender(name)

# print (gender_finder(""))


