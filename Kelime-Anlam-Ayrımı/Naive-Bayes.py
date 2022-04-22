from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import seaborn as sns; sns.set()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.utils import shuffle
sum = 0
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

    model = make_pipeline(CountVectorizer(), MultinomialNB()) #model = GaussianNB()
    model.fit(egitimCumle, egitiminif)

    labels = model.predict(testCumle)

    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix
    mat = confusion_matrix(testSinif, labels)
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
                xticklabels=["1", "2", "3", "4", "5", "6", "7", "8"], yticklabels=["1", "2", "3", "4", "5", "6", "7", "8"])

    plt.xlabel('Dogru Etiketler')
    plt.ylabel('Tahmin Etiketleri')
    #plt.show()

    esitlikMiktar = 0
    for i in range(0, testVeriSayi):
        if(testSinif[i] == labels[i]):
            esitlikMiktar += 1
    print(metrics.classification_report(testSinif, labels))
    print(esitlikMiktar / testVeriSayi)
    sum += esitlikMiktar / testVeriSayi
print(sum/30)