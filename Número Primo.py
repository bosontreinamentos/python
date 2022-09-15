# Método simples para verificar se um número é primo

"""
Em teoria dos números, um número natural n é primo se possuir exatamente dois fatores: 1 e o próprio número (n).
Um número i é considerado um fator do número n, se i for divisor exato de n.

A tabela a seguir mostra alguns números, seus fatores, e se são primos ou não:

Número Fatores Primo?
1      1       Não
2      1,2     Sim
3      1,2     Sim
4      1,2,4   Não
5      1,5     Sim
7      1,7     Sim
8      1,2,4,8 Não
9      1,3,9   Não
13     1,13    Sim

O único fator de n que é maior que n/2 é o próprio n.
"""

# Função para determinar se um número é primo - complexidade O(n):
def ePrimo(n):
    # Números iguais ou menores que 1 não são primos 
    if n <= 1:
        return '1 não é número primo!'

    # Verificar de 2 a n / 2
    for i in range(2, n//2):
        if n % i == 0:
            return 'Não é primo'
 
    return 'Sim, o número é primo'

"""
Otimização

Os fatores de um número ocorrem em pares.
Se a é um fator do número n, então também existe um fator b tal que a x b = n.

Pares de fatores - exemplo com o número 18:
a↑  b↓  a x b
1   18  1 x 18 = 18
2   9   2 x 9 = 18
3   6   3 x 6 = 18

Excluindo 1 e o próprio número, se n não for divisível pelos fatores da coluna a, então também não é divisível pelos fatores da coluna b.
Neste caso, o número é primo.

Os valores de a se encontram abaixo da raiz quadrada de n. Assim, basta testar a divisibilidade de n até o valor de sua raiz - o que é muito mais rápido.

# Método otimizado - Complexidade O(√n)
import math
def ePrimo(n):
    # Números iguais ou menores que 1 não são primos 
    if n <= 1:
        return '1 não é número primo!'
    
    # Verificar de 2 a √n    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return 'Não é primo'
    return 'Sim, o número é primo'
"""

# Testar
num = int(input('Entre com o número:'))
print(f'{num} é primo? {ePrimo(num)}')

# Referências: https://geekflare.com/prime-number-in-python/
