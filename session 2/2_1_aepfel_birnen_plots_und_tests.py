import numpy as np
import  matplotlib.pyplot as plt


# simuliere ein paar Äpfel. Wir verwenden dazu eine Normalverteilung mit vorgegebenen Mittelwert und Standardabweichung.
# In der Realität kennen wir diese nicht, sondern versuchen sie aus den gemessenen Daten zu schätzen.
# Das kann nie exakt gelingen, weil die gemessenen Daten Einflüssen unterliegen, die wir nicht unter unserer Kontrolle haben
# Das nennen wir dann alles "Zufall"

apfelAnzahlProben=100
apfelMengenVerteilungMittelwert=100
apfelMengeStandardAbweichung=20

birnenAnzahlProben=10
birnenMengenVerteilungMittelwert=110
birnenMengeStandardAbweichung=15

# erzeuge ein Array mit zufälligen Zahlen, die aus eine Normalverteilung gezogen werden.
# diese Zahlen können wir später anstelle eines echten Experiments verwenden um ein bisschen damit herumzuspielen
apfelMengenSamples=np.random.normal(apfelMengenVerteilungMittelwert, apfelMengeStandardAbweichung,apfelAnzahlProben)
birnenMengenSamples=np.random.normal(birnenMengenVerteilungMittelwert, birnenMengeStandardAbweichung,birnenAnzahlProben)


############################## Berechne Den Mittelwert und die Standardabweichung der zufällig gezogenen Stichprobe aus der Normalverteilung

# der 
durchschnittApfelMengenProben=np.mean(apfelMengenSamples)
durchschnittBirnenMengenProben=np.mean(birnenMengenSamples)

medianApfelMengenProben=np.median(apfelMengenSamples)
medianBirnenMengenProben=np.median(birnenMengenSamples)

sdApfelMengenProben=np.std(apfelMengenSamples)
sdBirnenMengenProben=np.std(birnenMengenSamples)



#############Stelle die gezogenen Zahlen auf unterschiedliche Art und Weise dar
fig1, ax1 = plt.subplots() #damit machen wir ein neues Plot-Fenster auf
ax1.set_title('Äpfel')
ax1.hist(apfelMengenSamples,label='Äpfel') 
ax1.legend()
ax1.set_xlabel('Menge [kg]')
ax1.set_xlabel('Anzahl der Samples mit dieser Menge')


############Stelle beides in einem Plot dar:
    
#matplotlib interpretiert mehrere numpy arrays in einer Liste als mehrere Datenreihen die getrennt nebeneinander in einem Plot dargestellt werden.
# wir packen also beide sammlungen von Stickproben in eine gemeinsame Liste:
alleSamples=[apfelMengenSamples,birnenMengenSamples] # mit [a,b] legen wir eine Liste an, die beide unterschiedlichen Datensätze enthält.
alleNamen= ["Äpfel","Birnen"]


#als Histogramm
fig1, ax1 = plt.subplots()
ax1.set_title('Äpfel vs. Birnen')
ax1.hist(alleSamples,label=alleNamen) 
ax1.legend()
ax1.set_xlabel('Menge [kg]')
ax1.set_xlabel('Anzahl der Samples mit dieser Menge')


# als Boxplot
fig1, ax1 = plt.subplots()
ax1.set_title('Äpfel vs. Birnen')
ax1.set_ylabel('Menge [kg]')
ax1.set_xlabel('Fruchtart')
ax1.boxplot(alleSamples)
plt.xticks([1, 2], ['Äpfel','Birnen']) #hiermit kommen die labels an die richtigen stellen 



# Die Datenpunkte an sich
xPlotCenters=[1,2]
plotLabels=["Äpfel","Birnen"]

fig1, ax1 = plt.subplots()
ax1.set_title('Äpfel vs. Birnen')
ax1.scatter(y=apfelMengenSamples,x=[1]* apfelAnzahlProben,label="Äpfel",alpha=0.2)
ax1.scatter(y=birnenMengenSamples,x=[2]* birnenAnzahlProben,label="Birnen",alpha=0.2)
plt.xticks(xPlotCenters, plotLabels)
ax1.legend()

#und mit ein bisschen Rauschen in der X-Achse für bessere unterscheidbarkeit:
fig1, ax1 = plt.subplots()
ax1.set_title('Äpfel vs. Birnen')

apfelXpos=np.random.random(apfelAnzahlProben) *0.2+1
birneXpos=np.random.random(birnenAnzahlProben) *0.2+2
ax1.scatter(y=apfelMengenSamples,x=apfelXpos,label="Äpfel",alpha=0.2)
ax1.scatter(y=birnenMengenSamples,x=birneXpos,label="Birnen",alpha=0.2)
plt.xticks(xPlotCenters, plotLabels)
plt.xlim([0.5,2.5])
ax1.legend()



############################# Wie wahrscheinlich ist es, dass die Apfel- und Birnenmengen aus der gleichen Normalverteilung stammen?

# unterscheiden sich Äpfel und Birnen wirklich? Oder beruhen die Abweichungen in unserer Stichprobe nur auf zufälligen Schwankungen?

#..... unter der Annahme, dass sowohl Apfel- als auch Birnenmengen einer normalverteilung folgen, 
# können wir ausrechnen, wie wahrscheinlich es ist, dass wir den gleichen oder einen noch größeren Unterschied beobachten, obwohl beide aus der gleichen Verteilung kommen.

#wir machen dazu einen t-Test auf "abweichung er Mittelwerte von Proben aus einer Normalverteilung"
# Stichproben sind "unabhängig" - also keine paarweisen Samples
import scipy
import math
#https://en.wikipedia.org/wiki/Student%27s_t-test
print(scipy.stats.ttest_ind(apfelMengenSamples,birnenMengenSamples))
# der oben ausgegebene "p-value" entspricht der oben erläuterten Wahscheinlichkeit, dass die Stichprobe mindestend so unterschielich ausfällt wie beobachtet,
# -obwohl sie aus der gleichen verteilung gezogen wurde


# und rechnen ein Konfidenzinterval aus
# Das Konfidenzintervall enthält mit x%iger Wahrscheinlichkeit den wahren Mittelwert.
# ..d.h. ein 95% Konfidenzintervall rund um den Beobachteten Durchschnitt durchschnittApfelMengenProben enthält in 95% der Fälle apfelMengenVerteilungMittelwert

#https://en.wikipedia.org/wiki/Student%27s_t-distribution

durchschnittApfelMengenKonfidenzIntervall=scipy.stats.t.interval(0.95,df=apfelAnzahlProben-1, loc=durchschnittApfelMengenProben, scale=sdApfelMengenProben / np.sqrt(apfelAnzahlProben))
durchschnittBirnenMengenKonfidenzIntervall=scipy.stats.t.interval(0.95,df=birnenAnzahlProben-1, loc=durchschnittBirnenMengenProben, scale=sdBirnenMengenProben / np.sqrt(apfelAnzahlProben))

print("Der Mittelwert der Apfelernten liegt mit 95% Wahrscheinlichkeit irgendwo zwischen "+str(durchschnittApfelMengenKonfidenzIntervall[0])+" und "+str(durchschnittApfelMengenKonfidenzIntervall[1]))

#das können wir auch grafisch darstellen:
#leider will matplotlib die werte für die "error bars" als differenzen zum dargestellen wert, deshalb müssen wir das erstmal umrechnen
apfelErrors=(durchschnittApfelMengenProben-durchschnittApfelMengenKonfidenzIntervall[0],durchschnittApfelMengenKonfidenzIntervall[1]-durchschnittApfelMengenProben)
birnenErrors=(durchschnittBirnenMengenProben-durchschnittBirnenMengenKonfidenzIntervall[0],durchschnittBirnenMengenKonfidenzIntervall[1]-durchschnittBirnenMengenProben)

fig1, ax1 = plt.subplots()
plt.bar(x=[0,1],height=[durchschnittApfelMengenProben,durchschnittBirnenMengenProben], yerr=[apfelErrors,birnenErrors])
plt.xticks([0,1], ['Äpfel','Birnen']) #hiermit kommen die labels an die richtigen stellen 
ax1.set_ylabel('Menge [kg]')
ax1.set_xlabel('Fruchtart')
