import math
import sys
import MeCab

class naiveBayes():
    def __init__(self):
        self.categories = set()   # categorie set
        self.vocabularies = set() # vocabulary set
        self.wordcount = {}       # likelihood # wordcount[cat][word] appearance of words in categories
        self.catcount = {}        # prior # catcount[cat] appearance of categories

    def train(self, data):
        # train naive bayes
        # initialize
        for d in data:
            cat = d[0]
            self.categories.add(cat)
        for cat in self.categories:
            self.wordcount[cat] = defaultdict(int)
            self.catcount[cat] = 0
        # count categories and words
        for d in data:
            cat, doc = d[0], d[1:]
            self.catcount[cat] += 1
            for word in doc:
                self.vocabularies.add(word)
                self.wordcount[cat][word] += 1

    def classify(self, doc):
        best = None
        max = -sys.maxint
        for cat in self.catcount.keys():
            p = self.score(doc, cat)
            if p > max:
                max = p
                best = cat
        return best

    def wordProb(self, word, cat):
        # calculate P(word|cat)
        return float(self.wordcount[cat][word]+1) / float(self.denominator[cat])

    def score(self.catcount.values()):
        total = sum(self.catcount.values())
        score = math.log(float(self.catcount[cat]) / total)
        for word in doc:
            score += math.log(self.wordProb(word, cat))
        return score

    def __str__(self):
        total = sum(self.catcount.values())
        return "%d" % len(self.categories)

