# Dengue Free Feira - MI Algoritimos - Problema 2

import csv
from datetime import datetime as dt
import sys


cor = {
    'base': '\033[m',
    'pt': '\033[30m',
    'vm': '\033[31m',
    'vd': '\033[32m',
    'am': '\033[33m',
    'az': '\033[34m',
    'ma': '\033[35m',
    'ci': '\033[36m',
    'bc': '\033[37m',
}


# Exceções
class NegativeNumberError(Exception):
    pass


print(f'\n{cor["ma"]}{" TELA INICIAL ":=^73}')
print(f'{cor["ci"]}'
    ' Escolha a opção que deseja executar:\n\n'
    ' [ 1 ] Visualição de Dados\n'
    ' [ 2 ] Atualização de Dados\n'
    ' [ 3 ] Encerrar o programa')
opcoes = ['1' , '2', '3']
escolha = ''
while escolha not in opcoes:
    escolha = str(input(' Escolha uma opção: '))
    if escolha not in opcoes:
        print(' Erro Entrada invalida')
if escolha == '1':
    print(f'{cor["ci"]}'
        ' Escolha o intervalo de exibição dos dados:\n\n'
        ' [ 1 ] Ultima Atualização\n'
        ' [ 2 ] Especificar data\n'
        ' [ 3 ] Especificar intervalo entre datas\n'
        ' [ 4 ] Retornar ao menu anterior')
    opcoes = ['1' , '2', '3', '4']
    escolha = ''
    while escolha not in opcoes:
        escolha = str(input(' Escolha uma opção: '))
        if escolha not in opcoes:
            print(' Erro Entrada invalida')
    if escolha == '1':
        print('Ultima Atualização')
        print(f'\n{cor["ma"]}{" Modo de Exibição ":=^73}')
        print(f'{cor["ci"]}'
            ' Escolha o modo de exibição dos dados:\n\n'
            ' [ 1 ] Todos os bairros\n'
            ' [ 2 ] Apenas um bairro\n'
            ' [ 3 ] Retornar ao menu anterior\n')
        opcoes = ['1' , '2', '3']
        escolha = ''
        while escolha not in opcoes:
            escolha = str(input(' Escolha uma opção: '))
            if escolha not in opcoes:
                print(' Erro Entrada invalida')

    elif escolha == '2':
        print('Escolha de Data')
        print(f'\n{cor["ma"]}{" Modo de Exibição ":=^73}')
        print(f'{cor["ci"]}'
            ' Escolha o modo de exibição dos dados:\n\n'
            ' [ 1 ] Todos os bairros\n'
            ' [ 2 ] Apenas um bairro\n'
            ' [ 3 ] Retornar ao menu anterior\n')
        opcoes = ['1' , '2', '3']
        escolha = ''
        while escolha not in opcoes:
            escolha = str(input(' Escolha uma opção: '))
            if escolha not in opcoes:
                print(' Erro Entrada invalida')

    elif escolha == '3':
        print('Escolha do Intervalo')
        print(f'\n{cor["ma"]}{" Modo de Exibição ":=^73}')
        print(f'{cor["ci"]}'
            ' Escolha o modo de exibição dos dados:\n\n'
            ' [ 1 ] Todos os bairros\n'
            ' [ 2 ] Apenas um bairro\n'
            ' [ 3 ] Retornar ao menu anterior\n')
        opcoes = ['1' , '2', '3']
        escolha = ''
        while escolha not in opcoes:
            escolha = str(input(' Escolha uma opção: '))
            if escolha not in opcoes:
                print(' Erro Entrada invalida')

    elif escolha == '4':
        print('Retornar')

elif escolha == '2':
    print('Atualizar Dados')
