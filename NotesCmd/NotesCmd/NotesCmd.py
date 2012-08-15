#!/usr/bin/python
# -*- coding: utf-8 -*-
### ::FUNCTION ::  ###


def number_of_line():
        """Liczba linii w pliku"""
        i = 0
        with open("Notes.txt", "r") as NOL:
            for line in NOL:
                try:
                        if line.strip() != False and line[1] != "@":
                                i = i+1
                except IndexError: 
                        pass
        return i
             
#########################
###     DELETE LINES  ###
#########################
def delete(x):
        """Usuwanie linii do podanego momentu"""
        with open("Notes.txt","r") as f:
                items = f.readlines()
        with open("Notes.txt","w") as out:
                for item in items[x:]:
                        out.write("%s\n" % item)
#########################
print "Wybierz\n"
print "|A|dd line\n|R|ead Note File\n|D|elete\n|Q|uit"
choice = "n"
#########################

while choice.lower() != "q":
    choice = raw_input("Twoj wybor:\t")
    if choice.lower() == "a":
        text = raw_input("Podaj notatke. ENTER konczy\n\n")
        with open("Notes.txt","a") as notefile:
                        NOL = number_of_line()+1
                        if text[0] != '@':
                            notefile.write("["+str(NOL)+"] "+text+"\n")
                        else:
                            notefile.write(text+"\n")
        continue
    elif choice.lower() == "r" :
            notefile = open("Notes.txt","r")
            print notefile.read()
            notefile.close()
            continue
    elif choice.lower() == "d":
        x = raw_input("Ile linii usunac?")
        delete(int(x))
        continue
    else:
        continue
