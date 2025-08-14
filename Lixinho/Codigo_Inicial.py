import csv
from datetime import datetime as dt

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


# Função 'Exibição de Dados'
def dados_info():
    with open('dengue_free_feira2.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=",")
        dados = list(leitor)

        print(f'\n{cor["ma"]}{" DADOS ":=^70}')

        # Exibe todos os dados do arquivo
        for linha in dados:
            print(f'{cor["ci"]}{linha}')


#Função 'Escolha do Bairro'
def bairros_lista():

    # Variaveis
    lista_bairro = []
    bairro = bairro_escolhido = 0

    # Abertura do arquivo em modo de leitura
    with open('dengue_free_feira2.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=",")
        dados = list(leitor)

        # Exibe todos os bairros enumerados
        for i, linha in enumerate(dados):
            if i == 0:
                print(f'\n{cor["ma"]}{linha[1]:=^70}'
                      )  # Falta espaço entre o titulo
            elif i < 26:
                print(f"{cor['ci']}{i} - {linha[1]}")
                lista_bairro.append(linha[1])

        #Escolha do Bairro
        while not bairro_escolhido > 0 and bairro_escolhido < 26:
            bairro_escolhido = int(
                input(f'{cor["bc"]}Informe o numero do Bairro: '))
        bairro = lista_bairro[(bairro_escolhido - 1)]  # Adicionar try/except

        print(f'Bairro Escolhido: {bairro}\n')
        return bairro


# Função 'Atualizar Dados'
def arqv_atualizar():

    # Variaveis
    dados_atualizados = []
    data_att_valido = habitantes_valido = casos_suspeitos_valido = False
    casos_negativos_valido = casos_positivos_valido = False
    casos_suspeitos = casos_negativos = casos_positivos = habitantes = confirmar = ''
    data_atualizacao = dt.min

    print(f'\n{cor["ma"]}{" ATUALIZAÇÃO ":=^70}')

    # Validação da data da atualização
    print(f'{cor["am"]}Atenção: Informe a data no formato "dia/mes/ano"')
    while not data_att_valido:
        try:
            data_atualizacao = str(input(f'{cor["bc"]}Data da Atualização: '))
            data_att = dt.strptime(data_atualizacao, '%d/%m/%Y')
            data_att_valido = True
        except:
            print(
                f'{cor["vm"]}ERRO: Data Invalida! Siga o padrão "dia/mes/ano"')

    # Escolha do bairro da atualização
    bairro_atualizacao = bairros_lista()

    # Validação do n de habitantes e confirmação do n informado
    while not habitantes_valido:
        try:
            habitantes = int(input('Informe o numero de habitantes: '))
            habitantes = str(habitantes)
            confirmar = str(
                input(f'Valor informado {habitantes}. Deseja alterar [S/N]? '))
            if confirmar in 'Ss':
                habitantes_valido = False
            elif confirmar in 'Nn':
                habitantes_valido = True
            else:
                print('Entrada Invalida')
        except:
            print('Entrada Invalida')

    print(f'\n{cor["ma"]}{" Total de Casos ":=^70}{cor["bc"]}')

    # Validação do n de casos positivos e confirmação do n informado
    while not casos_positivos_valido:
        try:
            casos_positivos = int(
                input('Informe o numero de casos positivos: '))
            casos_positivos = str(casos_positivos)
            confirmar = str(
                input(
                    f'Valor informado {casos_positivos}. Deseja alterar [S/N]? '
                ))
            if confirmar in 'Ss':
                casos_positivos_valido = False
            elif confirmar in 'Nn':
                casos_positivos_valido = True
            else:
                print('Entrada Invalida')
        except:
            print('Entrada Invalida')

    # Validação do n de casos negativos e confirmação do n informado
    while not casos_negativos_valido:
        try:
            casos_negativos = int(
                input('Informe o numero de casos positivos: '))
            casos_negativos = str(casos_negativos)
            confirmar = str(
                input(
                    f'Valor informado {casos_negativos}. Deseja alterar [S/N]? '
                ))
            if confirmar in 'Ss':
                casos_negativos_valido = False
            elif confirmar in 'Nn':
                casos_negativos_valido = True
            else:
                print('Entrada Invalida')
        except:
            print('Entrada Invalida')

    # Validação do n de casos suspeitos e confirmação do n informado
    while not casos_suspeitos_valido:
        try:
            casos_suspeitos = int(
                input('Informe o numero de casos positivos: '))
            casos_suspeitos = str(casos_suspeitos)
            confirmar = str(
                input(
                    f'Valor informado {casos_suspeitos}. Deseja alterar [S/N]? '
                ))
            if confirmar in 'Ss':
                casos_suspeitos_valido = False
            elif confirmar in 'Nn':
                casos_suspeitos_valido = True
            else:
                print('Entrada Invalida')
        except:
            print('Entrada Invalida')

    # Lista para adicionar no arquivo csv
    dados_atualizados.append(data_atualizacao)
    dados_atualizados.append(bairro_atualizacao)
    dados_atualizados.append(habitantes)
    dados_atualizados.append(casos_suspeitos)
    dados_atualizados.append(casos_negativos)
    dados_atualizados.append(casos_positivos)

    with open('dengue_free_feira3.csv', 'a', newline='') as arquivo:
        editor = csv.writer(arquivo, delimiter=",")
        editor.writerow(dados_atualizados)


# Função 'Menu Inicial'
def menu():
    menu = ''
    while menu != '3':
        print(f'\n{cor["ma"]}{" TELA INICIAL ":=^70}')
        print(f'{cor["ci"]}'
            '[ 1 ] Visualizar Dados \n[ 2 ] Atualizar Dados \n[ 3 ] Encerrar')

        # Escolha das Opções
        menu = str(input(f'{cor["bc"]}Escolha uma opção: '))
        while menu not in ['1', '2', '3']:
            menu = str(input('Escolha uma opção: '))

        # Opção 1: Visualizar Dados
        if menu == '1':
            dados_info()

        # Opção 2: Atualizar Dados
        elif menu == '2':
            arqv_atualizar()

arqv_atualizar()

