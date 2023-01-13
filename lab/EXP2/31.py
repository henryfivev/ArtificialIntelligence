import copy
S = []
V={}
M={}
M[0]='a'
M[1]='b'
M[2]='c'
M[3]='d'
M[4]='e'
cot=1
def readClauseSet(filePath):
    global S
    global cot
    for line in open(filePath,encoding = 'utf-8'):
        line = line.replace(' ', '').strip()
        if line[0]=='(':
           line=list(line)
           line[0]=''
           line[len(line)-1]=''
           line=''.join(line)
        for i in range(len(line)-2):
            if line[i+1]==','and line[i]==')':
                line=list(line)
                line[i+1]=';'
                line=''.join(line)
        line = line.split(';')
        newele={}
        for i in range(len(line)):
            str1=line[i]
            for j in range(len(str1)-1):
                str2=str1
                if str1[j]=='(':
                   elename=str2[0:j]
                   elemem=str2[j+1:len(str1)-1]
                   elemem=elemem.split(',')
                   newele[elename]=elemem
                   line[i]=newele 
                   break   
        newele['posnum']=cot
        cot+=1
        S.append(newele)

def opposite(clause):
    if '!' in clause:
        return clause.replace('!', '')
    else:
        return '!' + clause


def resolution():
    global S
    global cot
    print(len(S))
    end = False
    while True:
        if end: break 
        father = S.pop()
        jflag=False
        for i,val in father.items():
            if end: break
            for mother in S:
                if end: break
                j=[]
                pos2=''
                pos3=''
                for key,value in mother.items(): 
                    if key==opposite(i):
                        dif=0
                        for pos1 in value:
                            if pos1 in val:
                                continue
                            else:
                                dif+=1
                                pos2=pos1
                        if dif<=1:
                            for h in range(len(val)):
                                if val[h] in value:
                                    continue
                                else:
                                    pos3=val[h]
                            flag=True
                            for key1 in V.values():
                                if pos2 ==key1:
                                    flag=False
                                    break
                            if flag==True: 
                                j.append(key)
                                break 
                if j == []:
                    continue
                else:
                    jflag=True
                    #print('R[',father['posnum'],',',mother['posnum'],'] = ',end=' ')
                    print('R[',end='')
                    m=0
                    for k1 in father.keys():
                        if k1==i:
                            break
                        m+=1
                    n=0
                    for k2 in mother.keys():
                        if k2==key:
                            break
                        n+=1
                    print(father['posnum'],end='')
                    if len(father)>2:
                        print(M[m],end='')
                    print(',',end='')
                    print(mother['posnum'],end='')
                    if len(mother)>2:
                        print(M[n],end='')
                    print(']',end='')
                    if pos2!='' and pos3!='':
                        print('(',end='')
                        print(pos3,'=',pos2,end='')
                        print(') ',end='')
                    print('= ',end='')
                    newele1={}
                    newele2={}
                    newele1=copy.deepcopy(father)
                    newele2=copy.deepcopy(mother)
                    if pos2!='' and pos3!='':
                        V[pos2]=pos3
                        for vk,v in newele1.items():
                            if vk=='posnum':
                                break
                            for k in range(len(v)):
                                if v[k]==pos3:
                                    v[k]=pos2
                    #print(V)
                    del newele1[i]
                    del newele2[j[0]]
                    if len(newele1)>1:
                        newele1['posnum']=cot
                        cot+=1
                        S.append(newele1) 
                    if len(newele2)>1:
                        newele2['posnum']=cot
                        cot+=1
                        S.append(newele2)
                    S.remove(mother)
                    #print('S:',end=' ')
                    #print(len(S),S)
                    if len(newele1) == 1 and len(newele2) == 1:
                        print('[]')
                        end = True
                    elif len(newele1) == 1:
                        cot2=0 
                        for key,value in newele2.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot2!=len(newele2)-2:
                                print(',',end='')
                            cot2+=1
                        print('\n')
                    elif len(newele2) == 1:
                        cot2=0 
                        for key,value in newele1.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot2!=len(newele1)-2:
                                print(',',end='')
                            cot2+=1
                        print('\n')
                    else:
                        cot2=0 
                        cot3=0
                        for key,value in newele1.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot2!=len(newele1)-2:
                                print(',',end='')
                            cot2+=1
                        print('和',end=' ')
                        for key,value in newele2.items():
                            if key=='posnum':
                                break
                            print(key,'(',end='')
                            for m in range(len(value)):
                                print(value[m],end='')
                                if m!=len(value)-1:
                                    print(',',end='')
                            print(')',end='')
                            if cot3!=len(newele2)-2:
                                print(',',end='')
                            cot3+=1
                        print('\n')
        if jflag==False:
            S.insert(0,father)

def ui():
    print('----')
    print('--------命题逻辑归结推理系统--------')
    print('----')

def main():
    filePath = r'py\\input1.txt'
    readClauseSet(filePath)
    ui()
    print(len(S))
    with open('py\\input1.txt') as file_object:
        contents = file_object.read()
        print(contents)
    resolution()


if __name__ == '__main__':
    main()
