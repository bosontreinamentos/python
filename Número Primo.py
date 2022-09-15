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
        return False
 
    # Verificar de 2 a n / 2
    for i in range(2, n//2):
        if n % i == 0:
            return False
 
    return True
 
# Testar
num = int(input('Entre com o número:'))
print(f'{num} é primo? {ePrimo(num)}')
