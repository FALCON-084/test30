import json
f = open('final_text_appended.txt','r')
lines =[]
line = f.readline()
while(line!=''):
    lines.append(line)
    line = f.readline()
formats = {}
fs_sorted_dict ={}
ff_sorted_dict ={}
for line in lines:
    line = line.replace('\n','')
    temp = line.split(';;')
    if(temp[1].find('fs') != -1 and temp[1].find('ff') != -1):
        key = temp[1]
        if(key in formats.keys()):
            formats[key].append(temp[2])
        else :
            formats[key] = []
            formats[key].append(temp[2])
        key = temp[1][temp[1].find('ff'):temp[1].find(' ')]
        if(key in ff_sorted_dict.keys()):
            ff_sorted_dict[key].append(temp[2])
        else :
            ff_sorted_dict[key] = []
            ff_sorted_dict[key].append(temp[2])
        key = temp[1][temp[1].find('fs'):]
        if(key in fs_sorted_dict.keys()):
            fs_sorted_dict[key].append(temp[2])
        else :
            fs_sorted_dict[key] = []
            fs_sorted_dict[key].append(temp[2])



f1 = open('font_format_stats','w')
for k in sorted(formats, key=lambda k: len(formats[k]), reverse=True):
    print k ,len(formats[k])
    f1.write(k +' '+ str(len(formats[k])) +' '+'\n' )
f1.close()
with open('formats.json', 'w') as fp1:
    json.dump(formats, fp1, sort_keys=True, indent=4)

f2 = open('ff_stats','w')
for k in sorted(ff_sorted_dict, key=lambda k: len(ff_sorted_dict[k]), reverse=True):
    print k ,len(ff_sorted_dict[k])
    f2.write(k +' '+ str(len(ff_sorted_dict[k])) +' '+'\n' )
f2.close()
with open('ff.json', 'w') as fp2:
    json.dump(ff_sorted_dict, fp2, sort_keys=True, indent=4)

f3 = open('fs_stats','w')
for k in sorted(fs_sorted_dict, key=lambda k: len(fs_sorted_dict[k]), reverse=True):
    print k ,len(fs_sorted_dict[k])
    f3.write(k +' '+ str(len(fs_sorted_dict[k])) +' '+'\n' )
f3.close()
with open('fs.json', 'w') as fp3:
    json.dump(fs_sorted_dict, fp3, sort_keys=True, indent=4)