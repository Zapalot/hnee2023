
#Im Kurs erarbeiteter Code:
# Wir simulieren ...
# ...Ein Huhn, welches mit einer bestimmten Wahrscheinlichkeit ein sauberes Ei legt
# ...Zehn Hühner, die das jeweils tun
# ... 100 Tage an denen die Zehn Hühner Eier legen
# ... 1000 Durchgänge des 100Tägigen Versuchs, um zu schauen, wie die im Versuch berechnete Quote sauberer Eier streut

import random # wir brauchen die "random" bibliothek
#random.seed(10) # lege die random seed fest damit in jedem durchlauf die gleiche sequenz von zahlen gewürfelt wird
p_sauber=0.6 # wir legen die Wahscheinlichkeit dass das Ei sauber wird mit 0.6 fest




# führe das gesamte Experiment 1000 mal durch, so dass wir beurteilen können, wie stark die ermittelten p_sauber_geschaetzt werte streuen
nWiederholungen=1000
schaetzungsListe=[] # lege eine leere Liste an, in der wir alle Schätzungen von p_sauber aus den generierten Daten speichern können
for wIndex in range(nWiederholungen): #die "for" schleife geht durch ein Element von dem was nach "in" kommt nach dem anderen.
    #alles was Eingerückt nach dem Doppelpunkt des "for" konstrukts steht wird wiederholt ausgeführt.

	#  Wiederhole den "Tag im Hühnerstall" 100x
	# .... und füge jeden Tag die Ergebnisse des Tages zu einer Liste hinzu
    tagesErgebnisListe=[] # erzeuge eine leere liste, in die wir die tagesergebnisse speichern können
    nTage=100
    for tagesIndex in range(nTage):
        anzahlSauber=0 # lege eine strichliste für das zählen der eier an und setze sie auf 0
        nHennen=10
        #print("Die Ergebnis das Tages:")
        # lasse jedes Huhn ein Ei legen und notiere wenn es sauber war:
        for hennenIndex in range(nHennen):
            #print (i) # zur anschaung was das "i" macht
            #führe das zufallsexperiment "eierlegen" innerhalb der schleife aus
            # ziehe eine zufallsszahl zwischen 0 und 1 -  und wenn sie kleiner war als "pSauber", ist das Ei sauber.
            if random.uniform(0,1)<p_sauber:
                #print("sauber")
                anzahlSauber=anzahlSauber+1        # mache einen stich auf die liste 
           # else:
               # print("schmutzig")
        #print(anzahlSauber) # zeige die anzahl der sauberen Eier dieses Tages an
        #hänhe das Ergebnis des Tages an die Liste der Tagesergebnisse hinten an. 
        tagesErgebnisListe=tagesErgebnisListe+[anzahlSauber]
    # Berechne einen Schätzwert für pSauber anhand der Ergebisse der 100 tage
    pSaubergeschaetzt=sum(tagesErgebnisListe)/(nTage*nHennen)
    schaetzungsListe=schaetzungsListe+[pSaubergeschaetzt]

#plotte ein Histogramm der Werte in der Liste
import matplotlib.pyplot as plt
plt.hist(schaetzungsListe)


