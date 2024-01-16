import os

def clear():
    os.system('cls')

def Calculo(digitos : list):
    # Multiplique os valores por uma contagem regressiva começando de  10
    # Somar o resultado de todos os resultados da contagem regressiva
    soma_iteracao = 0
    index_regressivo = len(digitos) + 1
    for valor in digitos:
        soma_iteracao += int(valor) * index_regressivo
        index_regressivo -= 1 

    # Multiplicar por 10
    # Obter o resto da divisão do resultado por 11
    sobra =  (soma_iteracao * 10) % 11

    # Se o resultado > 9 ele deve ser zero
    # Else o resultado não é alterado
    digito_gerado = 0 if sobra > 9 else sobra
    return digito_gerado

# Primeiro digito

clear()
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
digitos_iniciais = list(cpf_separado[0])

primeiro_digito = str(Calculo(digitos_iniciais))
digitos_iniciais.append(primeiro_digito)
segundo_digito = Calculo(digitos_iniciais)
print(primeiro_digito, segundo_digito)
