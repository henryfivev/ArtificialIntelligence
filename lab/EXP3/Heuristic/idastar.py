target = {}
num = 1
for i in range(4):
    for j in range(4):
        target[num] = (i, j)
        num += 1

    target[0] = (3, 3)

"""
def h(node):
	cost = 0
	for i in range(4):
		for j in range(4):
			num = node[i][j]
			x, y = target[num]
			cost += abs(x-i) + abs(y-j)
	
	return cost

def h(node):
	cost = 0
	x = 1
	for i in range(4):
		for j in range(4):
			if i == 3 and j == 3:
				x = 0
			if node[i][j] != x:
				cost = cost + 1
			else:
				pass
			x = x + 1
	return cost
"""


def h(node):
	cost = 0
	x = 1
	for i in range(4):
		for j in range(4):
			if i == 3 and j == 3:
				x = 0
			if node[i][j] != x:
				cost = cost + 1
			else:
				pass
			x = x + 1
	return cost


def successors(node):
    x, y = 0, 0
    for i in range(4):
        for j in range(4):
            if(node[i][j] == 0):
                x, y = i, j
    success = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i, j in moves:
        a, b = x+i, y+j
        if(a < 4 and a > -1 and b < 4 and b > -1):
            temp = [[num for num in col] for col in node]
            temp[x][y] = temp[a][b]
            temp[a][b] = 0
            success.append(temp)

    return sorted(success, key=lambda x: h(x))


def is_goal(node):
    index = 1
    for row in node:
        for col in row:
            if(index != col):
                break
            index += 1
    return index == 16


def search(path, g, bound):
    node = path[-1]
    f = g + h(node)
    if(f > bound):
        return f
    if(is_goal(node)):
        return -1

    Min = 9999
    for succ in successors(node):
        if succ not in path:
            path.append(succ)
            t = search(path, g+1, bound)
            if(t == -1):
                return -1
            if(t < Min):
                Min = t
            path.pop()

    return Min


def ida_star(root):
    bound = h(root)
    path = [root]

    while(True):
        t = search(path, 0, bound)
        if(t == -1):
            return (path, bound)
        if(t > 70):
            return ([], bound)

        bound = t


def load():
    # root = [2,  7,  5,  3], [11, 10,  9, 14], [4,  0,  1,  6], [4,  0,  1,  6]
    # 6 root = [[0, 5, 15, 14], [7, 9, 6, 13], [1, 2, 12, 10], [8, 11, 4, 3]]
    # root = [[1, 2, 4, 8], [5, 7, 11, 10], [13, 15, 0, 3], [14, 6, 9, 12]]
	root = [[14, 10, 6, 0], [4, 9, 1, 8], [2, 3, 5, 11], [12, 13, 7, 15]]
	# 2 root = [[5, 1, 3, 4], [2, 7, 8, 12], [9, 6, 11, 15], [0, 13, 10, 14]]
    # root = [[6, 10, 3, 15], [14, 8, 7, 11], [5, 1, 0, 2], [13, 12, 9, 4]]
	return root


root = load()
(path, bound) = ida_star(root)
step = 0
for p in path:
    print('step', step)
    step += 1
    for row in p:
        print(row)

print('bound', bound)
