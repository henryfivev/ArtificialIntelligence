import os
import sys
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
        number += 1
        S.append(line)

def judge(havenewclause):
    if havenewclause:
        print(S[-1])


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
    for first in S:
        for second in S:
            if (len(first) == 1 and len(second) == 1):
                # set - set
                pass
            elif (len(first) == 1 and len(second) > 1):
                # sample - set
                # first.keys()
                judge(havenewclause)
                pass
            elif (len(first) > 1 and len(second) == 1):
                # set - sample
                judge(havenewclause)
                pass
            else:
                # set - set
                judge(havenewclause)
                pass
    print("---this is the end---")
    


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
print("")
resolution()