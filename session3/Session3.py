#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#importiere pakete
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

#Lese die Tabelle ein
# mittels der "parse_dates" und "date_format" argumente können wir pandas dazu bringen die daten in der Tabelle richtig einzulesen
# mit der "encoding" anganbe sorgen wir für eine richtige darstellung von sonderzeichen und umlauten
# beides muss zu dem passen, was (z.B. in Excel oder Libreoffice) zum Abspeichern der Tabelle verwendet wurde
experimentaldaten=pd.read_csv("generierte_eier.txt",sep="\t",decimal=".", encoding = "ISO-8859-1",parse_dates=["tag"], date_format="%d.%m.%y")

#Auswertung der Daten in der Tabelle

#Häufig wollen wir Gruppen miteinander vergleichen.
#Dazu sind zwei Ansätze hilfreich:
# 2.a): Gruppierung mit "pandas group_by" --> Das macht vieles automatisch, ist aber manchmal etwas undurchschaubar oder unflexibel
# 2.b): Auswahl eines Teils der zeilen der Tabelle, mit bestimmten Eigenschaften


###########
# 2.a): Gruppierung mit "pandas group_by" (https://pandas.pydata.org/docs/user_guide/groupby.html))

 #Erzeugt ein Objekt, in dem die Zeilen der Tabelle nach Gruppen mit gleicher "Mischung" Gruppiert sind.
gruppiertNachMischung=experimentaldaten.groupby("mischung")

#jetzt können wir uns ganz bequem statistische kenngrößen zu den Gruppen ausrechnen:
print("mittelwerte:") 
print(gruppiertNachMischung["anzahl_sauber"].mean())

print("Standardabweichungen:") 
print(gruppiertNachMischung["anzahl_sauber"].std())

print("Summen:") 
print(gruppiertNachMischung["anzahl_sauber"].sum())

# wir können auch nach zwei oder mehr merkmalen gruppieren: dann bekommt jeder Kombination dieser Merkmale eine eigene Gruppe:
gruppiertNachMischungUndStall=experimentaldaten.groupby(["mischung","stall"])   
print("gruppiertNachMischungUndStall:") 
print(gruppiertNachMischungUndStall["anzahl_sauber"].mean())

#durch clevere Gruppenbildung lassen sich auch alle Daten zu jeder Mischung jedes Tags aufsummeieren:
tagesSummen=experimentaldaten.groupby(["tag","mischung"]).sum()

###########
# 2.b): Auswahl von Zeilen anhand von Merkmalen

#Wir können feststellen, ob Zeilen zu einer bestimmten Gruppe gehören, indem wir einen Vergleich mit == anstellen:
gehoertZu1=   experimentaldaten["stall"]==1 
print(gehoertZu1)

#mit dieser information können wir z.B. Zeilen aus der Tabelle auswählen:
alleAus1=experimentaldaten[gehoertZu1] 
# dass das geht ist zunächst erstmal verwunderlich:
#eben haben wir noch Spalten ausgewählt, indem wir sie in die Eckigen Kammern geschrieben haben
# jetzt verwenden wir exakt die gleiche Syntax für eine Zeilenauswahl!
#
# Woher weiß Pandas ob wir Spalten oder Zeilen meinen?
# --> Es aus Form (genausoviele Einträge wie das df Zeilen hat) und Inhalt (booleans) der zur Indizierung verwendeten Variable, was es tun soll.
# Das ist euch unheimlich? (was könnte schief gehen?!)... dann vielleicht besser explizit:
    
alleAus1mitLoc=experimentaldaten.loc[gehoertZu1,:] # vor dem Komma stehen die Zeilenindices, danach die Spaltenindices. ":" bedeutet "alle"

#so können wir auch gleich sowohl nach Spalten als auch nach Zeilen filtern:
sauberAus1=experimentaldaten.loc[gehoertZu1,"anzahl_sauber"]
schmutzigAus1=experimentaldaten.loc[gehoertZu1,"anzahl_schmutzig"]

#... und dann z.B. die Summe ausrechnen:
gesamtSauberAus1=sauberAus1.sum()
gesamtSchmutzigAus1=schmutzigAus1.sum()

anteilSauber=gesamtSauberAus1/(gesamtSauberAus1+gesamtSchmutzigAus1)

##############
# 3) Berechnungen von von zusätzlichen Merkmalen

# wir können ganz einfach zwei Spalten addieren:
experimentaldaten["anzahl_gesamt"]=experimentaldaten["anzahl_sauber"]+experimentaldaten["anzahl_schmutzig"]
experimentaldaten["anteil_sauber"]=experimentaldaten["anzahl_sauber"]/experimentaldaten["anzahl_gesamt"] #was passiert wenn "anzahl_gesamt" irgendwo 0 ist?!

# wir probieren es aus:
experimentaldaten.loc[0,"anzahl_gesamt"]=0
experimentaldaten.loc[0,"anzahl_sauber"]=0
experimentaldaten.loc[0,"anzahl_schmutzig"]=0
experimentaldaten["anteil_sauber"]=experimentaldaten["anzahl_sauber"]/experimentaldaten["anzahl_gesamt"] #was passiert wenn "anzahl_gesamt" irgendwo 0 ist?!

print(experimentaldaten.loc[0,"anteil_sauber"]) # 0/0 gibt "nan" (das steht für "not a number")

# diese "nan"s können wir mit der pandas funktion "isnull" finden und ausschließen
print(experimentaldaten.isnull())

#in unserem Fall macht es vielleicht Sinn in diesen Fällen den Aneil einfach auf "0" zu setzen:
experimentaldaten.loc[experimentaldaten["anteil_sauber"].isnull(),"anteil_sauber"]=0

###########
# 4) Erzeugen von Grafiken
# Auch hier gibt's wieder viele unterschiedliche Möglichkeiten sehr ähnliche Resultate zu erzeugen
# Wie können direkt die Plotfukntionen von Pandas verwenden:
#https://www.statology.org/pandas-groupby-plot/
#
# Oder (und ich finde das führt schneller zum Ergebnis) Seaborn:
# Die Logik dabei ist, dass für verschiedene Achsen bzw. Unterscheidungsmerkmale
# (x, y, hue/"farbton", style/"linienstrichelung") jeweils eine Spalte aus der Tabelle angegeben kann:

#so können wir z.B. fix ein Box-Plot der nach Stall und Mischung aufgeteilten Legedaten erstellen:
plt.subplots() # erzeuge ein neues plot fenster
plotAxes= sns.boxplot(experimentaldaten, x="stall",y="anzahl_sauber",hue="mischung") 
plotAxes.set_title('Saubere Eier')

# Oder die Anzahl der gelegten Eier pro Tag über die zeit auftragen
plt.subplots() # erzeuge ein neues plot fenster
sns.lineplot(tagesSummen,x="tag",y="anzahl_sauber",hue="mischung")

# die Beispielseiten von Seaborn sind lassen keine Wünsche offen - hier habe ich z.B. nach einer Darstellung gesucht,
# in der die verschiedenen Klassen nebeneinander stehen und mit "multiple="dodge"" gefunden:
# https://seaborn.pydata.org/generated/seaborn.histplot.html
plt.subplots()
sns.histplot(experimentaldaten,x="anzahl_sauber",hue="mischung", multiple="dodge")

#############
# Iteration durch die Daten mit "for" Schleifen
#
#wenn uns die in Pandas eingebauten Möglichkeiten nicht reichen können wir selbst mit einer "for" schleife durch die Daten gehen und mit einzelnen Gruppen davon etwas machen:

ergebnisse=pd.DataFrame(columns=["tag","anteil"])
alleUnterschiedlichenTage=experimentaldaten["tag"].unique()
for aktuellerTag in alleUnterschiedlichenTage: #mit "for" können wir den gleichen Code für jedes Element aus einer Menge durchführen.
    alleDatenMitDiesemTag=experimentaldaten.loc[experimentaldaten["tag"]==aktuellerTag,:] #wähle einen Teil der Daten aus
    summeSauber=alleDatenMitDiesemTag["anzahl_sauber"].sum()
    print(summeSauber)
    
############################S  
# Konfidenzintervalle:
# Ein sehr nützliches Maß für die Sicherheit mit der wir eine Zahl bestimmt haben ist der /Konfidenzintervall/
#
# Wenn wir davon ausgehen, dass jedes einzelne Ei jeweils mit einer bestimmten Wahrscheinlichkeit verschmutzt wird,
# ergibt sich daraus, dass sie Anzahl der sauberen bzw. schmutzigen Eier Binomialverteilt ist.
#
# wir nehmen also an: aus n insgesamt gelegten eiern ist jedes einzelne mit einer Wahrscheinlichkeit p schmutzig. beobachtet haben wir k schmutzige
# .... dann können wir die Funktion scipy.stats.binomtest verwenden um das Konfidenzintervall für p zu berechnen:
import scipy.stats as stats #unser hypothesentest liegt in scipy.stats

# wir wollen uns die beiden Ställe getrennt anschauen:
stallgruppen=experimentaldaten.groupby("stall")
eiersummen=stallgruppen[["anzahl_sauber","anzahl_schmutzig"]].sum() #und berechnen für jeden Stall die gesamtanzahl der sauberen bzw. schmutzigen eier:

print(eiersummen)
#für stall nummer 1:
print("####Stall no 1:")
summeSauber=eiersummen.loc[1,"anzahl_sauber"]
summeGesamt=eiersummen.loc[1,:].sum()
anteilSauber=summeSauber/summeGesamt
print("Anteil Sauber:"+str(anteilSauber))
print(stats.binomtest (summeSauber,summeGesamt).proportion_ci())
print("####Stall no 2:")
summeSauber=eiersummen.loc[2,"anzahl_sauber"]
summeGesamt=eiersummen.loc[2,:].sum()
anteilSauber=summeSauber/summeGesamt
print("Anteil Sauber:"+str(anteilSauber))
print(stats.binomtest (summeSauber,summeGesamt).proportion_ci())

#### und das gleiche nochmal mit einer schleife: (das macht so richtig Sinn wenn es viele einträge gibt)
eiersummen["anzahl_gesamt"]=eiersummen["anzahl_sauber"]+eiersummen["anzahl_schmutzig"]
eiersummen["anteil_sauber"]=eiersummen["anzahl_sauber"]/eiersummen["anzahl_gesamt"]
eiersummen["anteil_sauber_untere_grenze"]=0.0 #wir schaffen platz für die daten aus dem testmodul
eiersummen["anteil_sauber_obere_grenze"]=0.0 #wir schaffen platz für die daten aus dem testmodul


for index, row in eiersummen.iterrows():
    print(eiersummen.loc[index,"anzahl_sauber"])
    print(row["anzahl_sauber"])
    ci=stats.binomtest (int(row["anzahl_sauber"]),int(row["anzahl_gesamt"])).proportion_ci() # mit int() wandeln wir eine zahl in eine "integer" also Ganzzahl um. (sonst beschwert sich)
    eiersummen.loc[index,"anteil_sauber_untere_grenze"]=ci.low
    eiersummen.loc[index,"anteil_sauber_obere_grenze"]=ci.high
    
#das lässt sich auch schön grafisch darstellen:
    


############################Statistische tests:
# Unterscheiden sich Stall 1 und 2 im Anteil der dort gelegten sauberein Eier?
#
# --> Jedes einzelne Ei hat eine gewisse Wahrscheinlichkeit, nach dem Legen entweder sauber (S) oder nicht Sauber (\S) zu sein.
# Die Summe dieser Wahrscheinlichkeiten ist gleich 1 P(S)+P(\S)=1
# Wir nehmen als Nullhypothese an, dass diese Wahrscheinlichkeiten in beiden Ställen gleich sind: P_1(S)=P_2(S)
#

# Wir verwenden Fishers exact test, um zu überprüfen, wie wahrscheinlich unter den
# Bedingungen der Nullhypothese eine Verteilung von sauber/dreckig herauskommt,
# die mindestens ebenso extrem von  der Gleichverteilung abweicht wie die beobachtete.
stallgruppen=experimentaldaten.groupby("stall")
eiersummen=stallgruppen[["anzahl_sauber","anzahl_schmutzig"]].sum()
import scipy.stats as stats #unser hypothesentest liegt in scipy.stats
stats.fisher_exact(eiersummen)


#########
#Exkurs: Boschloos test

#res = stats.boschloo_exact(eiersummen)
#print("Wahrscheinlichkeit, dass die selben oder extremere Daten herauskommen, wenn die Ställe gleiche Veerschmutzungswahrscheinlichkeiten haben: "+str( res.pvalue))

# Macht es einen Unterschied, wenn wir Zeilen und Spalten vertauschen?
# In der Dokumentation der Funktion steht dazu nichts... Also probieren wir es mal aus:
#res_t = stats.boschloo_exact(eiersummen.transpose())
#print("Wahrscheinlichkeit, dass die selben oder extremere Daten herauskommen, wenn die Ställe gleiche Veerschmutzungswahrscheinlichkeiten haben: (gedreht)"+str( res_t.pvalue))

# verdammt, da kommt wirklich etwas anderes heraus...
# Woran liegt's?
#
# Im Wikipedia-Artikel https://en.wikipedia.org/wiki/Boschloo%27s_test ist eine ganz gute Erklärung:
# Kurz gefasst: Es scheint etwas damit zu tun zu haben, ob die Randsummen der Spalten oder der Zeilen 
# als fest oder zuällig angesehen werden.
# Im Wiki-Artikel sind die Zeilensummen fest und die Spaltensummen zufällig.
# (Das entspricht in unserem Fall der Tabelle "eiersummen" der Annahme dass die Anzahl der Eier pro Stall fest ist, und die Anzahl der Sauberen jeweils zufällig)
#
# Interessanterweise ist in der Dokumentation https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boschloo_exact.html
# ein Beispiel, in dem es genau umgekehrt ist!

# Schauen wir also vielleich einfach mal in die Originalquelle:
#https://sci-hub.ru/10.1111/j.1467-9574.1970.tb00104.x
# hier wird einiges klarer, und das Layout entspricht dem Wikipedia-Artikel.

# google : boschaloos transpose
#ergibt das hier: https://github.com/scipy/scipy/issues/13896

# Alles klar?!  


 