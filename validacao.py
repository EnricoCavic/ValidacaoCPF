import os
import random

def clear():
    os.system('cls')

def cpf_validado(cpf):
    cpf = list(cpf)
    primeiro_digito = calcular_proximo(cpf)
    cpf.append(primeiro_digito)

    segundo_digito = calcular_proximo(cpf)
    cpf.append(segundo_digito)

    return ''.join(cpf)


def calcular_proximo(digitos : list):
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

def gerar(gerar_valido = False):
    retorno_cpf_gerado = ['','']
    for i in range(9):
        retorno_cpf_gerado[0] += str(random.randint(0,9))

    if(not gerar_valido):
        for i in range(2):
            retorno_cpf_gerado[1] += str(random.randint(0,9))
    else:
        gerados = list(retorno_cpf_gerado[0])
        for i in range(2):
            proximo = calcular_proximo(gerados)
            gerados.append(proximo)
            retorno_cpf_gerado[1] += proximo


    return retorno_cpf_gerado

clear()
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

        if(casefold_input == 'gerar'):
            cpf_separado = gerar()
            print(f'CPF gerado:{cpf_separado}')
        elif(casefold_input == 'gerar_validado'):
            cpf_separado = gerar(True)
            print(f'CPF gerado:{cpf_separado}')
        else:
            print('Isso não é um número válido.')
            continue

    cpf_completo = cpf_separado[0] + cpf_separado[1]

    #print(*cpf_separado)

    cpf_gerado = cpf_validado(cpf_separado[0])

    if(cpf_completo != cpf_gerado):
        print('CPF Inválido!',
               f'CPF digitado:{cpf_completo}',
               f'CPF calculado:{cpf_gerado}', sep='\n')
    else:
        print('CFP digitado é valido!')



