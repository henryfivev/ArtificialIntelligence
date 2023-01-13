import copy
import os
import sys
S = []
P = []
V = {}
M = {}
M[0] = 'a'
M[1] = 'b'
M[2] = 'c'
M[3] = 'd'
M[4] = 'e'
cot = 1


def readFile(filePath):
    global S
    global cot
    for line in open(filePath, encoding='utf-8'):
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
            newele = {}
            str1 = line[i]
            for j in range(len(str1)-1):
                str2 = str1
                if str1[j] == '(':
                    elename = str2[0:j]
                    elemem = str2[j+1:len(str1)-1]
                    elemem = elemem.split(',')
                    if elename in newele.keys():
                        str3 = elename+'2'
                        newele[str3] = elemem
                    else:
                        newele[elename] = elemem
                    line[i] = newele
                    break
        line.append(cot)
        cot += 1
        S.append(line)


def fanyi(str1):
    if '!' in str1:
        return str1.replace('!', '')
    else:
        return '!' + str1


def guijie():
    global S
    end = False
    global cot
    global index
    index = 0
    while True:
        if end:
            break
        W = []
        for m in range(len(S)):
            if len(S[m]) == 2:
                W.append(S[m])
        for m in range(len(W)):
            for n in range(m+1, len(W)):
                key1 = list(W[m][0].keys())
                key2 = list(W[n][0].keys())
                value1 = list(W[m][0].values())
                value2 = list(W[n][0].values())
                if key1[0] == fanyi(key2[0]) and value1[0] == value2[0]:
                    end = True
                    print('R[', end='')
                    print(W[m][len(W[m])-1], W[n][len(W[n])-1], end='] = []')
                    break
            if end:
                break
        father = S[index]
        index += 1
        for index1 in range(len(father)-1):
            if end:
                break
            # if index1==len(father)-1:break
            listi = list(father[index1].keys())
            i = listi[0]
            vali = list(father[index1].values())
            val = vali[0]
            for mother in S:
                if end:
                    break
                j = []
                pos2 = ''
                pos3 = ''
                for index2 in range(len(mother)-1):
                    # if index2==len(mother)-1:break
                    keyi = list(mother[index2].keys())
                    key = keyi[0]
                    valuei = list(mother[index2].values())
                    value = valuei[0]
                    if key == fanyi(i):
                        dif = 0
                        for pos1 in value:
                            if pos1 in val:
                                continue
                            else:
                                dif += 1
                                pos2 = pos1
                        if dif <= 1:
                            for h in val:
                                if h in value:
                                    continue
                                else:
                                    pos3 = h
                            flag = False
                            if pos2 == '' and pos3 == '':
                                flag = True
                            if len(pos2) == 1 and len(pos3) > 1:
                                t = pos3
                                pos3 = pos2
                                pos2 = t
                                flag = True
                            if len(pos3) == 1 and len(pos2) > 1:
                                flag = True
                            if flag == True:
                                j.append(key)
                                break
                if j == []:
                    continue
                else:
                    m = 0
                    for k1 in range(len(father)-1):
                        lf = list(father[k1].keys())
                        if lf[0] == i:
                            break
                        m += 1
                    n = 0
                    for k2 in range(len(mother)-1):
                        lm = list(mother[k2].keys())
                        if lm[0] == key:
                            break
                        n += 1

                    p = []
                    p.append(father[len(father)-1])
                    p.append(mother[len(mother)-1])
                    p.sort()
                    pflag = True
                    for p1 in P:
                        if p1 == p:
                            pflag = False
                            break
                    if pflag == False:
                        break
                    P.append(p)
                    newele1 = []
                    newele2 = []
                    newele1 = copy.deepcopy(father)
                    newele2 = copy.deepcopy(mother)
                    for index4 in range(len(newele1)-1):
                        if newele1[index4] == father[index1]:
                            newele1.remove(newele1[index4])
                            break
                    for index4 in range(len(newele2)-1):
                        if newele2[index4] == mother[index2]:
                            newele2.remove(newele2[index4])
                            break
                    if pos2 != '' and pos3 != '':
                        V[pos2] = pos3
                        for index3 in range(len(newele1)-1):
                            listval = list(newele1[index3].values())
                            for k in range(len(listval[0])):
                                if listval[0][k] == pos3:
                                    listval[0][k] = pos2
                        for index3 in range(len(newele2)-1):
                            listval = list(newele2[index3].values())
                            for k in range(len(listval[0])):
                                if listval[0][k] == pos3:
                                    listval[0][k] = pos2
                    n1flag = False
                    for s in S:
                        if len(s) != len(newele1):
                            continue
                        num = 0
                        for index5 in range(len(s)-1):
                            for index6 in range(len(s)-1):
                                if s[index6] == newele1[index5]:
                                    num += 1
                                    break
                        if num == len(s)-1:
                            n1flag = True
                            break
                    n2flag = False
                    for s in S:
                        if len(s) != len(newele2):
                            continue
                        num = 0
                        for index5 in range(len(s)-1):
                            for index6 in range(len(s)-1):
                                if s[index6] == newele2[index5]:
                                    num += 1
                                    break
                        if num == len(s)-1:
                            n2flag = True
                            break
                    if newele1 == newele2:
                        newele2 = []
                    if len(newele1) > 1 and len(newele2) > 1:
                        break
                    if n1flag == True or n2flag == True:
                        break
                    print('R[', end='')
                    print(father[len(father)-1], end='')
                    if len(father) > 2:
                        print(M[m], end='')
                    print(',', end='')
                    print(mother[len(mother)-1], end='')
                    if len(mother) > 2:
                        print(M[n], end='')
                    print(']', end='')
                    if pos2 != '' and pos3 != '':
                        print('(', end='')
                        print(pos3, '=', pos2, end='')
                        print(') ', end='')
                    print('= ', end='')
                    if len(newele1) > 1:
                        newele1[len(newele1)-1] = cot
                        cot += 1
                        S.append(newele1)
                    if len(newele2) > 1:
                        newele2[len(newele2)-1] = cot
                        cot += 1
                        S.append(newele2)
                    if len(newele1) <= 1 and len(newele2) <= 1:
                        print('[]')
                        end = True
                    elif len(newele1) <= 1:
                        cot2 = 0
                        print(newele2[len(newele2)-1], '.', end='')
                        for index7 in range(len(newele2)-1):
                            item = newele2[index7]
                            ki = list(item.keys())
                            vi = list(item.values())
                            print(ki[0], '(', end='')
                            for m in range(len(vi[0])):
                                print(vi[0][m], end='')
                                if m != len(vi[0])-1:
                                    print(',', end='')
                            print(')', end='')
                            if cot2 != len(newele2)-2:
                                print(',', end='')
                            cot2 += 1
                        print('\n')
                    elif len(newele2) <= 1:
                        cot2 = 0
                        print(newele1[len(newele1)-1], '.', end='')
                        for index7 in range(len(newele1)-1):
                            item = newele1[index7]
                            ki = list(item.keys())
                            vi = list(item.values())
                            print(ki[0], '(', end='')
                            for m in range(len(vi[0])):
                                print(vi[0][m], end='')
                                if m != len(vi[0])-1:
                                    print(',', end='')
                            print(')', end='')
                            if cot2 != len(newele1)-2:
                                print(',', end='')
                            cot2 += 1
                        print('\n')


def main():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filePath = r'/input3.txt'
    # 更换样例测试文件时将input1改为input2或input3即可。
    readFile(path+filePath)
    print(len(S))
    with open(path+filePath)as file_object:
        i = 1
        for line in file_object:
            print(i, '.', end='')
            print(line, end='')
            i += 1
    print('\n')
    guijie()


if __name__ == '__main__':
    main()
