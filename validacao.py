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
    return str(digito_gerado)

clear()
# Primeiro digito
while(True):
    # Coletar a soma dos 9 primeiros digitos do cpf
    cpf_input = input('Digite [exit] ou [e] para sair\nDigite um CPF:')

    cpf_input = cpf_input.replace('.', '')
    cpf_separado = cpf_input.split('-')
    try: 
        for cpf in cpf_separado:
            int(cpf)
    except:
        casefold_input = cpf_input.casefold()
        if(casefold_input == 'e' or casefold_input == 'exit'):
            break

        print('Isso não é um número válido.')
        continue

    cpf_completo = cpf_separado[0] + cpf_separado[1]

    #print(*cpf_separado)
    cpf_final = list(cpf_separado[0])

    primeiro_digito = Calculo(cpf_final)
    cpf_final.append(primeiro_digito)

    segundo_digito = Calculo(cpf_final)
    cpf_final.append(segundo_digito)

    cpf_final = ''.join(cpf_final)

    if(cpf_completo != cpf_final):
        print('CPF Inválido!',
               f'CPF digitado:{cpf_completo}',
               f'CPF calculado:{cpf_final}', sep='\n')
    else:
        print('CFP digitado é valido!')



