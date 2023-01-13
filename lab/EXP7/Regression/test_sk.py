# -*- coding: utf-8 -*-
# coding: utf-8
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import log_loss
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

'''
获得数据
'''
path = (Path(__file__).parent) / 'data/regress_data2.csv'
data = pd.read_csv(str(path), encoding="gbk")
cols = data.shape[1]
X = data.iloc[:,:cols-1] # 去掉y
y = data.iloc[:,cols-1:] # 去掉x

mj = data['面积']
fj = data['房间数']
jg = data['价格']

#画原始数据曲线图
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(mj, fj, jg)
ax.set_title('3d Scatter plot')
plt.show()

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=1)
reg = LinearRegression()
model = reg.fit(X_train, y_train)
#epochs = model.history['loss']
#loss = log_loss(X_train, y_train) #gives the loss for these values
y_pred = reg.predict(X_test)
#print("loss:", loss)
print('MSE:', mean_squared_error(y_test, y_pred))
print(y_pred)