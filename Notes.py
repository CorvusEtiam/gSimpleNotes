#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################
###     CONFIG 	        ###
###########################
PATH = "Notes.txt"
###  ::FUNCTION" ::     ###
###########################
### Liczba linii w pliku###
###########################

def NumberOfLine(PATH): #Number of line
        i = 0
        with open(PATH, "r") as NOL:
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
def Delete(PATH,x):
        with open(PATH,"r") as f:
                items = f.readlines()
                f.close()
        with open(PATH,"w") as out:
                for item in items[x:]:
                        out.write("%s\n" % item)

def Add(PATH):
      with open(PATH,"a") as notefile:
                        NOL = NumberOfLine()+1
                        if text[0] != '@':
                            notefile.write("["+str(NOL)+"] "+text+"\n")
                            notefile.close()
                        else:
                            notefile.write(text+"\n")
                            notefile.close()   
def Read(PATH):
        notefile = open("Notes.txt","r")
        print notefile.read()
        notefile.close()







