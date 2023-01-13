"""
print("hello world\
        hjkl\
        momom")
"""

for i in range (10, 0, -1):
    print (i,end=" ")

def fun1(pos, /, poskey, *, key):
    return pos + poskey + key


def concat(*argv, sep='/'):
    return sep.join(argv)

"""
4.7.4-4.7.5:unread
"""

def fun2(n):
    return lambda x : x + n

f = fun2(10)
ans1 = f(1)
ans2 = fun2(10)(2)