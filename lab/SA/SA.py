"""48 [1, 4, 0, 3, 2]"""
import random
import numpy as np
from math import e
from math import exp

city = [[-1, 9, -1, 4, 14],
        [9, -1, 12, 8, 5],
        [-1, 12, -1, 13, 27],
        [4, 6, 13, -1, 6],
        [14, 5, 27, 6, -1]]

T0 = 50000
T_end = 15
q = 0.98
L = 100

# 两个城市的距离


def dist(a, b):
    if city[a][b] == -1:
        distance = 1000
    else:
        distance = city[a][b]
    return distance

# 路程总长


def totaldistance(a):
    value = 0
    for j in range(4):
        value += dist(a[j], a[j + 1])
    value += dist(a[4], a[0])
    return value

# 初始化一个解 


def init_ans():
    ans = []
    for i in range(5):
        ans.append(i)
    return ans

# 产生新解


def creat_new(ans_before):
    ans_after = []
    for i in range(len(ans_before)):
        ans_after.append(ans_before[i])
    cuta = random.randint(0, 4)
    cutb = random.randint(0, 4)
    ans_after[cuta], ans_after[cutb] = ans_after[cutb], ans_after[cuta]
    return ans_after


if __name__ == '__main__':
    ans0 = init_ans()
    T = T0
    cnt = 0
    trend = []
    while T > T_end:
        for i in range(L):
            newans = creat_new(ans0)
            old_dist = totaldistance(ans0)
            new_dist = totaldistance(newans)
            df = new_dist - old_dist
            if df >= 0:
                rand = random.uniform(0, 1)
                if rand < 1/(exp(df / T)):
                    ans0 = newans
            else:
                ans0 = newans
        T = T * q
        cnt += 1
        now_dist = totaldistance(ans0)
        trend.append(now_dist)
        print(cnt, "次降温，温度为：", T, " 路程长度为：", now_dist)
    distance = totaldistance(ans0)
    print(distance, ans0)
