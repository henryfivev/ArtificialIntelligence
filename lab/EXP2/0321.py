import os
import sys
from sympy import false, sec, true
import copy

S = []
SS = []
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
    if SS[-1] == []:
        print("[]", end="")
    for x in SS[-1]:
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


def repeat(a:'list'):

    sset = set(a)


def resolution():
    global S
    global SS
    S.sort(key = lambda i:len(i))
    longest = len(S[-1])-1
    havenewclause = 0
    print("---------------------")
    for x in S:
        print(x, S.index(x)+1)
    print("---------------------")
    print("----现用支持集策略----")
    first = S[0]
    for second in S:
        if [] in SS:
            return
        if (len(first) == 1 and len(second) == 1):  # set - set
            skey = list(second[0].keys())
            if (fanyi(skey[0]) == list(first[0].keys())):
                newclause = MGU(first[0], second[0])
                if newclause == true:
                    havenewclause = 1
                    SS.append([])
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
                    SS.append([])
                    print('R[', S.index(first)+1, ',',
                            S.index(second)+1, ']',
                            end='', sep='')
                    judge(newclause, havenewclause)
                    havenewclause = 0
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
                        if temp in SS:
                            pass
                        elif len(temp) > longest:
                            pass
                        else:
                            SS.append(temp)
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
                                                t = list(temp[y].keys())
                                                temp[y][t[0]
                                                        ][v] = newclause[w]
                                    else:
                                        pass
                        if temp in SS:
                            pass
                        elif len(temp) > longest:
                            pass
                        else:
                            SS.append(temp)
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
                        if temp in SS:
                            pass
                        elif len(temp) > longest:
                            pass
                        else:
                            SS.append(temp)
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
                                                t = list(temp[y].keys())
                                                temp[y][t[0]
                                                        ][v] = newclause[w]
                                    else:
                                        pass
                        if temp in SS:
                            pass
                        elif len(temp) > longest:
                            pass
                        else:
                            SS.append(temp)
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
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                havenewclause = 1
                                SS.append(temp)
                                print('R[', S.index(first)+1, chr(97+x), ',',
                                        S.index(second)+1, chr(97+y), ']',
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
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                havenewclause = 1
                                SS.append(temp)
                                print('R[', S.index(first)+1, chr(97+x), ',',
                                        S.index(second)+1, chr(97+y), ']',
                                        end='', sep='')
                                judge(newclause, havenewclause)
                            havenewclause = 0
            pass
    S.sort(key = lambda i:len(i))
    SS.sort(key = lambda i:len(i))
    for first in SS:
        for second in S:
            if SS.index(first) > 10:
                break
            if [] in SS:
                return
            if (len(first) == 1 and len(second) == 1):  # set - set
                skey = list(second[0].keys())
                if (fanyi(skey[0]) == list(first[0].keys())):
                    newclause = MGU(first[0], second[0])
                    if newclause == true:
                        havenewclause = 1
                        SS.append([])
                        print('R[', SS.index(first)+1+len(S), ',',
                                S.index(second)+1, ']',
                                end='', sep='')
                        judge(newclause, havenewclause)
                        havenewclause = 0
                        pass
                    elif newclause == false:
                        pass
                    else:
                        havenewclause = 1
                        SS.append([])
                        print('R[', SS.index(first)+1+len(S), ',',
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
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                                                    t = list(temp[y].keys())
                                                    temp[y][t[0]
                                                            ][v] = newclause[w]
                                        else:
                                            pass
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                                                    t = list(temp[y].keys())
                                                    temp[y][t[0]
                                                            ][v] = newclause[w]
                                        else:
                                            pass
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                                if temp in SS:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    havenewclause = 1
                                    SS.append(temp)
                                    print('R[', SS.index(first)+1+len(S), chr(97+x), ',',
                                            S.index(second)+1, chr(97+y), ']',
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
                                if temp in SS:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    havenewclause = 1
                                    SS.append(temp)
                                    print('R[', SS.index(first)+1+len(S), chr(97+x), ',',
                                            S.index(second)+1, chr(97+y), ']',
                                            end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                pass
    S.sort(key = lambda i:len(i))
    SS.sort(key = lambda i:len(i))
    # circle 3
    for first in SS:
        for second in S:
            if SS.index(first) > 10:
                break
            if [] in SS:
                return
            if (len(first) == 1 and len(second) == 1):  # set - set
                skey = list(second[0].keys())
                if (fanyi(skey[0]) == list(first[0].keys())):
                    newclause = MGU(first[0], second[0])
                    if newclause == true:
                        havenewclause = 1
                        SS.append([])
                        print('R[', SS.index(first)+1+len(S), ',',
                                S.index(second)+1, ']',
                                end='', sep='')
                        judge(newclause, havenewclause)
                        havenewclause = 0
                        pass
                    elif newclause == false:
                        pass
                    else:
                        havenewclause = 1
                        SS.append([])
                        print('R[', SS.index(first)+1+len(S), ',',
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
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                                                    t = list(temp[y].keys())
                                                    temp[y][t[0]
                                                            ][v] = newclause[w]
                                        else:
                                            pass
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                                                    t = list(temp[y].keys())
                                                    temp[y][t[0]
                                                            ][v] = newclause[w]
                                        else:
                                            pass
                            if temp in SS:
                                pass
                            elif len(temp) > longest:
                                pass
                            else:
                                SS.append(temp)
                                print('R[', SS.index(first)+1+len(S), ',',
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
                                if temp in SS:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    havenewclause = 1
                                    SS.append(temp)
                                    print('R[', SS.index(first)+1+len(S), chr(97+x), ',',
                                            S.index(second)+1, chr(97+y), ']',
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
                                if temp in SS:
                                    pass
                                elif len(temp) > longest:
                                    pass
                                else:
                                    havenewclause = 1
                                    SS.append(temp)
                                    print('R[', SS.index(first)+1+len(S), chr(97+x), ',',
                                            S.index(second)+1, chr(97+y), ']',
                                            end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                pass
    print("--------fail---------")
    print("---this is the end---")


path = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath = r'/input3.txt'
# 更换样例测试文件时将input1改为input2或input3即可。
readFile(path + filePath)
resolution()


"""
现将S[0]设为目标公式的否定
先遍历S[0]对S
再遍历SS对S

明天try
SSS
sort list----优先尝试子句归结
"""