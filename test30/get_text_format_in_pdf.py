f =open('final_text_appended.txt','r')
text = raw_input('enter the text you want to know stats for:')
guesses = []
lines =[]
line = f.readline()
while(line!=''):
    lines.append(line)
    if(line.find(text)!=-1):
        guesses.append(line)
    line = f.readline()
if(len(guesses) ==0):
    print("there are no guesses , try again")
elif(len(guesses) ==1):
    print guesses[0].split(';;')[1]
    print guesses[0]
else :
    print "There are over "+str(len(guesses))+" sentences matching , do you want to print them?"
    answer =raw_input("enter n to continue i.e print them: or y to refine it:")
    if(answer == 'n'):
        for i in guesses:
            print i.split(';;')[1]
            print i
    elif(answer == 'y'):
        answer =raw_input("type a word or phrase that occurs in next or prev sentence to refine")
        ref_word_guess =[]
        size =len(lines)
        for i in range(len(guesses)):
            idx = int(guesses[i].split(';;')[0])
            if(idx >3):
                for j in range(idx-2,idx+3):
                    if(line[j].find(answer)!=-1):
                        ref_word_guess.append(guesses[i])
                        break
        print "There are over "+len(guesses)+" sentences matching , do you want to print them?"
        for i in ref_word_guess:
            print i 

            