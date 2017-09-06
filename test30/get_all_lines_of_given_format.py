import json
''' goal extract all words of the given format '''
freq = []
f =open('ff_stats','r')
line = f.readline()
while(line!=''):
    freq.append((line.split()[0],int(line.split()[1])))
    line = f.readline()
f.close()
f =open('fs_stats','r')
line = f.readline()
while(line!=''):
    freq.append((line.split()[0],int(line.split()[1])))
    line = f.readline()
f.close()
f =open('font_format_stats','r')
line = f.readline()
while(line!=''):
    freq.append((line.split()[0]+' '+line.split()[1],int(line.split()[2])))
    line = f.readline()
f.close()
print freq
given_format = raw_input("enter format to search for:")
#given_format='fs1'
f =open('final_text_appended.txt','r')
line = f.readline()
answer =''
if(given_format.find(' ')!=-1):
    print 'if'
    #this means format is of form ffx fsy
    for i in freq:
        if(i[0] == given_format):
            print "There are over "+str(freq[1])+"sentences matching , do you want to print them?"
            answer =raw_input("enter y to continue:")
            break
    if(answer == 'y'):
        ff_no= given_format.split()[0]
        fs_no= given_format.split()[1] 
        direct =[]
        span_class =[]
        while(line!=''):
            if(line.find(given_format)!=-1):
                direct.append(line)
            elif( line.find(ff_no)!=0 and line.find(fs_no)!=0):
                span_class.append(line)
            line = f.readline()
    else :
        pass
else :
    print 'else'
    for i in freq:
        if(i[0] == given_format):
            print 'if'
            print "There are over "+str(i[1])+" sentences matching , do you want to print them?"
            answer =raw_input("enter y to continue:")
            break
    if(answer == 'y'):
        direct =[]
        while(line!=''):
            if(line.find(given_format)!=-1):
                direct.append(line)
            line = f.readline()
        for i in direct:
            print i        
    f.close()
# with open('formats.json','r') as fp:
#     data = json.load(fp)
# #json.dump(data,indent = 4,sort =True)
# for i in data.keys():
#     print i , 