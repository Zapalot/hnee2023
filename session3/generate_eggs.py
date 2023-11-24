#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:08:11 2023

@author: fbo
"""
#eier generieren
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta

startDate=date.fromisoformat('2023-12-04')
dateInterval = timedelta(days=1)
nDates=100


mischungen=['dinkel', 'stroh', 'sand']
staelle=[1,2]
curObservation=0

mischungsWahrscheinlichkeitSauber={'dinkel':0.8, 'stroh':0.9, 'sand':0.6}


stallAnzahlHuehner={1:10.0,2:13.0}
stallLegeWahrscheinlichkeit={1:0.9,2:0.85}
rows=[]
for i in range(nDates):
    curDate=pd.to_datetime(startDate+i*dateInterval)
    for curStall in staelle:
        gesamtEier=np.random.binomial(stallAnzahlHuehner[curStall], stallLegeWahrscheinlichkeit[curStall])
        for curMisch in mischungen:
            anzahlSauber=np.random.binomial(gesamtEier,mischungsWahrscheinlichkeitSauber[curMisch])
            anzahlSchmutzig=gesamtEier-anzahlSauber
            rows.append({
                "beaobachtungsnummer":curObservation,
                'tag':curDate,
                'stall':curStall,
                'mischung':curMisch,
                'anzahl_sauber':anzahlSauber,
               'anzahl_schmutzig':anzahlSchmutzig,
                    'kommentar':"alles nur ein traum", 
                    'messende person':"generiert"                
                })
            curObservation=curObservation+1
eggTable=pd.DataFrame(rows)
eggTable.to_csv("generierte_eier.txt",sep="\t",decimal=".", encoding = "ISO-8859-1",date_format='%d.%m.%Y')
