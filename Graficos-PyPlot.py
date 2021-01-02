# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:57:39 2020

@author: Boson
"""
import matplotlib.pyplot as grafico

meses = ['Jan','Fev','Mar','Abr','Mai', 'Jun']
tMed = [30,31,27,26,22,18]

grafico.ylabel('Temp / °C')
grafico.xlabel('Mês',color='blue')
grafico.axis(ymin=0,ymax=40)
grafico.title('Temperaturas Médias Mensais')
#grafico.plot(meses,tMed,label='Temperaturas',marker='o')
grafico.bar(meses,tMed)
grafico.legend()
#grafico.grid(True)

grafico.show()