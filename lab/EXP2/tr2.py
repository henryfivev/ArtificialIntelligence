import os
import sys
from sympy import false, true
import copy
S = []
number = 1


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


def judge(havenewclause):
    if havenewclause:
        print(S[-1])


def fanyi(str1):
    if '!' in str1:
        return list(str1.replace('!', ''))
    else:
        ret = '!' + str1
        ret1 = ret.split()  # use for debug
        return ret1


def MGU(a, b):
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
                elif (len(alist[0][x]) > 1 and len(blist[0][x]) > 1):  # if no var inside
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


def resolution():
    global S
    havenewclause = 0
    # 回去把S改了，clauseset
    # number -> size
    print("---------------------")
    for x in S:
        print(x, S.index(x)+1)
    print("---------------------")
    # print(S[1][0]) # {'A': ['mike']}
    # print(list(S[1][0])) # ['A']
    # print(S[10]) [{'!A': ['w']}, {'!C': ['w']}, {'S': ['w']}]
    for first in S:
        for second in S:
            if (len(first) == 1 and len(second) == 1):  # set - set
                skey = list(second[0].keys())
                if (fanyi(skey[0]) == list(first[0].keys())):
                    svalue = list(second[0].values())
                    fvalue = list(first[0].values())
                    if svalue == fvalue:
                        havenewclause = 1
                        S.append([])
                        judge(havenewclause)
                        havenewclause = 0
                        pass
                pass
            elif (len(first) == 1 and len(second) > 1):  # sample - set
                pass
            elif (len(first) > 1 and len(second) == 1):  # set - sample
                firstcopy = copy.deepcopy(second)
                secondcopy = copy.deepcopy(first)
                for x in range(len(secondcopy)):
                    skey = list(secondcopy[x].keys())
                    if (fanyi(skey[0]) == list(firstcopy[0].keys())):
                        newclause = MGU(firstcopy[0], secondcopy[x])
                        if newclause == true:
                            havenewclause = 1
                            temp = copy.deepcopy(secondcopy)
                            del temp[x]
                            S.append(temp)
                            pass
                        elif newclause == false:
                            pass
                        else:
                            havenewclause = 1
                            temp = copy.deepcopy(secondcopy)
                            del temp[x]
                            for y in range(len(temp)):
                                for z in temp[y].values():
                                    for w in newclause.keys():
                                        if w in z:
                                            l = list(temp[y].values())
                                            for v in range(len(l[0])):
                                                if w == z[v]:
                                                    t = list(temp[y].keys())
                                                    temp[y][t[0]
                                                            ][v] = newclause[w]
                                        else:
                                            pass
                            S.append(temp)
                            judge(havenewclause)
                            havenewclause = 0
                    else:
                        pass
                pass
            else:  # set - set
                judge(havenewclause)
                pass
    print("---this is the end---")


path = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath = r'/input5.txt'
# 更换样例测试文件时将input1改为input2或input3即可。
readFile(path + filePath)
print(len(S))
with open(path + filePath) as file_object:
    i = 1
    for linefromfile in file_object:
        print(i, '.', end='', sep='')
        print(linefromfile, end='')
        i += 1
print("")
# set = MGU(S[3][0], S[8][0])
# ty0 = list(set.keys())
# ty = list(S[8][0].keys())
resolution()
