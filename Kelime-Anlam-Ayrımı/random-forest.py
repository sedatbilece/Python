from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import seaborn as sns; sns.set()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.utils import shuffle

from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
    
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier 


oran = 0.7

#Exceldeki verileri listelere alÄ±yoruz
data = pd.read_excel('ac-kelimesi.xlsx')
data = shuffle(data)

data.columns = ["text", "label"]
cumleler = data['text'].tolist()
siniflar = data['label'].tolist()
toplamVeriSayi = len(cumleler)
testVeriSayi = int(toplamVeriSayi * oran)

egitimCumle  = cumleler[testVeriSayi : toplamVeriSayi]
egitiminif  = siniflar[testVeriSayi : toplamVeriSayi]
testCumle   = cumleler[0 : testVeriSayi]
testSinif   = siniflar[0 : testVeriSayi]

vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(egitimCumle).toarray()

Y = egitiminif

clf = RandomForestClassifier()
clf.fit(X, Y)

snc= clf.predict(vectorizer.transform(testCumle).toarray())

print("Accuracy: ", accuracy_score(testSinif, snc))


snc2=f1_score(testSinif, snc, average='weighted')
print("F1-SCORE : ",snc2)




# tek bir cümlenin tahmini
cumle=['bugün açlıktan öleceğim']
snctek= clf.predict(vectorizer.transform(cumle).toarray())
print(cumle," : ",snctek)

