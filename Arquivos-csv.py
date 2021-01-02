# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:30:19 2020

@author: Boson
"""

import csv

caminho = "C:\dados.csv"
lista = []

with open(caminho, 'r') as arqcsv: #abrir arquivo csv
    listagem = csv.reader(arqcsv) #ler o arquivo
    for linha in listagem:    #iterar por cada linha
        for item in linha:  #iterar por cada item da linha
            lista.append(int(item)) #adicionar item à lista
            
lista.sort()
print(lista)
print('Lidos {0} itens'.format(len(lista)))
