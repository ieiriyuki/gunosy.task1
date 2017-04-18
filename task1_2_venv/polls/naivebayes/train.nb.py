import sys
from sklearn.externals import joblib
# here import learning model naiveBayes
from nbModel import naiveBayes

# start test here
args = sys.argv
if len(args) != 3:
    print("You need to specify training data and a file to store it")
    sys.exit()

training = args[1]
input = open(training,"r")
nb = naiveBayes()
for temp in input:
    data = temp.split(',')
    nb.train(data)
input.close()

print(nb)
store = args[2]
joblib.dump(nb,store)
