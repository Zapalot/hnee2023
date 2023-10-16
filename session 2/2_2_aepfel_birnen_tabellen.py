#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:17:38 2023

@author: fbo
"""
import pandas as pd
import  matplotlib.pyplot as plt
#Erzeuge eine "Pandas" Tabelle mit Messungen. Je ein Messobjekt je Zeile, und eine Messgröße je Spalte

#mit eckigen Klammern können wir Listen Erzeugen
obstEintragA=['erbeere', 10]
obstEintragB=['erbeere', 15]

#Listen können Teil von anderen Listen sein:
data = [obstEintragA, obstEintragB,['himbeere', 15], ['preiselbeere', 4]] 

#pandas interpretiert eine Liste von Listen als eine Sammlung von Zeilen:
obstTabelle=pd.DataFrame(data,columns=["obstart","gewicht"])


#wir können und Spalten der Tabelle einzeln herausholen, indem wir den Spaltennamen in Eckige Klammern schreiben:
# mehr infos auf https://pandas.pydata.org/docs/user_guide/indexing.html
print(obstTabelle["obstart"])

#wir können Zellen nach ihrer Position in der Tabelle auswählen, indem wir  "iloc" verwenden:
print(obstTabelle.iloc[0,0])

#um ganze Zeilen oder Spalten zu bekommen, können wir einen der Indices mit ":" ersetzen:
print(obstTabelle.iloc[1,:])

#schaue, welche in welchen Zeilen die Spalte "obstart" den Eintrag "erdbeere" enthält (
#Vergleich zwischen zwei Werten mit ==
print(obstTabelle["obstart"]=="erbeere")

#wähle alle Zeilen aus in denen Erbeeren vermessen wurden:
#viele Dinge in python sind nicht unbedingt konsequent logisch, aber praktisch:
# Wenn in den Eckigen Klammern ein Spaltennamen steht, wird der ausgewählt... wenn da eine Liste mit true/False werten steht, gibt es stattdessen eine Auswahl von zeilen
obstTabelle[obstTabelle["obstart"]=="erbeere"]

#mit "groupby" können wir Gruppen bilden:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
obstGruppen=obstTabelle.groupby("obstart")
#damit können wir dann sehr bequem mittelwerte der einzelnen Gruppen ausrechnen:
print(obstGruppen.mean())
################################################### Ein paar Plots
boxplot=obstTabelle.boxplot(by="obstart")
boxplot.set_title('Gewichte unterschiedlicher Obstarten')
plt.suptitle('') # that's what you're after
boxplot.set_ylabel('Gewicht  [g]')
boxplot.set_xlabel('')
################################################## Tabellen aus Dateien lesen und schreiben
# Am einfachsten können wir daten aus textdateien lesen, deren Zellen mit einem immer gleichen Zeichen getrennt sind.
# "\t" steht z.B. für "Tabstop"
# achtung! standard ist der Dezimalpunkt als "Komma", wenn wir etwas anderes wollen müssen wir das explizit angeben

# Daten kopiert aus https://www.kob-bavendorf.de/files/bereiche/Streuobst/Projekte%20Streuobst/EIP%20Robuste%20Apfelsorten/Abschlussbericht_Robuste%20Apfelsorten%20final.pdf
# Tabelle 5: Verkostung von Frühsorten BUGA 2019 / Tabelle 6: Verkostung Herbstapfelsorten BUGA 2019
verkostungsdaten=pd.read_csv("apfelverkostung.txt",sep="\t",decimal=".")


fig1, ax1 = plt.subplots()
ax1.set_title('Geschmack vs. Kaufen')
ax1.scatter(y=verkostungsdaten["Geschmack"],x=verkostungsdaten["Kaufen?"],label="Äpfel")
ax1.set_ylabel('Geschmack')
ax1.set_xlabel('Kaufen?')


### Schreiben ist auch ganz einfach:
obstTabelle.to_csv("beerenobst.txt",sep="\t")


    