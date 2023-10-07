#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:14:14 2023

@author: fbo
"""
import skimage as ski                     #Eine praktische Bibliothek zum arbeiten mit Bildaten 
import matplotlib.pyplot as plt           #Eine Bibliothek zum Erstellen von Plots

#Lade das Bild mit den Tomaten
tomatenbild = ski.io.imread("tomaten.png")

########Das Bild anzeigen
plt.figure("Ganzes Bild")   #Erzeuge eine neue Grafik /"Figure"
imgplot = plt.imshow(tomatenbild) #Füge das Bild zu der zuletzt erzeugten Figure hinzu
plt.show()  #zeige die Figure an

# Einen Ausschnitt aus dem Bild in eine separate tabelle kopieren
minX=767 
maxX=minX+30
minY=446
maxY=minY+30
subImage=tomatenbild[ minY:maxY, minX:maxX ] # mit den Eckigen klammern kann ein Bereich angegeben werden, der ausgewählt wird.

#Den Ausschnitt anzeigen
plt.figure("Ausschnitt Tomate")
imgplot = plt.imshow(subImage)
plt.show()

figure=plt.figure("Histogramm der Rotwerte")
rotWerte=subImage[:,:,0].ravel()# die Histogrammfunktion braucht ein Array mit nur einer Zeile, keine Tabelle. "Ravel" wandelt das um
plt.hist(rotWerte)

# Der Plot bekommt noch ein paar Beschriftungen
plt.title('Histogramm der Rotwerte')
plt.xlabel('Rot-intensität')
plt.xlim([0,255])
plt.ylabel('Anzahl')
plt.show()