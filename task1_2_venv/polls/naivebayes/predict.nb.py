import sys
from sklearn.externals import joblib

args = sys.argv
if len(args) != 3:
    print("You need to specify trained model and test data")
    sys.exit()

categories = {'1':'エンタメ','2': 'スポーツ','3':'おもしろ','4':'国内',
              '5':'海外','6':'コラム','7':'IT・科学','8':'グルメ', }

class prediction():
    def __init__(self):
        self.correct = {}

    def count(self,true,call):
        self.correct.setdefault(true,{})
        self.correct[true].setdefault(call,0)
        self.correct[true][call] += 1

pred = prediction()
for i in categories:
    for j in categories:
        pred.count(categories[i],categories[j])

nb = joblib.load(args[1])
test = args[2]
valid = open(test, "r")
for temp in valid:
    data = temp.split(',')
    true = categories[data[0]]
    call = nb.classify(nb.to_words(data[1]))
    pred.count(true,call)

valid.close()

print(end='\t')
for i in categories:
    print(categories[i], end='\t')
print()
for i in categories:
    print(categories[i], end='\t')
    for j in categories:
        print(pred.correct[categories[i]][categories[j]], end='\t')
    print()
