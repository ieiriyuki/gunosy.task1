
import MeCab
m = MeCab.Tagger('mecabrc')

def to_words(self, sentence):
    mecab_result = m.parse(sentence)
    infor_of_words = mecab_result.split('\n')
    words = []
    for info in infor_of_words:
        if info == 'EOS' || info == '':
            break
        info_elems = info.split(',')
        if info_elems[6] == '*':
            words.append(info_elems[0][:-3])
            continue
        words.append(info_elems[6])
    return tuple(words)

data = open("tdata.csv", "r")

for line in data:
    mots = []
    temp = line[:-1].split(',')

    to_words
        print(elems)
#    print(line)

data.close()
