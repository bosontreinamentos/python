# Função que calcula o valor de pi usando a fórmula de Leibniz

"""
A fórmula de Leibniz é dada por:
π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
Cada número empregadona fórmula será chamado de "termo".
Quanto maior o número de termos empregados, maior será a precisão do valor de pi obtido.
"""

def leibniz(n):
    soma = 0
    for i in range(n):
        termo = (-1) ** i /(2*i+1)
        soma += termo
    
    return soma * 4

# Usuário indica quantos termos devem ser usados na fórmula
termos = int(input("Enter number of terms: "))

# Executar a função
pi = leibniz(termos)

# Mostrar o resultado
print(f'Valor de Pi = {pi}')
