# 中山大学计算机学院

# **人工智能本科生实验报告**

 

课程名称：Artificial Intelligence

| 教学班级 | 网安软工合班 | 专业（方向） | 网络空间安全 |
| -------- | ------------ | ------------ | ------------ |
| 学号     | 20337251     | 姓名         | 伍建霖       |

## 一、实验题目

### 盲目搜索和启发式搜索

## 二、实验内容

### 1.算法原理

#### BFS

1、创建一个空队列queue（用来存放节点）和一个空列表visit（用来存放已访问的节点）

2、依次将起始点及邻接点加入queue和visit中

3、poo出队列中最先进入的节点,从图中获取该节点的邻接点

4、如果邻接点不在visit中，则将该邻接点加入queue和visit中

5、输出pop出的节点

6、重复3、4、5，直至队列为空

#### DFS

1、创建一个空栈stack（用来存放节点）和一个空列表visit（用来存放已访问的节点）

2、依次将起始点及邻接点加入stack和visit中

3、poo出栈中最后进入的节点,从图中获取该节点的邻接点

4、如果邻接点不在visit中，则将该邻接点加入stack和visit中

5、输出pop出的节点

6、重复3、4、5，直至栈为空

(不过我没有用stack，而用了递归的操作，也类似于stack)

#### UCS

扩展路径消耗最小的节点N

(有点类似于djikstra算法)

(N点的路径消耗等于前一节点N-1的路径消耗加上N-1到N节点的路径消耗)

#### IDDFS

​	IDDFS是深度优先搜索的“升级版”：每次深搜都会有搜索的最大深度限制，如果没有找到解，那么就增大深度，再进行深搜，如此循环直到找到解为止，这样可以找到最浅层的解。

#### 双向搜索

双向搜索主要有两种：双向BFS和双向IDDFS

​	双向BFS类似于BFS，但它维护两个而不是一个队列，然后轮流拓展两个队列。同时用数组或哈希表记录当前的搜索情况，给从两个方向拓展的节点以不同的标记。当某点被两种标记同时标记时，搜索结束。双向IDDFS同理，从两个方向迭代加深深度搜索

#### IDA*

​	迭代加深搜索算法，在搜索过程中采用估值函数，以减少不必要的搜索。设置每次可达的最大深度depth，若没有到达目标状态则加深最大深度。采用估值函数，剪掉f(n)大于depth的路径。

#### A*

采用广度优先搜索策略，在搜索过程中使用启发函数

A*算法通过下面这个函数来计算每个节点的优先级。

![img](https://pic3.zhimg.com/80/v2-3c1f00587f5f8994946cf1d224419bba_720w.png)

其中：

- f(n)是节点n的综合优先级。当我们选择下一个要遍历的节点时，我们总会选取综合优先级最高（值最小）的节点。
- g(n) 是节点n距离起点的代价。
- h(n)是节点n距离终点的预计代价，这也就是A*算法的启发函数。关于启发函数我们在下面详细讲解。

A*算法在运算过程中，每次从优先队列中选取f(n)值最小（优先级最高）的节点作为下一个待遍历的节点。

其实A\*和 IDA\*就类似于BFS和DFS加上启发式函数，给他们指定一下方向

### 2. 伪代码

盲目搜索

```python
def BFS(start):
    将start加进队列中
    while (not ret):
        point = 队列第一个，pop
        将point标记为已访问
        row = point纵坐标
        col = point横坐标
    if point == end:
        ret = 1
    若point四周的点可行 and 未访问:
        将对应点加进队列
        
def DFS(point):
    将point标记为已访问
    row = point纵坐标
    col = point横坐标
    可行方向fd = [1, 1, 1, 1]

    if point == end:
        ret = 1
    else:
        若point四周的点可行 and 未访问过:
            fd对应位置改为对应点的坐标

        若fd没变:
            返回上一级DFS
        否则:
            遍历fd中可行的点:
                DFS(对应点)
                若ret为1:
                    可在这里输出路径
                    fd = [1, 1, 1, 1]

def BBFS():
    h = {}
    reach = false
    que = [[], [], []]
    que[1],que[2]分别加进start和end

    for d in range(rowlen*collen):
        dir为1时正向，2时反向
        遍历que[dir]:
            point = 队列第一个，pop
            将point标记为已访问
            row = point纵坐标
            col = point横坐标

            若point四周的点可行 and 未访问:
                将对应点加进队列

            若h中对应位置的值加dir == 3:
                表示存在节点被两边都搜过了
            h[对应位置] = dir
            
def uniformCostSearch(problem):
    # 初始化相关参数
    result = []
    explored = set()
    frontier = util.PriorityQueue()
    # 定义起始状态，其中包括开始的位置，对应的行动方案和行动代价
    start = (problem.getStartState(), [], 0)
    # 把起始状态放进frontier队列中，update方法会自动对其中的状态按照其行动代价进行排序
    frontier.update(start,0)
    # 构造循环，循环读取frontier中的状态，进行判定
    while not frontier.isEmpty():
        # 获取当前节点的各项信息
        (node, path, cost) = frontier.pop()
        # 如果弹出的节点状态满足目标要求，停止循环
        if problem.isGoalState(node):
            result = path
            break
        # 如果该节点该节点不满足目标要求，判定其是否访问过
        if node not in explored:
            explored.add(node)
            # 遍历这个节点的子节点，更新frontier队列
            for child,direction,step in problem.getSuccessors(node):
                newPath = path + [direction]
                newCost = cost + step
                newNode = (child, newPath, newCost)
                frontier.update(newNode, newCost)
    # 返回计算结果，即一个行动方案
    return result

def IDDFS(u, d):
    # 类似于DFS
    if d > limit:
        return
    else:
        for each edge (u, v):
            IDDFS(v, d + 1)
  	return
```

启发式搜索

```python
def astar(原图):
    用c表示当前g值
    将原图加进open中
    while 1:
        graph1 = 优先级最高的，从open中pop # f = g + h
        将graph1加入close
        遍历graph可能变成的情况: # 用g表示
            如果它在close中:
                pass
            否则:
                如果它不在open中:
                    将g加入open
                    把当前方格设置为它的父亲
                    记录该方格的f,g,h值
                否则：
                    当前c小于其g值:
                        把它的父亲设置为当前方格
                        重新计算它的g, f
    若目标graph已在open中:
        break
    否则:
        若open为空:
            print("----fail----")
            return
ptpath()

def dfs(当前图，深度，h):
    若深度+h大于最大深度:
        return false
    若当前图 == 目标图:
        return true
    下一图
    遍历下一图的可能性:
        重新计算h值
        记录路径
        若dfs(下一图，深度+1，新h值)
            return true
    return false
    

def idastar():
    计算h值
    最大深度 = h
    while(not dfs(argv...))
        最大深度 = 最大深度 + 1
    return 最大深度
```

### 3.关键代码展示（带注释）

#### BFS

![image-20220401224412598](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224412598.png)

#### DFS

![image-20220401224346476](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224346476.png)

#### BBFS

![image-20220401224501791](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224501791.png)

#### UCS

![image-20220401224546465](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224546465.png)

#### IDDFS

<img src="C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224623505.png" alt="image-20220401224623505" style="zoom: 150%;" />

#### A*

![image-20220401224843214](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224843214.png)

![image-20220401224856040](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401224856040.png)

#### IDA*

<img src="C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401225025731.png" alt="image-20220401225025731" style="zoom: 200%;" />

<img src="C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220401225041679.png" alt="image-20220401225041679" style="zoom:200%;" />

### 4.创新点&优化（如果有）

 尝试了多种评估函数

h1():当前图和目标图的不同之处的个数

h2():当前图任意节点到正确位置的步数

## 三、实验结果及分析

### 1. 实验结果展示示例（可图可表可文字，尽量可视化）

#### 盲目搜索

<img src="C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220402132740952.png" alt="image-20220402132740952" style="zoom:50%;" />

| BFS     | DFS     | BBFS    | UCS      | IDDFS    |
| ------- | ------- | ------- | -------- | -------- |
| 3.998ms | 35.98ms | 3.990ms | 500.09ms | 135.99ms |

#### 启发式搜索

M表示曼哈顿函数，D表示评估位置不正确的启发式函数，单位：ms

| 算法 | 样例一          | 样例三          | 样例六          | 样例五            |
| ---- | --------------- | --------------- | --------------- | ----------------- |
| A*   | M:287.9, D:2792 | M:19143, D:2749 | M:18381, D:6023 | M:5.87s, D:4.998s |
| IDA* | 0.008s          | 71.4s           | 大于20min       | 452.6s            |

### 2.评测指标展示及分析（其它可分析运行时间等）

#### 盲目搜索

从实验结果来看，BFS = BBFS > DFS > IDDFS >UCS，但由于样例太少，不具有一般性

UCS

![img](https://img-blog.csdnimg.cn/20190923110743984.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1N1eWViaXViaXU=,size_16,color_FFFFFF,t_70)

 IDDFS

![image-20220402142923705](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220402142923705.png)

#### 启发式搜索

​	在使用下面两个算法解决15puzzle问题之前，我尝试使用BFS和IDDFS来解决，但无一例外都耗时过长，无法跑出结果

A*

​	根据代码跑出来的结果来看，曼哈顿函数访问的节点少于misplaced的，即使用了更少的内存，而misplaced则花费了更少的时间。但从网上找的资料来看，曼哈顿函数应该是使用内存少同时花费更少的时间，与结果不符

IDA*

​	在我的认识中，IDA\*是要优于A\*的，但由于评估函数对两个算法的影响过大，导致IDA\*测出来的时间多于A\*

![image-20220402143119981](C:\Users\77354\AppData\Roaming\Typora\typora-user-images\image-20220402143119981.png)

## 四、参考资料

 **A\*算法视频讲解：**
[http://www.bilibili.com/video/av7830414/](https://link.zhihu.com/?target=http%3A//www.bilibili.com/video/av7830414/%3Fshare_source%3Dcopy_link%26ts%3D1543803890%26share_medium%3Dipad%26bbid%3Dfc1a404fefcd83a4bea5dc5062fb61c8)

**A\*算法可视化：**
[PathFinding.js](https://link.zhihu.com/?target=http%3A//qiao.github.io/PathFinding.js/visual/)

**参考链接：**
[堪称最好的A*算法 - 我的程序世界 - CSDN博客](https://link.zhihu.com/?target=https%3A//blog.csdn.net/b2b160/article/details/4057781)
[搜索--最佳优先搜索 - 沉淀，累积 - CSDN博客](https://link.zhihu.com/?target=https%3A//blog.csdn.net/highkit/article/details/7326167)
[八数码 poj1077 Eight（A*、IDA*)](https://link.zhihu.com/?target=https%3A//blog.csdn.net/guognib/article/details/21177719)
[八数码的八境界 - liugoodness - 博客园](https://link.zhihu.com/?target=http%3A//www.cnblogs.com/goodness/archive/2010/05/04/1727141.html)
[菜鸟系列--八数码八境界 - MyWorld - CSDN博客](https://link.zhihu.com/?target=https%3A//blog.csdn.net/kopyh/article/details/48442415)
[最短路径 A*算法 应用堆优化 - user-agent:this - CSDN博客](https://link.zhihu.com/?target=https%3A//blog.csdn.net/hello42/article/details/8914320)
[A*寻路极限优化 - Zzz的专栏 - CSDN博客](https://link.zhihu.com/?target=https%3A//blog.csdn.net/u013052238/article/details/78126019)