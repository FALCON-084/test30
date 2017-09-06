''' takes the post tagged words from saiki.txt (u need to run get_saiki.bash first )and retuens the possible nouns from it .'''
f = open('saiki.txt','r')
line = f.readline()
tag =0
buffer = 0
buff =''
temp =''
words= []
line_no=1
while(line != ''):
    line_split=line.split()
    tag =0
    buffer = 0
    buff =''
    temp =''
    for i in range(len(line_split)):
        if(line_split[i].find(str(line_no)+'_CD') !=-1):
            words.append(line_split[i])
            line_no+=1
            continue
        if(line_split[i].find('_N')== -1 and tag ==0 or line_split[i].find('-LRB-_-LRB-')!=-1):
            continue
        elif(line_split[i].find('_N')!=-1 and tag ==0 ):
            tag =1
            buffer = 0
            buff =''
            temp = line_split[i]
        elif(tag == 1):
            if (line_split[i].find('_N')!=-1):
                if(buffer ==1):
                    temp+=' '+buff
                    buff = ''
                    buffer =0
                temp+=' '+line_split[i]
            else :
                if (buffer ==0):
                    buffer = 1
                    buff = line_split[i]
                else :
                    if(temp!=''):
                        temp=temp.lstrip(' ')
                        temp =temp.rstrip(' ')
                        words.append(temp)
                    temp =''
                    buff =''
    else :
        if(temp != ''):
            temp=temp.lstrip(' ')
            temp =temp.rstrip(' ')
            words.append(temp)
    line = f.readline()
f.close()
for i in words:
    print i
f1 = open('nouns.txt','w')
'''note:- _cd may appear between sentences also , change num after find accordingly 6 is for lines upto 99999'''
for i in words:
    if(i.find('_CD')!=-1 and i.find('_CD') <6):
        f1.write(i+'\n')
    else :
        f1.write('\t'+i+'\n')
f1.close()



        


        
        

