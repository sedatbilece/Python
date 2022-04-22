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

sum1 = 0
sum2 = 0
cnt=0
for x in range(0,30):
#Test verilerinin orani
    oran = 0.3

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
    
    
    Encoder = LabelEncoder()
    Train_Y = Encoder.fit_transform(egitiminif)
    Test_Y = Encoder.fit_transform(testSinif)  
    
    Tfidf_vect = TfidfVectorizer(max_features=5000)
    Tfidf_vect.fit(egitimCumle)
    Train_X_Tfidf = Tfidf_vect.transform(egitimCumle)
    Test_X_Tfidf = Tfidf_vect.transform(testCumle)
    
    #eğitim
    # Classifier - Algorithm - SVM
    # fit the training dataset on the classifier
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
    SVM.fit(Train_X_Tfidf,egitiminif)
    # predict the labels on validation dataset
    predictions_SVM = SVM.predict(Test_X_Tfidf)
    # Use accuracy_score function to get the accuracy
    snc1=accuracy_score(testSinif, predictions_SVM)
    snc2=f1_score(testSinif, predictions_SVM, average='weighted')
    sum1 +=snc1
    sum2 +=snc2
    print("SVM Accuracy Score -> ",snc1)
    print("SMV F1 SCORE       ->",snc2 )
    print("**********"+str(cnt))
    cnt+=1

    
print(sum1/30)
print(sum2/30)
print(metrics.classification_report(testSinif, predictions_SVM))

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

mat = confusion_matrix(testSinif, predictions_SVM)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
xticklabels=["1", "2", "3", "4", "5"], yticklabels=["1", "2", "3", "4", "5"])

plt.xlabel('Dogru Etiketler')
plt.ylabel('Tahmin Etiketleri')
plt.show()


