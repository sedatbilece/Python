# -*- coding: utf-8 -*-
"""
Created on Mon May 23 01:03:29 2022

@author: bayram
"""

import pandas as pd
import numpy as np
import gensim
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,f1_score
from sklearn.ensemble import RandomForestClassifier

messages = pd.read_excel('Grup_6_Yas_Kelimesi_Etiketlemesi.xlsx')
messages.shape
messages = shuffle(messages)
messages.columns = ["text", "label"]
messages['text_clean'] = messages['text'].apply(lambda x: gensim.utils.simple_preprocess(x))
messages.head()
# Encoding the label column
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split (messages['text_clean'], messages['label'] , test_size=0.3)
# Train the word2vec model
w2v_model = gensim.models.Word2Vec(X_train,
                                   vector_size=100,
                                   window=5,
                                   min_count=2)
w2v_model.wv.index_to_key
words = set(w2v_model.wv.index_to_key )
X_train_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in words])
                         for ls in X_train])
X_test_vect = np.array([np.array([w2v_model.wv[i] for i in ls if i in words])
                         for ls in X_test])
# Why is the length of the sentence different than the length of the sentence vector?
for i, v in enumerate(X_train_vect):
    print(len(X_train.iloc[i]), len(v))
# Compute sentence vectors by averaging the word vectors for the words contained in the sentence
X_train_vect_avg = []
for v in X_train_vect:
    if v.size:
        X_train_vect_avg.append(v.mean(axis=0))
    else:
        X_train_vect_avg.append(np.zeros(100, dtype=float))
        
X_test_vect_avg = []
for v in X_test_vect:
    if v.size:
        X_test_vect_avg.append(v.mean(axis=0))
    else:
        X_test_vect_avg.append(np.zeros(100, dtype=float))
        # Are our sentence vector lengths consistent?
for i, v in enumerate(X_train_vect_avg):
    print(len(X_train.iloc[i]), len(v))
# Instantiate and fit a basic Random Forest model on top of the vectors
rf = RandomForestClassifier()
rf_model = rf.fit(X_train_vect_avg, y_train.values.ravel())
# Use the trained model to make predictions on the test data
y_pred = rf_model.predict(X_test_vect_avg)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print("accuracy score:",accuracy_score(y_test, y_pred))
print("f1_score:",f1_score(y_test, y_pred, average='weighted'))

