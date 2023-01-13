import copy
from email.policy import default
import gc
import os
import sys
from sklearn import tree
import time

from sympy import false, true

start = []
end = []
graph = []
rowlen = 0
collen = 0
state = []
ret = 0
que = []


def readFile(filePath):
    global collen, rowlen
    file = open(filePath, encoding='utf-8')
    for (number, line) in enumerate(file):
        line = line.replace("\n", "")
        print(line, number)
        graph.append(list(line))

        rowlen = len(line)
        if collen < number:
            collen = number

        if line.find("E") != -1:
            end.append(number)
            end.append(line.find("E"))
        if line.find("S") != -1:
            start.append(number)
            start.append(line.find("S"))


def DFS(point):  # point = [row, col]
    global state
    global ret
    state.append(point)
    row = point[0]
    col = point[1]
    fedirc = [1, 1, 1, 1]

    if row == end[0] and col == end[1]:
        print(point)
        ret = 1
    else:
        if (graph[row][col-1] != "1") and (not ([row, col-1] in state)):  # west
            fedirc[0] = [row, col-1]
        if (graph[row+1][col] != "1") and (not ([row+1, col] in state)):  # south
            fedirc[1] = [row+1, col]
        if (graph[row][col+1] != "1") and (not ([row, col+1] in state)):  # east
            fedirc[2] = [row, col+1]
        if (graph[row-1][col] != "1") and (not ([row-1, col] in state)):  # north
            fedirc[3] = [row-1, col]

        if fedirc.count(1) == 4:
            pass
        else:
            for x in range(4):
                if fedirc[x] != 1:
                    DFS(fedirc[x])
                    if ret:
                        print(point)
                        fedirc = [1, 1, 1, 1]

# we can use union find set 
# to print the path
# ufs = {hash(son) : father}
def BFS(startpoint):
    global que
    global ret
    global state
    que.append(startpoint)
    while not ret:  
        cpoint = que.pop(0)  # current point
        state.append(cpoint)
        row = cpoint[0]
        col = cpoint[1]
        if row == end[0] and col == end[1]:
            print(cpoint)
            ret = 1

        if (graph[row][col-1] != "1") and (not ([row, col-1] in state)):  # west
            que.append([row, col-1])
        if (graph[row+1][col] != "1") and (not ([row+1, col] in state)):  # south
            que.append([row+1, col])
        if (graph[row][col+1] != "1") and (not ([row, col+1] in state)):  # east
            que.append([row, col+1])
        if (graph[row-1][col] != "1") and (not ([row-1, col] in state)):  # north
            que.append([row-1, col])


def BBFS():
    h = {}
    reach = false
    que = [[], [], []]
    que[1].append(start)
    que[2].append(end)
    for d in range(rowlen*collen):
        dir = (d & 1) + 1
        sz = len(que[dir])
        for i in range(sz):
            x = que[dir].pop(0)
            row = x[0]
            col = x[1]
            state.append(x)
            if (graph[row][col-1] != "1") and (not ([row, col-1] in state)):  # west
                que[dir].append([row, col-1])
            if (graph[row+1][col] != "1") and (not ([row+1, col] in state)):  # south
                que[dir].append([row+1, col])
            if (graph[row][col+1] != "1") and (not ([row, col+1] in state)):  # east
                que[dir].append([row, col+1])
            if (graph[row-1][col] != "1") and (not ([row-1, col] in state)):  # north
                que[dir].append([row-1, col])
            hash = x[0]*1000 + x[1]
            if h.get(hash, 0)+dir == 3:
                reach = true
            h[hash] = dir
    if reach:
        print("found")
    else:
        print("haven't found")


path = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath = r'/input.txt'
readFile(path+filePath)
print("start =", start)
print("end   =", end)
print("----DFS start----")

manhattan_astar_start_time = time.time()
# DFS(start)
# BFS(start)
BBFS()
manhattan_astar_time = time.time() - manhattan_astar_start_time
gc.collect()
print("BFS use", manhattan_astar_time, "to finish search")
# print("----BFS start----")
# BFS(start)
# print("----BDS start----")
# BDS()
