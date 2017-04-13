import sys
from sklearn.externals import joblib
# here import learning model naiveBayes
import naiveBayes

# 1 エンタメ
# 2 スポーツ
# 3 おもしろ
# 4 国内
# 5 海外
# 6 コラム
# 7 IT・科学
# 8 グルメ

# start test here
args = sys.argv
if len(args) != 2:
    print("You need to specify training data")
    sys.exit()

training = args[1]

input = open(training,"r")
nb = naiveBayes.Model()
for temp in input:
    data = temp.split(',')
    nb.train(data)
input.close()

print(nb)
joblib.dump(nb,'trained.nb.pkl')
