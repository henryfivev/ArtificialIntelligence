#_*_coding:utf-8_*_
from time import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# 从sklearn.feature_extraction.text里导入文本特征向量化模板
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# 从sklearn.naive_bayes里导入朴素贝叶斯模型
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

"""
参考资料
https://blog.csdn.net/weixin_44016035/article/details/114953363
https://www.cnblogs.com/Yanjy-OnlyOne/p/11288098.html
"""

def readFile1():
    data_fit = open("train2.txt", mode='w', encoding='utf-8')
    for line in open("train.txt", encoding = 'utf-8'):
        data_fit.write(line.replace(" ", ",", 3))
    data_fit.close()

def readFile2():
    data_fit = open("test2.txt", mode='w', encoding='utf-8')
    for line in open("test.txt", encoding = 'utf-8'):
        data_fit.write(line.replace(" ", ",", 3))
    data_fit.close()

def main():
    readFile1()
    data = pd.read_csv("train2.txt", header=0, names=["line", "enum", "etype", "sentence"])
    enum = data["enum"].values
    stc = data["sentence"].values
    # 数据预处理：训练集和测试集分割，文本特征向量化
    # 随机采样84%的数据样本作为测试集
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(stc, enum, test_size=0.84, random_state=3)
    t1=Xtrain.tolist()
    t2=Ytrain.tolist()
    t11=Xtest.tolist()
    t22=Ytest.tolist()
    news_train = {"stc":t1, "enum": np.array(t2)}
    news_test = {'stc':t11, 'enum': np.array(t22)}
    # 文本特征向量化
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform((d for d in news_train["stc"]))
    y_train = news_train["enum"]
    X_test = vectorizer.transform((d for d in news_test["stc"]))
    y_test = news_test["enum"]
    # 初始化朴素贝叶斯
    # clf = MultinomialNB(alpha=0.99999)
    clf = KNeighborsClassifier(n_neighbors=15)
    # 利用训练数据对模型参数进行估计
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    print("train score: {0}".format(train_score))
    # 对参数进行预测
    pred = clf.predict(X_test)
    test_score = clf.score(X_test, y_test)
    print("predict: {0} is in category {1}".format(news_test["enum"][0], pred[0]))
    print("actually: {0} is in category {1}".format(news_test["enum"][0], [news_test["enum"][0]][0]))
    print("test score: {0}".format(test_score))
    print("----END----")


if __name__ == '__main__':
    main()