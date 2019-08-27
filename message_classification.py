# -*- coding: utf-8 -*-
#%%
#pandas用于读取数据
import pandas
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('SMSSpamCollection.txt',delimiter='\t',header=None)
y,X_train = df[0],df[1]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_train)

lr = linear_model.LogisticRegression()
lr.fit(X,y)
#把文本数据转换为二维数组
testX = vectorizer.transform(['URGENT! YOUR MOBILE NO. 1234 was awarded a prize',
                              'Hey money, whats up'])
predictions = lr.predict(testX)
print(predictions)