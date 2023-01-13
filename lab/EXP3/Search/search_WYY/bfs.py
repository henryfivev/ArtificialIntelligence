from collections import deque
import os
import sys

MAX = 100000  # 用于标识无已知路
n, m = 18, 36  # 长宽


class Point:  # 用来存点的类
    def __init__(self, x=0, y=0):  # 默认参数
        self.x = x
        self.y = y


def bfs(maze, begin, end):
    dist = [[MAX for col in range(m)]for row in range(n)]
    pre = [['' for col in range(m)]for row in range(n)]  # 存储沿途点的起点

    dirx = [0, 1, 0, -1]
    diry = [1, 0, -1, 0]  # 四个方向各一个单位

    dist[begin.x][begin.y] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        now = queue.popleft()
        flag = False
        for i in range(4):
            newx, newy = now.x+dirx[i], now.y+diry[i]
            if (n > newx >= 0) and (m > newy >= 0) and (maze[newx][newy]!='1') and (dist[newx][newy] == MAX):
                dist[newx][newy] = dist[now.x][now.y] + 1
                pre[newx][newy] = now
                queue.append(Point(newx,newy))
                if newx == end.x and newy == end.y:
                    flag = True
                    break
        if flag:
            break

    print("沿途路径：")
    way = []
    now = end
    while True:
        way.append(now)
        if now.x == begin.x and now.y == begin.y:
            break
        now = pre[now.x][now.y]
    while way:
        now = way.pop()
        print('(%d,%d)'%(now.x,now.y))


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    file = r'/MazeData.txt'

    maze = [['' for col in range(m)]for row in range(n)]  # 初始化列表
    begin, end = Point(), Point()
    with open(path+file) as file_object:
        i=0
        for line in file_object:
            maze[i] = line
            if 'S' in line:  # 如果在该行里发现起点就存好
                begin.x = i
                begin.y = line.index('S')
            if 'E' in line:
                end.x = i
                end.y = line.index('E')
            i += 1

    bfs(maze,begin,end)