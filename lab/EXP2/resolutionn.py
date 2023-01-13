import os
import sys
from sympy import false, sec, true
import copy

S = []
SS = set()
number = 0


def resolution():
    global S
    havenewclause = 0
    print("---------------------")
    for x in S:
        print(x, S.index(x)+1)
    print("---------------------")
    for first in S:
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
                                                    t = list(temp[y].keys())
                                                    temp[y][t[0]
                                                            ][v] = newclause[w]
                                        else:
                                            pass
                            if temp in S:
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
                                else:
                                    havenewclause = 1
                                    S.append(temp)
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
                                if temp in S:
                                    pass
                                else:
                                    havenewclause = 1
                                    S.append(temp)
                                    print('R[', S.index(first)+1, chr(97+x), ',',
                                          S.index(second)+1, chr(97+y), ']',
                                          end='', sep='')
                                    judge(newclause, havenewclause)
                                havenewclause = 0
                pass
    print("--------fail---------")
    print("---this is the end---")