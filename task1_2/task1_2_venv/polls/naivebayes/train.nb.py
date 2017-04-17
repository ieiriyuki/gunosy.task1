import sys
from sklearn.externals import joblib
# here import learning model naiveBayes
from .nbModel import naiveBayes

# start test here
args = sys.argv
if len(args) != 2:
    print("You need to specify training data")
    sys.exit()

training = args[1]
input = open(training,"r")
nb = naiveBayes()
for temp in input:
    data = temp.split(',')
    nb.train(data)
input.close()

print(nb)
joblib.dump(nb,'trained.nb.pkl')
