''' preprocessing read .css file redoreder h1-h5 , rename h1-h5 in html'''

import string
import re
def get_content(line):
    ''' get the text content in div class in html document obtained from pdf2htmlEX '''
    temp =''
    i= 0
    while  i < (len(line)):
        if(line[i] == '>' and line[i:].find('<') > 0 ):
            temp += line[i+1:i+(line[i:].find('<'))]
            i = i + line[i:].find('<')
        i+=1
    return temp
def get_final_content(line):
    split_tags = re.split('<|>',line)
    '''tag_level shows the number of times span is opened within span class
        tag_error shows the number of times span width is opened '''
    tag_level = 0
    tag_error = 0
    tag_buffer =[]
    for i in range(len(split_tags)):
        if split_tags[i].find('div') >-1 :
            split_tags[i] =''
        elif split_tags[i].find('span class=') >-1 :
            if split_tags[i].find('_ _') >-1:
                split_tags[i] =''
                tag_error += 1
            else :
                tag_level +=1
                split_tags[i] = split_tags[i].replace('span class=','')
                temp1 = split_tags[i].split()
                temp = ''
                #removing the other types of formatting info like ls 
                for l in temp1 :
                    if(l.find('ff')!= -1 ):
                        temp += l + ' '
                    if(l.find('fs')!= -1 ):
                        temp += l
                temp = temp.rstrip(' ')
                temp = temp.lstrip(' ')
                temp = temp.rstrip('"')
                temp = temp.lstrip('"')
                if(temp!=''):
                    split_tags[i] ='<'+temp+'>'
                    tag_buffer.append(temp)
                else:
                    tag_level-=1
                    tag_error+=1
        elif split_tags[i].find('/span') >-1 :
            if(tag_error > 0):
                split_tags[i] =''
                tag_error -=1
            elif(tag_level > 0):
                split_tags[i] = '</' + tag_buffer.pop(tag_level-1) + ">" 
                tag_level -= 1
    #print split_tags
    temp = ''
    for i in split_tags :
        temp += i
    return temp

def get_format(line):
    temp =''
    if(line.find('<div class=') == 0):
        temp += line[12:line.find('>')]
        temp = temp [:len(temp)-1]
        return temp
    else :
        print(line,'\nno format found ,please verify that string is of form <div class= and ends with >') 
        return temp
def get_font_format(line):
    temp =''
    if(line.find('<div class=') == 0):
        temp += line[line.find(' ff')+1:line.find('fc')-1]
        temp = temp [:len(temp)]
        return temp
    else :
        print(line,'\nno format found ,please verify that string is of form <div class= and ends with >') 
        return temp




f = open("test.html",'r')
new_line =f.readline()
line_no =0
lines =[]
page_no =[]
while (new_line != '') :
    new_line.replace('</div>','</div>\n')
    lines.append(new_line)
    new_line =f.readline()
f.close()
f1 = open("final_text_no_append.txt",'w')
unref_sentences =[] # contains sentences that may have been cut near eol
for line in lines :
    num = line.count("<div class")
    if (num>1):

        split_list = line.split("<div class",num)
        for i in range(len(split_list)):
            split_list[i] = "<div class" + split_list[i]
            new = get_font_format(split_list[i])
            if(new.find('ff') != -1 ):
                f1.write(new)
                f1.write('\n')
                content =get_final_content(split_list[i])
                if(content != ''):
                    f1.write(content)
                    f1.write('\n')
                    tuple1 = (new,content)
                    unref_sentences.append(tuple1)
f1.close()
#for sentence in unref_sentences :
    #print sentence
#print(unref_sentences)
ref_sentences = []
tag =0
prev_format ,prev_text ='',''
item_id =0
for sentence in unref_sentences:
    now_format = sentence[0]
    now_text = sentence[1]
    if(now_format == prev_format and prev_text[len(prev_text) -1] == ' '):
        prev_text += now_text
    else :
        item_id +=1
        ref_sentences.append((item_id,prev_format,prev_text))
        prev_text = now_text
        prev_format = now_format
    
f1 = open("final_text_appended.txt",'w')
for i in ref_sentences :
    f1.write(str(str(i[0]) + ';;' + str(i[1]) + ';;' + str(i[2])))
    f1.write('\n')
f1.close()



