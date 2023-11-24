#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:41:25 2023

@author: fbo
"""
#generate random number between 0 and 1 
import random # wir brauchen die "random" bibliothek
#random.seed(10)
# lege die random seed fest damit in jedem durchlauf die gleiche sequenz von zahlen gewürflet wird
p_sauber=0.6


#eineListe=eineListe+["text"]
##ToDo: Wiederhole den "Tag im Hühnerstall" 100x!
# .... und füge jeden Tag die Ergebnisse des Tages zu einer Liste hinzu
nWiederholungen=1000
schaetzungsListe=[]
for wIndex in range(nWiederholungen):
    eineListe=[] # erzeuge eine leere liste
    nTage=50
    for tagesIndex in range(nTage):
        anzahlsauber=0 # lege eine strichliste für das zählen der eier an und setze sie auf 0
        nHennen=10
        #print("Die Ergebnis das Tages:")
        # lasse jedes Huhn ein Ei legen und notiere wenn es sauber war:
        for hennenIndex in range(nHennen):
            #print (i) # zur anschaung was das "i" macht
            #führe das zufallsexperiment "eierlegen" innerhalb der schleife aus
            if random.uniform(0,1)<p_sauber:
                #print("sauber")
                anzahlsauber=anzahlsauber+1        # mache einen stich auf die liste 
           # else:
               # print("schmutzig")
        print(anzahlsauber)
        eineListe=eineListe+[anzahlsauber]
    pSaubergeschaetzt=sum(eineListe)/(nTage*nHennen)
    schaetzungsListe=schaetzungsListe+[pSaubergeschaetzt]
print(eineListe)

#plotte ein Histogramm der Werte in der Liste
import matplotlib.pyplot as plt
plt.hist(schaetzungsListe)

