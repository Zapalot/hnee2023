#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1.1)Tabelle einlesen
# schaut in der Datein "2_2_aepfel_birnen_tabellen.py", wie dort eine Tabelle eingelesen aus einer Datei eingelesen wird.
# Lest mit dieser Methode die Tabelle "iris.txt" ein.

irisdaten=pd.read_csv("iris.txt",sep="\t",decimal=".")
 "c:/alle meine daten/eier.txt"



#1.2)Spalten aus der Tabelle auswählen
# schaut in der Datein "2_2_aepfel_birnen_tabellen.py", wie dort eine Spalte aus der Tabelle ausgewählt wird.
# Speichert die Spalte "Petal.Width" in eine eigene Variable 
petalWidths=irisdaten["Petal.Width"]

#1.3) Daten darstellen als Histogramm:
# macht ein Plot, welches die Verteilung der PetalBreiten in einem Histogramm darstellt.

fig1, ax1 = plt.subplots() #damit machen wir ein neues Plot-Fenster auf
ax1.set_title('Iris')
ax1.hist(petalWidths,label="Petal.Width") 


#1.4) Reflektion:
# Folgen die Zuckergehalte einer Normalverteilung? Auf was könnte die Form des Histogramm hindeuten?


#1.5.) Darstellung von zwei Spalten als Scatterplot
#  benutzt die matplotlib-funktion "scatter", um die Datenpunkte darzustellen.
# Dabei soll "Sepal.Width" auf der x-Achse dargestellt werden, "Petal.Width" auf der y-Achse

#was fällt euch auf?
fig1, ax1 = plt.subplots()
ax1.scatter(y=irisdaten["Petal.Width"],x=irisdaten["Sepal.Width"])



#1.6.) Darstellung mit labels / installation des "seaborn" pakets
# Eigentlich hätten wir ja gerne ein Plot, in dem die Spezies farbig unterscheidbar sind und es eine Legende dazu gibt.
# oder gleich so ein schickes "pair" Plot wie hier:
#https://en.wikipedia.org/wiki/Iris_flower_data_set

#Mit matplotlib geht das, ist aber ein Haufen Arbeit...
# Einfacher geht es mit dem zusatzpaket "seaborn".
# Um das zu installieren:
# 1.6.1) Terminal aufmachen
# 1.6.2) Environment aktivieren: "mamba activate hnee2023"
# 1.6.3) Paket installieren: "mamba install seaborn"
# 1.6.4) hier im Code weiterarbeiten:  "import seaborn as sns" und dann ein Beispiel aus https://seaborn.pydata.org/generated/seaborn.pairplot.html anpassen.
import seaborn as sns
sns.pairplot(irisdaten, hue="Species")
#1.8 Mittelwerte ausrechnen
# schaut euch in "2_2_aepfel_birnen_tabellen.py" an, wie dort Mittelwerte für Gruppen von Werten in einem Pandas-Dataframe ausgerechnet werden, und macht das genauso mit den Iris Daten







