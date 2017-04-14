import sys
from sklearn.externals import joblib

categoryes = {'1':'エンタメ',
              '2': 'スポーツ',
              '3':'おもしろ',
              '4','国内',
              '5','海外',
              '6','コラム',
              '7','IT・科学',
              '8':'グルメ',
              }
nb = joblib.load('trained.nb.pkl')
data = temp.split(',')
call = nb.classify(nb.to_words(data[1]))

return categories[call]
