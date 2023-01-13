import os
import sys
from sympy import false, true
import copy

S = []
S = []
number = 0


def readFile(filePath):
    global S
    global number
    for line in open(filePath, encoding='utf-8'):  # line
        line = line.replace(' ', '').strip()
        if line[0] == '(':
            line = list(line)
            line[0] = ''
            line[len(line)-1] = ''
            line = ''.join(line)
        for i in range(len(line)-2):
            if line[i+1] == ',' and line[i] == ')':
                line = list(line)
                line[i+1] = ';'
                line = ''.join(line)
        line = line.split(';')
        for i in range(len(line)):
            newele = {}  # newle
            str1 = line[i]  # str1
            for j in range(len(str1)-1):
                str2 = str1  # str2
                if str1[j] == '(':
                    elename = str2[0:j]  # elename
                    elemem = str2[j+1:len(str1)-1]
                    elemem = elemem.split(',')
                    if elename in newele.keys():
                        str3 = elename+'2'  # str3
                        newele[str3] = elemem
                    else:
                        newele[elename] = elemem
                    line[i] = newele
                    break
        # line.append(number)
        number += 1
        S.append(line)


def printlast():
    if S[-1] == []:
        print("[]", end="")
    for x in S[-1]:
        k = list(x.keys())
        v = list(x.values())
        if len(v[0]) > 1:
            print(k[0], "(", end="", sep="")
            for y in range(len(v[0])):
                print(v[0][y], end="", sep="")
                if y != len(v[0])-1:
                    print(',', end="")
            pass
            print(") ", end="", sep="")
        else:
            for y in range(len(v[0])):
                print(k[0], "(", v[0][y], ") ", end="", sep="")
    print("")


def judge(instead, havenewclause):
    if havenewclause:
        if instead == true:
            print(" = ", end='')
            printlast()
        else:
            ikey = list(instead.keys())
            ivalue = list(instead.values())
            print("(", end="")
            for x in range(len(ikey)):
                print(ikey[x], "=", ivalue[x], end="", sep="")
                if x != len(ikey)-1:
                    print(",", end="")
            print(") = ", end="")
            printlast()
            pass
    else:
        pass


def fanyi(str1):
    if '!' in str1:
        return str1.replace('!', '').split()
    else:
        ret = '!' + str1
        ret1 = ret.split()  # use for debug
        return ret1


def MGU(a: 'dict', b: 'dict') -> "bool or dict":

    valueset = {}
    ainfunc = copy.deepcopy(a)
    binfunc = copy.deepcopy(b)
    alist = [x for x in ainfunc.values()]
    blist = [x for x in binfunc.values()]
    if alist == blist:  # ab same
        return true
    else:
        for x in range(len(alist[0])):
            if (alist[0][x] in blist[0][x]) and (alist[0][x] != blist[0][x]):
                break
            else:
                if alist[0][x] == blist[0][x]:
                    pass
                elif (len(alist[0][x]) > 1 and len(blist[0][x]) > 1) or\
                        (len(alist[0][x]) == 1 and len(blist[0][x]) == 1):
                    # if no var inside
                    # haven't solve f(g(y)) - f(u)
                    return false
                elif len(alist[0][x]) > len(blist[0][x]):
                    valueset[blist[0][x]] = alist[0][x]
                    blist[0][x] = alist[0][x]
                else:
                    valueset[alist[0][x]] = blist[0][x]
                    alist[0][x] = blist[0][x]
    if alist != blist:  # MGU Error
        return false
    return valueset


def norepeat():
    global S
    sset = copy.deepcopy(S)
    """
    for a in sset:
        for b in sset:
            if sset.index(a) != sset.index(b):
                for c in range(len(a)):
                    for d in range(len(b)):
                        if type(a[c]) == dict:
                            a[c] = list(a[c].items())
                        if type(b[d]) == dict: 
                            b[d] = list(b[d].items())
                        if 
                        if a == b:
                            del S[sset.index(b)]
    """


def resolution():
    global S
    S.sort(key=lambda i: len(i))
    print("---------------------")
    for x in S:
        print(x, S.index(x)+1)
    print("-------开始归结-------")
    for ccc in range(10):
        S.sort(key=lambda i: len(i))
        print("-------sorted--------")
        longest = len(S[-1])-1
        length = len(S)
        havenewclause = 0
        for first in S:
            if S.index(first) > length*2:
                break
            for second in S:
                if [] in S:
                    return
                if (len(first) == 1 and len(second) == 1):  # set - set
                    skey = list(second[0].keys())
                    if (fanyi(skey[0]) == list(first[0].keys())):
                        newclause = MGU(first[0], second[0])
                        if newclause == true:
                            havenewclause = 1
                            S.append([])
                            print('R[', S.index(first)+1, ',',
                                  S.index(second)+1, ']',
                                  end='', sep='')
                            judge(newclause, havenewclause)
                            havenewclause = 0
                            pass
                        elif newclause == false:
                            pass
                        else:
                            havenewclause = 1
                            S.append([])
                            print('R[', S.index(first)+1, ',',
                                  S.index(second)+1, ']',
                                  end='', sep='')
                            judge(newclause, havenewclause)
                            pass
                    pass
                elif (len(first) == 1 and len(second) > 1):  # sample - set
                    for x in range(len(second)):
                        skey = list(second[x].keys())
                        if (fanyi(skey[0]) == list(first[0].keys())):
                            newclause = MGU(first[0], second[x])
                            if newclause == true:
                                havenewclause = 1
                                temp = copy.deepcopy(second)
                                del temp[x]
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                            elif newclause == false:
                                pass
                            else:
                                havenewclause = 1
                                temp = copy.deepcopy(second)
                                del temp[x]
                                for y in range(len(temp)):
                                    for z in temp[y].values():
                                        for w in newclause.keys():
                                            if w in z:
                                                l = list(temp[y].values())
                                                for v in range(len(l[0])):
                                                    if w == z[v]:
                                                        t = list(
                                                            temp[y].keys())
                                                        temp[y][t[0]
                                                                ][v] = newclause[w]
                                            else:
                                                pass
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, chr(97+x), ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                        else:
                            pass
                    pass
                elif (len(first) > 1 and len(second) == 1):  # set - sample
                    # this situation will be reached in elif2
                    firstcopy = copy.deepcopy(first)
                    secondcopy = copy.deepcopy(second)
                    for x in range(len(secondcopy)):
                        skey = list(secondcopy[x].keys())
                        if (fanyi(skey[0]) == list(firstcopy[0].keys())):
                            newclause = MGU(firstcopy[0], secondcopy[x])
                            if newclause == true:
                                havenewclause = 1
                                temp = copy.deepcopy(firstcopy)
                                del temp[x]
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                            elif newclause == false:
                                pass
                            else:
                                havenewclause = 1
                                temp = copy.deepcopy(firstcopy)
                                del temp[x]
                                for y in range(len(temp)):
                                    for z in temp[y].values():
                                        for w in newclause.keys():
                                            if w in z:
                                                l = list(temp[y].values())
                                                for v in range(len(l[0])):
                                                    if w == z[v]:
                                                        t = list(
                                                            temp[y].keys())
                                                        temp[y][t[0]
                                                                ][v] = newclause[w]
                                            else:
                                                pass
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, chr(97+x), ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                        else:
                            pass
                    pass
                else:  # set - set
                    for x in range(len(first)):
                        for y in range(len(second)):
                            fkey = list(first[x].keys())
                            if (fanyi(fkey[0]) == list(second[y].keys())):
                                newclause = MGU(first[x], second[y])
                                if newclause == false:
                                    pass
                                elif newclause == true:
                                    firstcopy = copy.deepcopy(first)
                                    secondcopy = copy.deepcopy(second)
                                    del firstcopy[x]
                                    del secondcopy[y]
                                    temp = firstcopy + secondcopy
                                    if temp in S:
                                        pass
                                    elif len(temp) > longest:
                                        pass
                                    else:
                                        havenewclause = 1
                                        S.append(temp)
                                        print('R[', S.index(first)+1, chr(97+x), ',',
                                              S.index(second) +
                                              1, chr(97+y), ']',
                                              end='', sep='')
                                        judge(newclause, havenewclause)
                                    havenewclause = 0
                                    pass
                                else:
                                    firstcopy = copy.deepcopy(first)
                                    secondcopy = copy.deepcopy(second)
                                    del firstcopy[x]
                                    del secondcopy[y]
                                    temp = firstcopy + secondcopy
                                    for xx in range(len(temp)):
                                        for z in temp[xx].values():
                                            for w in newclause.keys():
                                                if w in z:
                                                    l = list(temp[xx].values())
                                                    for v in range(len(l[0])):
                                                        if w == z[v]:
                                                            t = list(
                                                                temp[xx].keys())
                                                            temp[xx][t[0]
                                                                     ][v] = newclause[w]
                                                else:
                                                    pass
                                    if temp in S:
                                        pass
                                    elif len(temp) > longest:
                                        pass
                                    else:
                                        havenewclause = 1
                                        S.append(temp)
                                        print('R[', S.index(first)+1, chr(97+x), ',',
                                              S.index(second) +
                                              1, chr(97+y), ']',
                                              end='', sep='')
                                        judge(newclause, havenewclause)
                                    havenewclause = 0
                    pass
    print("--------fail---------")
    print("---this is the end---")


path = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath = r'/input2.txt'
# 更换样例测试文件时将input1改为input2或input3即可。
readFile(path + filePath)
# norepeat()
resolution()


"""
现将S[0]设为目标公式的否定
先遍历S[0]对S
再遍历SS对S

明天try
SSS
sort list----优先尝试子句归结
"""
""""
pseudocode
读入数据,存在S中
开始归结：
    将S以len为key进行升序排序
    输出现有S
    循环10次:
        将S以len为key进行升序排序
        for first in S:
            若first的下标大于两倍的len(S):
                break # sort一下再进行归并
            for second in S:
                若S中存在空列表:
                    归结成功
                若first和second都是原子公式:
                    若互为否定:
                        若需要合一:
                            若不能合一:
                                pass
                            若能合一:
                                S中添加一个空列表 # 此时已归结成功
                        否则:
                            S中添加一个空列表 # 此时已归结成功
                    否则pass
                若first和second中一个是原子公式一个是子句:
                    遍历子句中的原子公式
                        若和原子公式互为否定:
                            若需要合一:
                                若不能合一:
                                    pass
                                若能合一:
                                    将(变量替换且删除原子公式的否定)的子句加入S
                            否则:
                                将删除原子公式的否定后的子句加入S
                        否则pass
                若first和second都是子句:
                    遍历两个子句:
                        若存在一对互为否定的原子公式:
                            若需要合一:
                                若不能合一:
                                    pass
                                若能合一:
                                    将(变量替换且删除原子公式的否定
                                        且合并了的)的子句加入S
                            否则:
                                将删除原子公式的否定且合并后的子句加入S
                        否则pass
    输出fail,归结失败



def MGU(a: 'dict', b: 'dict') -> "bool or dict":
    valueset = {}
    ainfunc = copy.deepcopy(a)
    binfunc = copy.deepcopy(b)
    alist = [x for x in ainfunc.values()] # [['x','y']]
    blist = [x for x in binfunc.values()] # [['tony','mike']]
    if alist == blist:  
        # ab same
        # 即不需要合一
        return true
    else:
        for x in range(len(alist[0])):
            if (alist[0][x] in blist[0][x]) and\
                (alist[0][x] != blist[0][x]):
                # 若其中一项被包含在另一项中,则无法合一
                break
            else:
                if alist[0][x] == blist[0][x]:
                    # 该项不需要替换
                    pass
                elif (len(alist[0][x]) > 1 and len(blist[0][x]) > 1) or\
                     (len(alist[0][x]) == 1 and len(blist[0][x]) == 1):
                    # haven't solve f(g(y)) - f(u)
                    # 两项都不是变量or两项都是变量
                    return false
                elif len(alist[0][x]) > len(blist[0][x]):
                    # 用不是变量的项替换是变量的项
                    valueset[blist[0][x]] = alist[0][x]
                    blist[0][x] = alist[0][x]
                else:
                    # 用不是变量的项替换是变量的项
                    valueset[alist[0][x]] = blist[0][x]
                    alist[0][x] = blist[0][x]
    if alist != blist:  # MGU Error
        return false
    return valueset


def resolution():
    global S
    S.sort(key=lambda i: len(i))
    print("---------------------")
    for x in S:
        print(x, S.index(x)+1)
    print("-------开始归结-------")
    for ccc in range(10):
        S.sort(key=lambda i: len(i))
        print("-------sorted--------")
        longest = len(S[-1])-1
        length = len(S)
        havenewclause = 0
        for first in S:
            if S.index(first) > length*2:
                break
            for second in S:
                if [] in S:
                    return
                if (len(first) == 1 and len(second) == 1):  # set - set
                    skey = list(second[0].keys())
                    if (fanyi(skey[0]) == list(first[0].keys())):
                        newclause = MGU(first[0], second[0])
                        if newclause == true:
                            havenewclause = 1
                            S.append([])
                            # 输出新生成的子句
                            print('R[', S.index(first)+1, ',',
                                  S.index(second)+1, ']',
                                  end='', sep='')
                            judge(newclause, havenewclause)
                            # 输出完毕
                            havenewclause = 0
                            pass
                        elif newclause == false:
                            pass
                        else:
                            havenewclause = 1
                            S.append([])
                            # 输出新生成的子句
                            print('R[', S.index(first)+1, ',',
                                  S.index(second)+1, ']',
                                  end='', sep='')
                            judge(newclause, havenewclause)
                            # 输出完毕
                            pass
                    pass
                elif (len(first) == 1 and len(second) > 1):  # sample - set
                    for x in range(len(second)):
                        skey = list(second[x].keys())
                        if (fanyi(skey[0]) == list(first[0].keys())):
                            newclause = MGU(first[0], second[x])
                            if newclause == true:
                                havenewclause = 1
                                temp = copy.deepcopy(second)
                                del temp[x]
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    # 输出新生成的子句
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                    # 输出完毕
                                havenewclause = 0
                            elif newclause == false:
                                pass
                            else:
                                havenewclause = 1
                                temp = copy.deepcopy(second)
                                del temp[x]
                                # 替换变量
                                for y in range(len(temp)):
                                    for z in temp[y].values():
                                        for w in newclause.keys():
                                            if w in z:
                                                l = list(temp[y].values())
                                                for v in range(len(l[0])):
                                                    if w == z[v]:
                                                        t = list(
                                                            temp[y].keys())
                                                        temp[y][t[0]
                                                                ][v] = newclause[w]
                                            else:
                                                pass
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    # 输出新生成的子句
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, chr(97+x), ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                    # 输出完毕
                                havenewclause = 0
                        else:
                            pass
                    pass
                elif (len(first) > 1 and len(second) == 1):  # set - sample
                    # this situation will be reached in elif2
                    firstcopy = copy.deepcopy(first)
                    secondcopy = copy.deepcopy(second)
                    for x in range(len(secondcopy)):
                        skey = list(secondcopy[x].keys())
                        if (fanyi(skey[0]) == list(firstcopy[0].keys())):
                            newclause = MGU(firstcopy[0], secondcopy[x])
                            if newclause == true:
                                havenewclause = 1
                                temp = copy.deepcopy(firstcopy)
                                del temp[x]
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    # 输出新生成的子句
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                    # 输出完毕
                                havenewclause = 0
                            elif newclause == false:
                                pass
                            else:
                                havenewclause = 1
                                temp = copy.deepcopy(firstcopy)
                                del temp[x]
                                # 替换变量
                                for y in range(len(temp)):
                                    for z in temp[y].values():
                                        for w in newclause.keys():
                                            if w in z:
                                                l = list(temp[y].values())
                                                for v in range(len(l[0])):
                                                    if w == z[v]:
                                                        t = list(
                                                            temp[y].keys())
                                                        temp[y][t[0]
                                                                ][v] = newclause[w]
                                            else:
                                                pass
                                if temp in S:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    S.append(temp)
                                    # 输出新生成的子句
                                    print('R[', S.index(first)+1, ',',
                                          S.index(second)+1, chr(97+x), ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                    # 输出完毕
                                havenewclause = 0
                        else:
                            pass
                    pass
                else:  # set - set
                    for x in range(len(first)):
                        for y in range(len(second)):
                            fkey = list(first[x].keys())
                            if (fanyi(fkey[0]) == list(second[y].keys())):
                                newclause = MGU(first[x], second[y])
                                if newclause == false:
                                    pass
                                elif newclause == true:
                                    # 合并并删除对应原子
                                    firstcopy = copy.deepcopy(first)
                                    secondcopy = copy.deepcopy(second)
                                    del firstcopy[x]
                                    del secondcopy[y]
                                    temp = firstcopy + secondcopy
                                    if temp in S:
                                        pass
                                    elif len(temp) > longest:
                                        pass
                                    else:
                                        havenewclause = 1
                                        S.append(temp)
                                        # 输出新生成的子句
                                        print('R[', S.index(first)+1, chr(97+x), ',',
                                              S.index(second) +
                                              1, chr(97+y), ']',
                                              end='', sep='')
                                        judge(newclause, havenewclause)
                                        # 输出完毕
                                    havenewclause = 0
                                    pass
                                else:
                                    # 合并并删除对应原子
                                    firstcopy = copy.deepcopy(first)
                                    secondcopy = copy.deepcopy(second)
                                    del firstcopy[x]
                                    del secondcopy[y]
                                    temp = firstcopy + secondcopy
                                    # 替换变量
                                    for xx in range(len(temp)):
                                        for z in temp[xx].values():
                                            for w in newclause.keys():
                                                if w in z:
                                                    l = list(temp[xx].values())
                                                    for v in range(len(l[0])):
                                                        if w == z[v]:
                                                            t = list(
                                                                temp[xx].keys())
                                                            temp[xx][t[0]
                                                                     ][v] = newclause[w]
                                                else:
                                                    pass
                                    if temp in S:
                                        pass
                                    elif len(temp) > longest:
                                        pass
                                    else:
                                        havenewclause = 1
                                        S.append(temp)
                                        # 输出新生成的子句
                                        print('R[', S.index(first)+1, chr(97+x), ',',
                                              S.index(second) +
                                              1, chr(97+y), ']',
                                              end='', sep='')
                                        judge(newclause, havenewclause)
                                        # 输出完毕
                                    havenewclause = 0
                    pass
    print("--------fail---------")
    print("---this is the end---")
"""