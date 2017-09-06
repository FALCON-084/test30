f = open('test.css','r')
def extract_font_size(line):
    '''takes line in css and returns font size as tuple ('fs', 6, 21.95424)'''
    ''' expected format fs6{font-size:21.954240 '''
    #id = int(line[line.find('fs')+2:line.find('{')],16)
    id = line[line.find('fs')+2:line.find('{')]
    if(line[len(line)-1].isdigit() == True) :
        val = line[line.find(':')+1:]
    else :
        val = float(line[line.find(':')+1:line.find('p')])
    return ('fs',id ,val) 
def extract_font_family(line):
    '''takes line in css and returns font family as a tuple ('ff', 2, 1.144)'''
    ''' .ff11{font-family:ff11;line-height:1.115000;font-style:normal;font-weight:normal;visibility:visible;'''
    #id = int(line[line.find('ff')+2:line.find('{')],16)
    id =line[line.find('ff')+2:line.find('{')]
    idx = line.find('line-height:')+12
    val = float(line[idx:idx+line[idx:].find(';')])
    return ('ff',id ,val) 

new_line =f.readline()
lines =[]
while (new_line != '') :
    new_line = new_line[:len(new_line)-2]
    lines.append(new_line)
    new_line =f.readline()
f.close()
#print(lines)
f = open('extracted_css.txt','w')
for line in lines :
    if line.startswith('@font-face'):
        temp = line[line.find('.ff'):]
        write = extract_font_family(temp)
        #print write[0],write[1],write[2]
        f.write(str(write[0] + ' ' + write[1] + ' ' + str(write[2]) ))
        f.write('\n')
    if line.startswith('.fs') and line.find('px') !=-1:
        temp = line[line.find('fs'):line.find('px')]
        write = extract_font_size(line)
        f.write(str(write[0] + ' ' + write[1] + ' ' + str(write[2]) ))
        f.write('\n')
f.close()



     
    



