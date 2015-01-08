import nltk
import os
from nltk.collocations import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')


for filename in os.listdir("./raw"):
    if filename[-3:] == "txt":
        print("Text file found -- processing")
        fh = open("raw/" + filename)
        raw = unicode(fh.read(),'utf8')
        tokens = tokenizer.tokenize(raw)
        tokens = [w for w in tokens if not w in stop]

        ng = nltk.ngrams(tokens,1)
        distributions = nltk.FreqDist(ng)
        export = distributions.most_common(500)
        print(export)
        exportFile = open("export" + filename[:-3] + "csv", "w+")
        exportFile.write("word,count\n")
        for k,v in export:
            exportFile.write(k[0] + "," + str(v) + "\n")
        
