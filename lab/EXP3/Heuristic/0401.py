import os
import sys

start = []
end = []
graph = []
rowlen = 0
collen = 0
state = []
ret = 0
que = []


def readFile(filePath):
    file = open(filePath, encoding='utf-8')
    for (number, line) in enumerate(file):
        line = line.replace("\n", "")
        line = line.split(" ")
        print(line, number)
        graph.append(list(line))


def hashh(a):
    return a[0]*100 + a[1]


def ptpath(): # print the path
    # up to the data structure
    pass


def h1(): 
    # if the number are at correct position
    pass



ans = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
openl = []
closel = []
ufs = {} # union find set
f = {}
g = {}
h = {}
def astar(start):
    c = 0 # count, current g
    openl.append(start)
    while 1:
        openl.sort() # f
        cpoint = openl.pop(0) # current point
        row = cpoint[1][0]
        col = cpoint[1][1]
        closel.append(cpoint)
        east = [row, col+1]
        south = [row+1, col]
        west = [row, col-1]
        north = [row-1, col]
        if east in closel:
            pass
        else:
            if east in openl:
                if g[hashh(east)] > c:
                    ufs[hashh(east)] = cpoint
                    # count f, g, h
                    # need i compute the pos nearby?
            else:
                openl.append(east)
                ha = hashh(east)
                ufs[ha] = cpoint
                # count f, g, h
        if graph == ans:
            break
        else:
            if openl.empty():
                print("----fail----")
                return
    ptpath()


path = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath = r'/input4.txt'
readFile(path+filePath)
print(graph)
# astar()
print("----end----")