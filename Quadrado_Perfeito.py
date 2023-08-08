import math

# Função que retorna true se n for quadrado perfeito, e false se não for.
def quadradoPerfeito(x):
    raiz = int(math.sqrt(x))
    return raiz*raiz == x

if __name__=='__main__':
    print("Verificar se número é quadrado perfeito")
    n = float(input('Digite um número qualquer, positivo: '))
    if(quadradoPerfeito(n)):
        print(f"{n} é quadrado perfeito.")
    else:
        print(f"{n} não é quadrado perfeito.")

