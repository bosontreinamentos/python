# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:26:09 2021

@author: Fábio dos Reis
"""

import csv
import math
import matplotlib.pyplot as plt

# Caminho do arquivo .csv
caminho = 'C:\Arquivos\dados.csv'

# Criar lista vazia para receber dados do arquivo csv:
lista=[]

# Abrir arquivo csv e carregar seus dados na lista:
with open(caminho,'r') as arqcsv:
    linhas = csv.reader(arqcsv) #ler o arquivo
    for linha in linhas:    #iterar por cada linha
        for item in linha:  #iterar por cada item da linha
            lista.append(int(item)) #adicionar item à lista

# Ordenar lista (rol)
lista.sort()

# Visualizar conteúdo da lista lida:
for item in lista:
    print(item)
    
# Ver lista
print('\nLista ordenada:', lista)

# Ver tamanho da lista (número de elementos):
n = len(lista)
print('\nLidos {0} elementos'.format(n))

# Calcular amplitude total (range - R)
R = max(lista) - min(lista)
print("Amplitude total:",R)

# Calcular número de classes K usando fórmula de Sturges
K = round(1 + 3.32 * math.log10(n))
print("Número de classes:",K)

# Calcular as amplitudes das classes
h = round(R / K)
print("Amplitude de cada classe:",h)

# Criar as classes
classes = []
for i in range(K):
    classes.append(i+1)
print('Classes:',classes)
    
# Função para determinar a frequência de cada valor na lista
freqValor = {}
def freq(lista):

    for i in lista:
        if freqValor.get(i):
            freqValor[i] += 1
        else:
            freqValor[i] = 1
    return freqValor

#print("\nFrequência de cada valor na lista:\n", freq(lista))

# Determinar os intervalos de classes e frequências absolutas
freq(lista)
listaClasses = []
soma = 0
freqAbs = []
inicioClasse = min(lista)
for i in range(K):
    fimClasse = inicioClasse + h   
    # iterar pelo dicionário e preencher lista com frequências absolutas
    for chave in freqValor.keys():
        if chave >= inicioClasse and chave <= fimClasse:
            soma += freqValor[chave]
    freqAbs.append(soma)
    soma = 0
    # Lista de classes para histograma:
    listaClasses.append(inicioClasse)
    # Próximo intervalo de classes
    inicioClasse = fimClasse + 1
listaClasses.append(fimClasse)
print("\nFreq Absolutas:",freqAbs)

# Mostrar tabela de frequências absolutas Fi
inicioClasse = min(lista)
print("\nTabela de Frequências Absolutas")
for i in range(K):
    fimClasse = inicioClasse + h  
    print(inicioClasse,"-",fimClasse,": ",freqAbs[i])
    inicioClasse = fimClasse + 1

# Plotar histograma usando Matplotlib
plt.style.use('ggplot')
plt.hist(lista, bins = listaClasses)
plt.title("Histograma");
plt.show()


# Frequências relativas das classes (Fi)
freqRel = []
for i in freqAbs:
    freqRel.append((i / n) * 100)
print('Fequências Relativas:\n',freqRel)

# Mostrar tabela de frequências relativas fi
inicioClasse = min(lista)
print("\nTabela de Frequências Relativas")
for i in range(K):
    fimClasse = inicioClasse + h  
    print('{} - {}: {:.2f}%'.format(inicioClasse,fimClasse,freqRel[i]))
    inicioClasse = fimClasse + 1
freqTotal = 0
for i in freqRel:
    freqTotal += i
print('Total: {}%'.format(freqTotal)) 
   
''' TODO: Frequências absolutas e relativas acumuladas '''
    