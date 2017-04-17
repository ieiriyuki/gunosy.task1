import math
import sys
import MeCab
from sklearn.externals import joblib

class naiveBayes():
    def __init__(self):
        self.catcount = {}
        self.wordcount = {}
        self.vocabularies = set()

    def to_words(self, sentence):
        mecab = MeCab.Tagger('mecabrc')
        words = [] # store words identified
        for info in mecab.parse(sentence).split('\n'):
            if info == 'EOS' or info == '': # exclude EOS and ''
                continue
            keyword = info.split(',')[0] # need only first one
            aword = keyword.split('\t') # separate word and class
            if aword[1] == '名詞': # if noun
                words.append(aword[0])
            elif aword[1] == '動詞': # if verb
                words.append(aword[0])
            elif aword[1] == '形容詞': # if adverb
                words.append(aword[0])
            elif aword[1] == '感動詞': # if ...
                words.append(aword[0])
        return words

    def count_word(self, category, words):
        for word in words:
            self.wordcount.setdefault(category,{})
            self.wordcount[category].setdefault(word,0)
            self.wordcount[category][word] += 1
            self.vocabularies.add(word)

    def count_category(self, category):
        self.catcount.setdefault(category,0)
        self.catcount[category] += 1

    def train(self, data):
        category = data[0]
        self.count_category(category)
        words = self.to_words(data[1])
        self.count_word(category, words)

    def prior_prob(self, category):
        num_of_category = sum(self.catcount.values())
        num_of_data_of_category = self.catcount[category]
        return num_of_data_of_category / num_of_category

    def is_word_in_category(self, category, word):
        if word in self.wordcount[category]:
            return self.wordcount[category][word]
        return 0

    def word_prob_given_category(self, category, word):
        numer = self.is_word_in_category(category, word) + 1
        denom = sum(self.wordcount[category].values()) + len(self.vocabularies)
        prob = numer / denom
        return prob

    def score(self, category, words):
        score = math.log(self.prior_prob(category))
        for word in words:
            score += math.log(self.word_prob_given_category(category, word))
        return score

    def classify(self, words):
        best = None
        max = -sys.maxsize
        for category in self.catcount.keys():
            prob = self.score(category, words)
            if prob > max:
                max = prob
                best = category
        return best

    def __str__(self):
        total = sum(self.catcount.values())
        categories = list(self.catcount.keys())
        strng = "documents %d, vocabularies %d, categories %d" % (total, len(self.vocabularies), len(categories))
        return strng

# start test here
args = sys.argv
if len(args) != 3:
    print("You need to specify training and test data")
    sys.exit()

training = args[1]
test = args[2]

if __name__ == "__main__":

    input = open(training,"r")
    nb = naiveBayes()
    for temp in input:
        data = temp.split(',')
        nb.train(data)
    input.close()

    print(nb)

    joblib.dump(nb, 'trained.nb.pkl')

    valid = open(test, "r")
    catcount = {}
    correct = {}
    for temp in valid:
        data = temp.split(',')
        true = data[0]
        # init
        correct.setdefault(true,0)
        catcount.setdefault(true, 0)
        catcount[true] += 1
        # inference
        call = nb.classify(nb.to_words(data[1]))
#        print(call + ' ' + temp)
        # is it correct ?
        if call == true:
            correct[true] += 1
    for i in catcount.keys():
        strng = "category %s, prior %d, correct %d" % (i, catcount[i], correct[i])
        print(strng)
    valid.close()
