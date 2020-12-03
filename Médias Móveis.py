# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:05:44 2020

@author: Fábio dos Reis
"""

import matplotlib.pyplot as plt

valores = [21.95,21.84,21.9,21.98,21.65,22.11,22.50,22.75,23.21,23.1,23.20,22.78,22.30,23.17,23.24,23.26,23.23,23.13,23.27,23.38,23.42,23.68,23.20,22.84,23.01,23.00,23.11,23.24,23.46,23.27,23.02,22.82,23.31] # cotações diárias
tam_grupo = 5 # deslocamento (uma semana útil)

i = 0
medias_moveis=[]

while i < len(valores) - tam_grupo + 1:
    grupo = valores[i : i + tam_grupo]
    media_grupo = sum(grupo) / tam_grupo
    medias_moveis.append(media_grupo)
    i +=1

# Exibir a lista de médias móveis
for valor in medias_moveis:
    print(round(valor,2))
    
# Gerar lista com dias do mês
dia_mes = []
for dia in range(1,len(medias_moveis)+1):
    dia_mes.append(dia)
    
""" TODO: Adicionar linha de tendência """
    
# Visualizar gráfico de médias móveis
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.title('Médias Móveis')
plt.axis(ymin=21,ymax=24,xmin=0,xmax=30)
plt.plot(dia_mes,medias_moveis,marker='o')
plt.style.use('seaborn')
plt.show()