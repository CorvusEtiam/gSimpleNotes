#!/usr/bin/python
# -*- coding: utf-8 -*-
### ::FUNCTION" ::  ###

###########################
### Liczba linii w pliku###
###########################
def NumberOfLine(): #Number of line
        i = 0
        with open("Notes.txt", "r") as NOL:
            for line in NOL:
                try:
                        if line.strip() != False and line[1] != "@":
                                i = i+1
                except IndexError: 
                        pass
        NOL.close()
        return i
             
#########################
###     DELETE LINES  ###
#########################
def Delete(x):
        with open("Notes.txt","r") as f:
                items = f.readlines()
                f.close()
        with open("Notes.txt","w") as out:
                for item in items[x:]:
                        out.write("%s\n" % item)
#########################
print "Wybierz\n"
print "|A|dd line\n|R|ead Note File\n|D|elete\n|Q|uit"
choice = "N"
#########################

while(choice != "Q"):
    choice = raw_input("Twoj wybor:\t")
    if(choice == "A" or choice == "a"):
        text = raw_input("Podajﾹ notatke. ENTER konczy\n\n")
        with open("Notes.txt","a") as notefile:
                       
                        NOL = NumberOfLine()+1
                        if text[0] != '@':
                            notefile.write("["+str(NOL)+"] "+text+"\n")
                            notefile.close()
                        else:
                            notefile.write(text+"\n")
                            notefile.close()
        continue
    elif(choice == "R" or choice == "r"):
            notefile = open("Notes.txt","r")
            print notefile.read()
            notefile.close()
            continue
    elif(choice == "D"):
        x = raw_input("Ile linii usunac?")
        Delete(int(x))
        continue
    else:
        continue
