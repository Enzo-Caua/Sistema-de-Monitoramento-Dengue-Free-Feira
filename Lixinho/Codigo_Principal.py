# Dengue Free Feira - MI Algoritimos - Problema 2


import csv
from datetime import datetime as dt
from datetime import timedelta as tmd
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


# Função 'Abrir Arquivo'
def abrir_arquivo(modo, lista_dados_atualizados):
   
    arquivo_valido = False

    while not arquivo_valido:
        try:
            # Abrir em Modo de Leitura
            if modo == 'r':
                with open('dengue_free_feira2.csv', 'r') as arquivo:
                    leitor = csv.reader(arquivo, delimiter=",")
                    lista_dados = list(leitor)
                    arquivo_valido = True
                    return lista_dados
            
            # Abrir em Modo de Atualização
            elif modo == 'a':
                with open('dengue_free_feira2.csv', 'a', newline='') as arquivo:
                    editor = csv.writer(arquivo, delimiter=",")
                    editor.writerow(lista_dados_atualizados)
                    print(f'{cor["vd"]} Dados Atualizados com Sucesso!')
                    arquivo_valido = True
        except FileNotFoundError:
            print(f'{cor["vm"]} ERRO: Arquivo Não Encontrado!')
            print(' Encerrando o programa! Revise o arquivo base!')
            sys.exit()           


# Função 'Exibir e Escolher Bairro'
def bairros_lista():
    lista_bairros = []
    bairro_escolhido = 0
    bairro_valido = False
    dados = abrir_arquivo('r', None)
    
    # Condição caso o arquivo esteja vazio
    if dados == []:
        print(f'{cor["vm"]} ERRO:Arquivo Vazio! Por Favor Adicione os Dados.')
        """ Chamar Função Atualizar Dados ou Inserir Novos Dados """

    # Exibe todos os bairros enumerados
    for i, linha in enumerate(dados):
        if i == 0:
                print(f'\n{cor["ma"]}{f' {linha[1]} ':=^73}')
        elif i < 26:
            print(f"{cor['ci']}{i} - {linha[1]}")
            lista_bairros.append(linha[1])

    # Escolha do Bairro
    """ Adicionar a possibilidade de mais bairros """
    while not 0 < bairro_escolhido < 26 and not bairro_valido:
        try:
            bairro_escolhido = int(input(f'{cor["bc"]}'
                                         ' Informe o numero do Bairro: '))
            if bairro_escolhido < 0:
                raise NegativeNumberError(f'{cor["vm"]}ERRO: '
                                          ' Digite apenas numeros positivos!')
            bairro = lista_bairros[(bairro_escolhido - 1)]
            print(f'Bairro Escolhido: {bairro}\n')
            bairro_valido = True
        except IndexError:
            print(' Bairro Não Existente!')
        except ValueError:
            print(' Entrada Invalida! Digite Novamente!')
        except NegativeNumberError as e:
            print(e)
    return bairro


# Função 'Escolha de Opçoes'
def escolha_opcao(opcoes):
    escolha = ''
    while escolha not in opcoes:
        escolha = str(input(' Escolha uma opção: '))
        if escolha not in opcoes:
            print(' Erro Entrada invalida')
    return escolha  


# Função 'Menu Inicial'
def menu_inicial():
    print(f'\n{cor["ma"]}{" TELA INICIAL ":=^73}')
    print(f'{cor["ci"]}'
        ' Escolha a opção que deseja executar:\n\n'
        ' [ 1 ] Visualição de Dados\n'
        ' [ 2 ] Atualização de Dados\n'
        ' [ 3 ] Encerrar o programa')
    lista_opcoes = ['1' , '2', '3']
    return lista_opcoes

# Função 'Menu de Periodo'
def menu_periodo():
    print(f'\n{cor["ma"]}{" Periodo de Exibição ":=^73}')
    print(f'{cor["ci"]}'
        ' Escolha o intervalo de exibição dos dados:\n\n'
        ' [ 1 ] Ultima Atualização\n'
        ' [ 2 ] Especificar data\n'
        ' [ 3 ] Especificar intervalo entre datas\n'
        ' [ 4 ] Retornar ao menu anterior')
    lista_opcoes = ['1' , '2', '3', '4']
    return lista_opcoes


# Função 'Menu de Exibição'
def menu_exibicao():
    print(f'\n{cor["ma"]}{" Modo de Exibição ":=^73}')
    print(f'{cor["ci"]}'
        ' Escolha o modo de exibição dos dados:\n\n'
        ' [ 1 ] Todos os bairros\n'
        ' [ 2 ] Apenas um bairro\n'
        ' [ 3 ] Retornar ao menu anterior\n')
    lista_opcoes = ['1' , '2', '3', '4']
    return lista_opcoes

# Codigo Principal
print(f"""
\n{cor["ma"]}{' SEJA BEM VINDO AO SISTEMA DENGUE FREE FEIRA ':=^73}{cor['vd']}
\n A  dengue  é uma doença endêmica viral transmitida principalmente pelos 
 mosquitos Aedes aegypti e Aedes albopictus. O sistema Dengue Free Feira
 foi  desenvolvido  com o objetivo de fornecer o acesso a dados precisos 
 sobre  a incidência da dengue e a situação epidemiológica em diferentes 
 regiões da cidade de Feira de Santana, para auxiliar no monitoramento e
 controle da dengue.""")

