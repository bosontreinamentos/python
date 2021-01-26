# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:32:27 2021

@author: Fábio dos Reis
"""

def soma(x, y):
    return x + y

print('Programa para somar dois números')

n1 = input('Entre com um número: ')
n2 = input('Entre com outro número: ')

res = soma(n1,n2)

print('\nResultado da soma: {0}'.format(res))