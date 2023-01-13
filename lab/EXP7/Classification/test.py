import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing as pp
STOP_ITER = 0 #根据迭代次数
STOP_COST = 1 #根据代价函数的变化值
STOP_GRAD = 2 #根据梯度变化

#sigmoid函数
def sigmoid(z):
    return 1/(1+np.exp(-z))
#假设函数h(x)
def model(X,theta):
    return sigmoid(np.dot(X,theta.T))
#代价函数cost
def cost(X,y,theta):
    left=np.multiply(-y, np.log(model(X,theta)))
    right=np.multiply(1-y, np.log(1-model(X,theta)))
    return np.sum(left-right)/ (len(X))
#计算梯度方向
def gradient(X,y,theta):
    grad=np.zeros_like(theta)
    error=(model(X,theta)-y).ravel()
    for j in range(len(theta.ravel())):
        terms=(np.multiply(error,X[:,j]))
        grad[0,j]=np.sum(terms)/(len(X))
    return grad

def shuffleData(data):
    np.random.shuffle(data)     #洗牌
    cols=data.shape[1]          #提取data的列数
    X=data[:,:cols-1]           #提取特征矩阵X
    y=data[:,cols-1:cols]       #提取观测值y
    return X, y

def stopcriterion(type,value,threshold):
    if type==STOP_ITER:
        #当迭代次数大于阈值就停止
        return value > threshold   
    elif type==STOP_COST:
        #两次迭代之间的差值小于阈值即可停止
        return abs(value[-1]-value[-2]) < threshold  
    elif  type==STOP_GRAD:
        #梯度下降的方向小于阈值即可
        #np.linalg.norm求范数，默认情况下=各值的平方和开根号
        return np.linalg.norm(value) < threshold

n=100  #样本总数为100
cost1=[]
def descent(data,theta,batchsize,stoptype,thresh,alpha):
    i=0  #迭代次数
    k=0  #batch
    X,y=shuffleData(data)  #洗牌
    grad=np.zeros_like(theta)  #梯度方向
    costs=[cost(X,y,theta)]  #计算代价函数的损失值
    
    while True:
        #1.计算梯度方向grad，batchsize始值选择样本的数量
        grad=gradient(X[k:k+batchsize],y[k:k+batchsize],theta)  
        #设置循环，每次迭代都选择新的一组[k,k+batchsize]的样本进行迭代
        k=k + batchsize
        #如果循环过程中k超过了样本总量，则让它回归至0，重新洗牌，再次循环
        if k >= n:
            k=0
            X,y=shuffleData(data)
        #2.根据梯度下降公式求解theta值
        theta=theta - alpha*grad
        #同时将每次迭代中代价函数的损失值计算出来
        costs.append(cost(X,y,theta)) 
        cost1.append(cost(X,y,theta))
        #3.选择下降停止策略：
        #循环计算次数i
        i=i+1  
        #如果选择根据迭代次数停止，则value=迭代次数
        if stoptype==STOP_ITER:
           value=i
        #如果根据代价损失来停止，则value=代价函数
        elif stoptype==STOP_COST:
           value=costs
        #若根据梯度方向来停止，则value=梯度下降方向
        elif  stoptype==STOP_GRAD:
           value=grad
        #直到所选择的value都满足阈值thresh，则停止循环
        if stopcriterion(stoptype,value,thresh):
            break
        #4.返回最后更新的theta值，迭代次数，损失值和梯度方向
    return theta,i-1,grad
#定义预测函数，带入model计算后，如果概率大于0.5，则为正向类1，否则为负向类0
def predict(X_,theta_):
    return [1 if x>0.5 else 0 for x in model(X_,theta_)]


df=pd.read_csv('classification_data.txt',header=None,names=['Exam 1', 'Exam 2', 'Admitted'])
#设定标签 
positive=df[df['Admitted']==1]    #'Admitted'==1 为正向类
negative=df[df['Admitted']==0]    #'Admitted'==0 为负向类
print("-----df-------")
print(df)

#可视化数据预览
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)
plt.scatter(x=positive['Exam 1'],y= positive['Exam 2'],marker='x',s=50,label='positive')
plt.scatter(x=negative['Exam 1'],y= negative['Exam 2'],marker='o',s=50,label='negative')
plt.legend()
ax.set_xlabel('Exam 1')
ax.set_ylabel('Exam 2')
plt.show()

#添加x0的特征值为1
df.insert(0,'ones',1)
#转化为矩阵matrix
data=df.values
cols=data.shape[1]  #计算data的列数
X=data[:,:cols-1]
y=data[:,cols-1:cols]
#建立theta的矩阵
theta=np.zeros([1,3])

scaled_data=data.copy()
scaled_data[:,1:3]=pp.scale(data[:,1:3])  #对x0不进行缩放

#全批量，停止方式为当迭代次数为5000次是停止，学习率为0.0000001
theta2, i, g = descent(scaled_data,theta,100,STOP_ITER,5000,0.0000001)

fig1, ax = plt.subplots(figsize=(8,4))
ax.plot(np.arange(len(cost1)), cost1)
plt.show()

theta_new=np.array(theta2)
#选区标准化后的特征矩阵
X_new=scaled_data[:,:3]
data_new = pd.DataFrame(scaled_data,columns=['ones','Exam1','Exam2','Admitted'])
data_new['prediction']=predict(X_new,theta_new)
#判断预测值和观测值是否相等，相等返回True，不相等返回False
accuracy= (data_new['prediction']==data_new['Admitted'])
#查看True的个数
print(accuracy.value_counts())