import os

def clear():
    os.system('cls')
    

# Primeiro digito

# Coletar a soma dos 9 primeiros digitos do cpf
cpf_input = input('Digite um cpf:')

cpf_input = cpf_input.replace('.', '')
cpf_separado = cpf_input.split('-')

try: 
    for cpf in cpf_separado:
        int(cpf)
except:
    print('Isso não é um número')


print(*cpf_separado)

cpf1_separado = list(cpf_separado[0])
# Multiplique os valores por uma contagem regressiva começando de  10
# Somar o resultado de todos os resultados da contagem regressiva

soma_iteracao = 0
index = 10
for valor in cpf1_separado:
    soma_iteracao += int(valor) * index
    index -= 1 

# Multiplicar por 10
soma_iteracao *= 10

# Obter o resto da divisão do resultado por 11
sobra =  soma_iteracao % 11

# Se o resultado > 9 ele deve ser zero
primeiro_digito = 0 if sobra > 9 else sobra

# Else o resultado não é alterado
print(primeiro_digito)
