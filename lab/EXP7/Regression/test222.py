# -*- coding: utf-8 -*-
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

path = (Path(__file__).parent) / 'data/regress_data2.csv'
data = pd.read_csv(str(path), encoding="gbk")

#画原始数据图
mj = data['面积']
fj = data['房间数']
jg = data['价格']

#画原始数据曲线图
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(mj, fj, jg)
ax.set_title('3d Scatter plot')
plt.show()

cols = data.shape[1]
x = data.iloc[:,:-1] # 去掉y
y = data.iloc[:,-1] # 去掉x

#求代价函数###############################################
def computeCost(X,y,theta):
    temp = np.power((X*theta.T-y),2)
    return np.sum(temp)/(2*X.shape[0])

#梯度下降#################################################
def gradientDescent(X,y,theta,alpha,iters):
    #初始化临时矩阵temp
    temp = np.matrix(np.zeros(theta.shape))
    #初始化代价函数举证，维数为迭代次数
    cost = []
    m = X.shape[0]
    for i in range(iters):
        #根据theta个数循环跟新theta
        temp = theta - (alpha/m) * (X*theta.T-y).T * X
        #得到跟新后的theta
        theta = temp
        #计算代价
        #cost[i]=computeCost(X,y,theta)
        cost.append(computeCost(X, y, theta))
    return theta,cost

#标准化特征缩放###########################################
def preProcess(x,y):
    # x-=np.mean(X,axis=0)
    # x/=np.std(x,axis=0,dd0f=1)
    # 均值归一化
    x=(x-np.average(x))/(np.max(x)-np.min(x))
    x=np.c_[np.ones(len(x)),x]
    y=np.c_[y]
    return x,y

#学习率-迭代次数
alpha=0.000005
iters=1500
theta=np.matrix(np.array([0,0]))

#归一化
x2,y2=preProcess(x,y)
x2=np.matrix(x2)
y2=np.matrix(y2)
theta2 = np.matrix(np.array([0,0,0]))

#梯度下降法
g2,cost2 = gradientDescent(x2,y2,theta2,alpha,iters)

#预测图-面积和价格
x = np.linspace(data["面积"].min(), data["面积"].max(), 100)
f = x * g2[0, 1] + g2[0, 0]
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, f, 'r', label='预测值')
ax.scatter(data['面积'], data['价格'], label='训练数据')
ax.legend(loc=2)
ax.set_xlabel('面积', fontsize=18)
ax.set_ylabel('价格', rotation=0, fontsize=18)
ax.set_title('预测价格和面积规模', fontsize=18)
plt.show()

#预测图-房间数和价格
x = np.linspace(data["房间数"].min(), data["房间数"].max(), 100)
f = x * g2[0, 2] + g2[0, 0]
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, f, 'r', label='预测值')
ax.scatter(data['房间数'], data['价格'], label='训练数据')
ax.legend(loc=2)
ax.set_xlabel('房间数', fontsize=18)
ax.set_ylabel('价格', rotation=0, fontsize=18)
ax.set_title('预测价格和房间数规模', fontsize=18)
plt.show()

#绘出损失图像
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(np.arange(iters), cost2, 'r')
ax.set_xlabel('迭代次数', fontsize=18)
ax.set_ylabel('代价', rotation=0, fontsize=18)
ax.set_title('误差和训练Epoch数', fontsize=18)
plt.show()

print("---面积和价格函数的斜率---")
print(g2[0, 1])
print("--房间数和价格函数的斜率--")
print(g2[0, 2])
print("------lastest cost2-------")
print(cost2[-1])

print("---------finish-----------")