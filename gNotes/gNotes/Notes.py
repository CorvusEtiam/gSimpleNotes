#!/usr/bin/python
# -*- coding:utf-8 -*-
try:import cPickle as pickle
except: import pickle

# import pickle lub cpickle
"""
Example: 
    dict = {Numer:Wartość}
    path = ./<lokalizacja>

"""
class Core(object):
    """
    Klasa centralna
    """
    def __init__(self):
        """
        Inicjacja wartosci poczatkowych. Pozniej przenies do osobnego pliku *.conf
        """
        self.path = "./Notes.p"
        self.dict = {}     
    def pickler(self,text):
        """
        serializacja wartości
        """
        with open(self.path, "wb") as fopen:
            fopen = pickle.dump(text,self.path)
            
    def unpickler(self):
        """
        deserializacja wartości  
        """
        with open(self.path,"rb") as foutput:
            outdict = pickle.load(foutput)
            return outdict
        
    def lenght(self,stat = False):    
        """
        Liczba wierszy
        """
        if stat == False:
            return len(self.dict)
        else:
            for key in self.dict.iterkeys():
                print key + " : " + self.dict.get(key)
    
    def delete(self,key):
        """
        Usuwanie klucza z pliku
        """
        dictionary = self.unpickler()
        self.lenght(stat = True)
        del dictionary[key]
        self.pickler(dictionary)
        
    def list(self):
        i = 0
        output = self.unpickler()
        for i in output.iterkeys():
            i = i+1
        return
    def append(self,text):
        output = self.unpickler()
        ls = self.list()
        output[ls+1] = text
    def Spec(self,text): 
        pass       
class Extension(object):
    """Do dodania w najblizszym mozliwym terminie"""
    pass

     
        
            
        