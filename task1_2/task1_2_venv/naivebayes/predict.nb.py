import sys
from sklearn.externals import joblib

# 1 エンタメ
# 2 スポーツ
# 3 おもしろ
# 4 国内
# 5 海外
# 6 コラム
# 7 IT・科学
# 8 グルメ

nb = joblib.load('trained.nb.pkl')
args = sys.argv
if len(args) != 2:
    print("You need to specify test data")
    sys.exit()

test = args[1]
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
    # print(call + ' ' + temp)
    # is it correct ?
    if call == true:
        correct[true] += 1
for i in catcount.keys():
    strng = "category %s, prior %d, correct %d" % (i, catcount[i], correct[i])
    print(strng)
valid.close()
