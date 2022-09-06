# Método simples para verificar se um número é primo
 
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