import os
import sys
import gc
import time

maze = []

func = [
    lambda x, y:(x, y-1),
    lambda x, y:(x, y+1),
    lambda x, y:(x-1, y),
    lambda x, y:(x+1, y),
]

def ids():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                sx, sy = i, j
            if maze[i][j] == 'E':
                ex, ey = i, j
    for i in range(len(maze)):
        maze[i] = list(maze[i])
    maze[sx][sy] = '0'
    maze[ex][ey] = '0'
    depth = 1  # 搜索限制深度
    while True:
        deep = 0  # 当前搜索深度
        stack = []
        stack.append((sx, sy))
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == '2':
                    maze[i][j] = '0'
        node = []
        while (len(stack)) > 0:
            curr = stack[-1]
            if curr[0] == ex and curr[1] == ey:
                print('沿途路径：')
                for output in stack:
                    print(output)
                return True
            if deep == depth:
                node.append((curr[0], curr[1]))
                stack.pop()
                deep -= 1
                curr = stack[-1]
            for dir in func:
                next = dir(curr[0], curr[1])
                if maze[next[0]][next[1]] == '0':
                    stack.append(next)
                    maze[next[0]][next[1]] = '2'
                    deep += 1
                    break
            else:
                maze[curr[0]][curr[1]] = '2'
                for i in range(len(node)):
                    de = node[i]
                    maze[de[0]][de[1]] = '0'
                node = []
                stack.pop()
                deep -= 1
        depth += 1


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    file = r'/MazeData.txt'
    with open(path+file) as file_object:
        for line in file_object:
            maze.append(line.strip())
    manhattan_astar_start_time = time.time()
    ids()
    manhattan_astar_time = time.time() - manhattan_astar_start_time
    gc.collect()
    print("IDDFS use", manhattan_astar_time, "to finish search")
    