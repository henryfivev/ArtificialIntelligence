from collections import deque
import gc
import os
import sys
import time

MAX = 100000  # 用于标识无已知路
n, m = 18, 36  # 长宽
frontier = []


class Point:  # 用来存点的类
    def __init__(self, x=0, y=0, cost=0):  # 默认参数
        self.x = x
        self.y = y
        self.cost = cost


class Po:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def ucs(maze, begin, end):
    dist = [[MAX for col in range(m)]for row in range(n)]
    prev = [[MAX for col in range(m)]for row in range(n)]
    dirx = [0, 1, 0, -1]
    diry = [1, 0, -1, 0]  # 四个方向各一个单位
    explore = []
    dist[begin.x][begin.y] = 0
    inqueue(begin)
    while True:
        if len(frontier) == 0:
            return
        now = frontier.pop(0)
        if now.x == end.x and now.y == end.y:
            output = now
            s = []
            s.append(now)
            print('沿途路径：')
            while True:
                pre = prev[output.x][output.y]
                s.append(pre)
                if pre.x == begin.x and pre.y == begin.y:
                    s = s[::-1]
                    for data in s:
                        print('(%d,%d)' % (data.x, data.y))
                    break
                output = pre
            return
        explore.append(Po(now.x, now.y))
        for i in range(4):
            newx, newy = now.x+dirx[i], now.y+diry[i]
            if (n > newx >= 0) and (m > newy >= 0) and (maze[newx][newy] != '1'):
                point = Po(newx, newy)
                if point not in explore and not in_frontier(point):
                    dist[newx][newy] = dist[now.x][now.y] + 1
                    prev[newx][newy] = Po(now.x, now.y)
                    inqueue(Point(newx, newy, dist[newx][newy]))


def inqueue(point):
    size = len(frontier)
    for i in range(size):
        if point.cost < frontier[i].cost:
            frontier.insert(i, point)
            return
    frontier.append(point)


def in_frontier(point):
    for data in frontier:
        if data.x == point.x and data.y == point.y:
            return True
    return False


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    file = r'/MazeData.txt'

    maze = [['' for col in range(m)]for row in range(n)]  # 初始化列表
    begin, end = Point(), Point()
    with open(path+file) as file_object:
        i = 0
        for line in file_object:
            maze[i] = line
            if 'S' in line:  # 如果在该行里发现起点就存好
                begin.x = i
                begin.y = line.index('S')
                begin.cost = 0
            if 'E' in line:
                end.x = i
                end.y = line.index('E')
                end.cost = MAX
            i += 1
    manhattan_astar_start_time = time.time()
    ucs(maze, begin, end)
    manhattan_astar_time = time.time() - manhattan_astar_start_time
    gc.collect()
    print("UCS use", manhattan_astar_time, "to finish search")
    
