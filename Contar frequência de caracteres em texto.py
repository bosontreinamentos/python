# Contagem de frequência de caracteres em uma string

# Ler string no console
string = input("Digite o texto: ")

# Qual letra consultar?
letra = input("Qual o caractere desejado? ")

# Criar dicionário para frequências
dic_freq = {}

for caractere in string:
    if caractere in dic_freq:
        dic_freq[caractere] += 1
    else:
        dic_freq[caractere] = 1

# Mostrar os resultados
print("\n--------------------------")
print("Caractere\tFrequência")
print("--------------------------")
for caractere, freq in dic_freq.items():
    if (caractere == letra):
        print("%5c\t\t%5d" %(caractere, freq))
        
print("Deseja ver as frequências de todos os caracteres na string? s = sim, n = não")
todos = input()
if (todos == "s"):
    for caractere, freq in dic_freq.items():
        print("%5c\t\t%5d" %(caractere, freq))

print("\nAté mais!")

# TODO: Ler texto de um arquivo em vez de digitado no console
# https://www.codesansar.com/python-programming-examples/find-frequency-character-string.htm