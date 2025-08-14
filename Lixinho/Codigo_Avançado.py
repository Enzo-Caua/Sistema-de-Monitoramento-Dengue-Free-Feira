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


# Permite visualizar os dados da ultima atualização de um unico bairro ou de tds
def visualizacao_ultima_att():
    dados = abrir_arquivo('r', None)
    data_min = dt.min.date()
    i = 1
    bairro = 'Tomba'
    
    # Verifica a data da ultima atualização
    for datas_csv in dados:
        if datas_csv[0] == 'Data':
            None
        elif datas_csv[1] == bairro:
            data = dt.strptime(datas_csv[0], '%d/%m/%Y').date()
            if data > data_min:
                data_min = data
        elif bairro == None:
            data = dt.strptime(datas_csv[0], '%d/%m/%Y').date()
            if data > data_min:
                data_min = data

    #Exibe somente os dados da data da ultima atualizaçao
    for datas_csv in dados:
        if datas_csv[0] == 'Data':
            None
        elif datas_csv[1] == bairro:
            data_x = dt.strptime(datas_csv[0], '%d/%m/%Y').date()
            if data_x == data_min and i < 10:
                print(i, ' -', datas_csv)
                i += 1
            elif data_x == data_min and i >= 10:
                print(i, '-', datas_csv)
                i += 1
        elif bairro == None:
            data_x = dt.strptime(datas_csv[0], '%d/%m/%Y').date()
            if data_x == data_min and i < 10:
                print(i, ' -', datas_csv)
                i += 1
            elif data_x == data_min and i >= 10:
                print(i, '-', datas_csv)
                i += 1

# Atualizar os dados automaticamente caso não haja atualização de um dia pra o
# outro: Verifica qual foi a data da ultima atualização, pega essa data e adicona~
# mais 1 e junta ela com os dados do dia anterior


# Função para escolha do periodo dos dados
def escolha_periodo():

    # Variaveis
    data_inicial_valido = False
    data_final_valido = False
    data_inicial = data_final = dt.min

    # Validação da data inicial
    while not data_inicial_valido:
        try:
            data_i = str(input('Data Inicial: '))
            data_inicial = dt.strptime(data_i, '%d/%m/%Y')
            data_inicial_valido = True
        except ValueError as ve:
            if "day is out of range for month" in str(ve):
                print('Data inexistente para esse mês!')
            else:
                print('Data Invalida! Siga o padrão "dia/mes/ano"')

    # Validação da data final
    while not data_final_valido:
        try:
            data_f = str(input('Data Final: '))
            data_final = dt.strptime(data_f, '%d/%m/%Y')

            # Verificação se a data final não é anterio a data inicial
            if data_inicial < data_final:
                data_final_valido = True
            elif data_inicial > data_final:
                print('Data final anterior a data inicial!')
            else:
                print('Tem alguma coisa errada!')
        except ValueError as ve:
            if "day is out of range for month" in str(ve):
                print('Data não existente nesse mês!')
            else:
                print('Data Invalida! Siga o padrão "dia/mes/ano"')
    return data_inicial, data_final


def filtro_periodo():
    
    data_inicial, data_final = escolha_periodo()
    filtro_datas = []

    periodo = [data_inicial + tmd(days=x) for x in 
               range((data_final - data_inicial).days + 1) ]

    # Usar isso pra adicionar numa lista e usar ela como filtro
    for i, dias in enumerate(periodo):
        dias = dias.date().strftime('%d/%m/%Y')
        if i == 0:
            # print(f'{"Datas":^73}')
            # print(f'{i + 1} - {dias}')
            filtro_datas.append(dias)
        elif i > 0:
            # print(f'{i + 1} - {dias}')
            filtro_datas.append(dias)
    return filtro_datas


def visualizacao_periodo():
    dados = abrir_arquivo('r', None)
    data_min = dt.min.date()
    filtro = filtro_periodo()
    bairro = 'Tomba'
    print(f'Bairro: {bairro}')
    i = 1

    #Exibe somente os dados do periodo escolhido
    for datas_csv in dados:
       if datas_csv[0] in filtro and datas_csv[1] == bairro:
           casos_totais_dia = int(datas_csv[3]) + int(datas_csv[4]) + int(datas_csv[5])
           casos_suspeitos = (int(datas_csv[3]) / casos_totais_dia) * 100
           casos_confirmados = (int(datas_csv[5]) / casos_totais_dia) * 100
           print(f'{i} - {datas_csv[0]} - Total de Casos: {casos_totais_dia} - '
                 f'Suspeitos: {casos_suspeitos:.2f}% - '
                 f'Confirmados: {casos_confirmados:.2f}%')
           i += 1


visualizacao_periodo()