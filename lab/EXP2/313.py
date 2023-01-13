import os
import sys
from sympy import false, true

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
        #line.append(number)
        #number += 1
        S.append(line)


def MGU(a, b):
    valueset = {}
    alist = [x for x in a.values()]
    blist = [x for x in b.values()]
    if alist == blist:
        return true
    else:
        for x in range(len(alist)):
            if (alist[x] in blist[x]) and (alist[x] != blist[x]):
                break
            else:
                valueset[alist[x][0]] = blist[x][0]
                alist[x][0] = blist[x][0]
    if alist != blist:
        return false
    return valueset


def Resolution():
    global S
    tr = S[0]

    # set - set go to MGU



    print("this is the end")
    


path = os.path.abspath(os.path.dirname(sys.argv[0]))
filePath = r'/input3.txt'
# 更换样例测试文件时将input1改为input2或input3即可。
readFile(path + filePath)
print(len(S))
with open(path + filePath) as file_object:
    i = 1
    for linefromfile in file_object:
        print(i, '.', end='', sep='')
        print(linefromfile, end='')
        i += 1
print('\n')
MGU(S[3][0], S[8][0])
Resolution()