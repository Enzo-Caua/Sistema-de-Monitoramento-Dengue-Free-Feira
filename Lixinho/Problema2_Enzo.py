# Dengue Free Feira - MI Algoritimos - Problema 2

import csv
import sys
from datetime import datetime as dt
from datetime import timedelta as tmd

""" Adicionar Mensagem caso não tenha nenhum dado para o periodo """
""" A exibição ta toda errada, tem q ser a diferença entre as datas """


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
    '__': '\033[4m'
}


# Exceções
class NumeroNegativo(Exception):
    pass


# Abrir o arquivo
def abrir_arquivo(modo, lista_dados_atualizados):
    arquivo_valido = False

    while not arquivo_valido:
        try:
            # Abrir em Modo de Leitura
            if modo == 'r':
                with open('dengue_free_feira2.csv','r') as arquivo:
                    leitor = csv.reader(arquivo, delimiter=",")
                    lista_dados = list(leitor)
                    arquivo_valido = True
                    return lista_dados

            # Abrir em Modo de Atualização
            elif modo == 'a':
                with open('dengue_free_feira2.csv','a',newline='') as arquivo:
                    editor = csv.writer(arquivo, delimiter=",")
                    editor.writerow(lista_dados_atualizados)
                    print(f'{cor["vd"]} Dados Atualizados com Sucesso!')
                    arquivo_valido = True
        except FileNotFoundError:
            print(f'{cor["vm"]} ERRO: Arquivo Não Encontrado!')
            print(' Encerrando o programa! Revise o arquivo base!')
            sys.exit()
        """Colocar Condição para encerrar ou criar novo arquivo"""


# Permite o usuario escolher uma das opções
def escolha_usuario(opcoes):
    escolha = 0

    while escolha not in opcoes:
        try:
            escolha = int(input(f'{cor["ci"]}Escolha uma opção: '))
            if escolha not in opcoes:
                raise IndexError
        except ValueError:
            print(f'{cor["vm"]}Atenção: Entrada invalida!')
        except IndexError:
            print(f'{cor["vm"]}Atenção: Opção invalida!')
    return escolha


# Função 'Exibir e Escolher Bairro'
def bairros_lista():
    lista_bairros = []
    bairro_escolhido = 0
    bairro_valido = False
    dados = abrir_arquivo('r', None)


    # Exibe todos os bairros enumerados
    for i, linha in enumerate(dados):
        if i == 0:
                print(f'\n{cor["ma"]}{f" {linha[1]} ":=^43}')
        elif i < 26:
            print(f"{cor['ci']}{i} - {linha[1]}")
            lista_bairros.append(linha[1])
        else:
            print(f"{cor['ci']}{'0'} - {'Todos os Bairros'}")
            break

    # Escolha do Bairro
    """ Adicionar a possibilidade de mais bairros """
    while not 0 < bairro_escolhido < 26 and not bairro_valido:
        try:
            bairro_escolhido = int(input(f'\n{cor["ci"]}'
                                         'Informe o numero do Bairro: '))
            if bairro_escolhido < 0:
                raise NumeroNegativo(print(f'{cor["vm"]}ERRO: '
                                           'Digite apenas numeros positivos!'))
            if bairro_escolhido == 0:
                bairro = 'Todos os Bairros'
            else:
                bairro = lista_bairros[(bairro_escolhido - 1)]
            print(f'Bairro Escolhido: {bairro}\n')
            bairro_valido = True
        except IndexError:
            print('Bairro Não Existente!')
        except ValueError:
            print('Entrada Invalida! Digite Novamente!')
        except NumeroNegativo:
            print(NumeroNegativo)
    return bairro

# Verifica a data da ultima atualização
def data_ultima_atualizacao():
    dados = abrir_arquivo('r', [])
    ultima_data = dt.min.date()
    # Considera a menor data da bilioteca datetime (01/01/0001)

    for linha in dados:
        if linha[0] != 'Data':
            data = dt.strptime(linha[0], '%d/%m/%Y').date()
            # .strptime() converte uma string para um variavel do tipo date
            if data > ultima_data:
                ultima_data = data
    # Retorna a ultima data como uma string no formato ('dia/mes/ano')
    return ultima_data.strftime('%d/%m/%Y')


# Visualização de dados da ultima atualização
def dados_ultima_atualizacao(tipo_dado):
    dados = abrir_arquivo('r', [])
    ultima_atualizacao = data_ultima_atualizacao()

    #Exibe os dados numericos ultima atualizaçao
    if tipo_dado == 'Numero':
        print(f'\n{cor["ma"]}{" Dados por Bairro ":=^68}')
        print(f"{cor['az']}{cor['__']}{'*'*68}")
        print(f'|{f"Ultima Atualização: {ultima_atualizacao}":^66}|')
        print(f"|{'Bairro':^15}|{'Habitantes':^12}|{'Suspeitos':^11}|"
              f"{'Confirmados':^13}|{'Negativos':^11}|")
        for linha in dados:
            if linha[0] == ultima_atualizacao:
                coluna_bairro = linha[1]
                coluna_habitantes = linha[2]
                coluna_suspeitos = linha[3]
                coluna_negativos = linha[4]
                coluna_positivos = linha[5]
                print(f'|{coluna_bairro[0:13]:^15}|{coluna_habitantes:^12}|'
                      f'{coluna_suspeitos:^11}|{coluna_positivos:^13}|'
                      f'{coluna_negativos:^11}|')
        print(f"\033[0;34m{'*'*68}{cor['base']}")

    # Exibe as porcentagens da ultima atualização
    elif tipo_dado == 'Porcentagem':
        print(f'\n{cor["ma"]}{" Dados por Bairro ":=^78}')
        print(f"{cor['az']}{cor['__']}{'*'*78}")
        print(f'|{f"Ultima Atualização: {ultima_atualizacao}":^76}|')
        print(f"|{'Bairro':^15}|{'Habitantes':^12}|{'Total':^9}|"
              f"{'Suspeitos':^11}|{'Confirmados':^13}|{'Negativos':^11}|")
        for linha in dados:
            if linha[0] == ultima_atualizacao:
                coluna_bairro = linha[1]
                coluna_habitantes = linha[2]
                coluna_suspeitos = int(linha[3])
                coluna_negativos = int(linha[4])
                coluna_positivos = int(linha[5])
                total_casos = (coluna_suspeitos + coluna_negativos +
                               coluna_positivos)
                porcento_suspeitos = str(
                    f'{(coluna_suspeitos / total_casos) * 100:.1f}%')
                porcento_negativos = str(
                    f'{(coluna_negativos / total_casos) * 100:.1f}%')
                porcento_positivos = str(
                    f'{(coluna_positivos / total_casos) * 100:.1f}%')
                print(f'|{coluna_bairro[0:13]:^15}|'
                      f'{coluna_habitantes:^12}|'
                      f'{total_casos:^9}|'
                      f'{porcento_suspeitos:^11}|'
                      f'{porcento_positivos:^13}|'
                      f'{porcento_negativos:^11}|')
        print(f"\033[0;34m{'*'*78}{cor['base']}")


# Função Periodo dos Dados
def intervalo_datas():

    # Variaveis
    data_inicial_valido = False
    data_final_valido = False
    data_inicial = data_final = dt.min

    print(f'\n{cor["ma"]}{" Intervalo de Datas ":=^43}')
    print(f'{cor["ci"]}Informe a data inicial e a data final '
          f'\nno formato (Dia/Mes/Ano Completo)\n')

    # Validação da data inicial
    while not data_inicial_valido:
        try:
            data_input = str(input('Data Inicial: '))
            data_inicial = dt.strptime(data_input, '%d/%m/%Y')
            data_inicial_valido = True
        except ValueError as ve:
            if "day is out of range for month" in str(ve):
                print('Data inexistente para esse mês!')
            else:
                print('Data Invalida! Siga o padrão "dia/mes/ano"')

    # Validação da data final
    while not data_final_valido:
        try:
            data_input = str(input('Data Final: '))
            data_final = dt.strptime(data_input, '%d/%m/%Y')

            # Verificação se a data final não é anterior a data inicial
            if data_inicial < data_final:
                data_final_valido = True
            elif data_inicial > data_final:
                print('Data final anterior a data inicial!')
        except ValueError as ve:
            if "day is out of range for month" in str(ve):
                print('Data não existente nesse mês!')
            else:
                print('Data Invalida! Siga o padrão "dia/mes/ano"')
    return data_inicial, data_final


# Filtro de Datas
def filtro_datas():

    data_inicial, data_final = intervalo_datas()
    filtro_datas = []

    # Adiciona a lista todas as datas no intervalo definido
    periodo = [data_inicial + tmd(days=x) for x in 
               range((data_final - data_inicial).days + 1) ]

    # Usar isso pra adicionar numa lista e usar ela como filtro
    for datas in periodo:
        dias = datas.date().strftime('%d/%m/%Y')
        filtro_datas.append(dias)
    return filtro_datas


# Visualização de dados do periodo especificado
def dados_periodo_datas(tipo_dado, filtro_datas, bairro):
    dados = abrir_arquivo('r', [])
    periodo = filtro_datas
    quant_datas = len(periodo) - 1
    bairro_escolhido = bairro

    if bairro_escolhido == 'Todos os Bairros':

        # Exibe os dados numericos de todos os bairro no periodo
        if tipo_dado == 'Numero':
            print(f'\n{cor["ma"]}{" Dados por Bairro ":=^81}')
            print(f"{cor['az']}{cor['__']}{'*'*81}")
            print(f'|{f"Periodo: {periodo[0]} a {periodo[quant_datas]}":^79}|')
            print(f"|{'Data':^12}|{'Bairro':^15}|{'Habitantes':^12}|"
                f"{'Suspeitos':^11}|{'Confirmados':^13}|{'Negativos':^11}|")
            for linha in dados:
                if linha[0] in periodo:
                    coluna_data = linha[0]
                    coluna_bairro = linha[1]
                    coluna_habitantes = linha[2]
                    coluna_suspeitos = linha[3]
                    coluna_negativos = linha[4]
                    coluna_positivos = linha[5]
                    print(f'|{coluna_data:^12}|{coluna_bairro[0:13]:^15}|'
                        f'{coluna_habitantes:^12}|{coluna_suspeitos:^11}|'
                        f'{coluna_positivos:^13}|{coluna_negativos:^11}|')
            print(f"\033[0;34m{'*'*81}{cor['base']}")

        # Exibe os dados numericos do periodo
        elif tipo_dado == 'Porcentagem':
            print(f'\n{cor["ma"]}{bairro_escolhido:=^91}')
            print(f"{cor['az']}{cor['__']}{'*'*91}")
            print(f'|{f"Periodo: {periodo[0]} a {periodo[quant_datas]}":^89}|')
            print(f"|{'Data':^12}|{'Bairro':^15}|{'Habitantes':^12}|"
                f"{'Total':^9}|{'Suspeitos':^11}|{'Confirmados':^13}|"
                f"{'Negativos':^11}|")
            for linha in dados:
                if linha[0] in periodo:
                    coluna_data = linha[0]
                    coluna_bairro = linha[1]
                    coluna_habitantes = linha[2]
                    coluna_suspeitos = int(linha[3])
                    coluna_negativos = int(linha[4])
                    coluna_positivos = int(linha[5])
                    total_casos = (coluna_suspeitos + coluna_negativos +
                                coluna_positivos)
                    porcento_suspeitos = str(
                        f'{(coluna_suspeitos / total_casos) * 100:.1f}%')
                    porcento_negativos = str(
                        f'{(coluna_negativos / total_casos) * 100:.1f}%')
                    porcento_positivos = str(
                        f'{(coluna_positivos / total_casos) * 100:.1f}%')
                    print(f'|{coluna_data:^12}|'
                        f'{coluna_bairro[0:13]:^15}|'
                        f'{coluna_habitantes:^12}|'
                        f'{total_casos:^9}|'
                        f'{porcento_suspeitos:^11}|'
                        f'{porcento_positivos:^13}|'
                        f'{porcento_negativos:^11}|')
            print(f"\033[0;34m{'*'*91}{cor['base']}")

    else: 
        # Exibe os dados numericos do bairro selecionado no periodo
        if tipo_dado == 'Numero':
            print(f'\n{cor["ma"]}{f" {bairro_escolhido} ":=^65}')
            print(f"{cor['az']}{cor['__']}{'*'*65}")
            print(f'|{f"Periodo: {periodo[0]} a {periodo[quant_datas]}":^63}|')
            print(f"|{'Data':^12}|{'Habitantes':^12}|{'Suspeitos':^11}|"
                f"{'Confirmados':^13}|{'Negativos':^11}|")
            for linha in dados:
                if linha[0] in periodo and linha[1] == bairro_escolhido:
                    coluna_data = linha[0]
                    coluna_bairro = linha[1]
                    coluna_habitantes = linha[2]
                    coluna_suspeitos = linha[3]
                    coluna_negativos = linha[4]
                    coluna_positivos = linha[5]
                    print(f'|{coluna_data:^12}|{coluna_habitantes:^12}|'
                        f'{coluna_suspeitos:^11}|{coluna_positivos:^13}|'
                        f'{coluna_negativos:^11}|')
            print(f"\033[0;34m{'*'*65}{cor['base']}")

        # Exibe os dados numericos do periodo
        elif tipo_dado == 'Porcentagem':
            print(f'\n{cor["ma"]}{f" {bairro_escolhido} ":=^75}')
            print(f"{cor['az']}{cor['__']}{'*'*75}")
            print(f'|{f"Periodo: {periodo[0]} a {periodo[quant_datas]}":^73}|')
            print(f"|{'Data':^12}|{'Habitantes':^12}|{'Total':^9}|"
                f"{'Suspeitos':^11}|{'Confirmados':^13}|{'Negativos':^11}|")
            for linha in dados:
                if linha[0] in periodo and linha[1] == bairro_escolhido:
                    coluna_data = linha[0]
                    coluna_bairro = linha[1]
                    coluna_habitantes = linha[2]
                    coluna_suspeitos = int(linha[3])
                    coluna_negativos = int(linha[4])
                    coluna_positivos = int(linha[5])
                    total_casos = (coluna_suspeitos + coluna_negativos +
                                coluna_positivos)
                    porcento_suspeitos = str(
                        f'{(coluna_suspeitos / total_casos) * 100:.1f}%')
                    porcento_negativos = str(
                        f'{(coluna_negativos / total_casos) * 100:.1f}%')
                    porcento_positivos = str(
                        f'{(coluna_positivos / total_casos) * 100:.1f}%')
                    print(f'|{coluna_data:^12}|{coluna_habitantes:^12}|'
                        f'{total_casos:^9}|{porcento_suspeitos:^11}|'
                        f'{porcento_positivos:^13}|{porcento_negativos:^11}|')
            print(f"\033[0;34m{'*'*75}{cor['base']}")


# Função 'Menu de Tipo de Dados
def menu_tipo_dados():
    print(f'\n{cor["ma"]}{" Tipo de Dados ":=^43}')
    print(f'{cor["ci"]}'
          'Escolha o tipo de dado a ser exibido:\n\n'
          '[ 1 ] Valores Numericos\n'
          '[ 2 ] Porcentagens\n'
          '[ 3 ] Retornar ao Menu Anterior')
    lista_opcoes = (1, 2, 3)
    escolha = escolha_usuario(lista_opcoes)

    # Ação de cada opção
    if escolha == 1:
        return 'Numero'
    elif escolha == 2:
        return 'Porcentagem'
    elif escolha == 3:
        print(f'\n{cor["ma"]}{"="*43}')
        print(f'\n{cor["vd"]}{"RETORNANDO AO MENU INICIAL...":^43}')
        return


# Função 'Menu de Periodo'
def menu_periodo():
    print(f'\n{cor["ma"]}{" Periodo de Exibição ":=^43}')
    print(f'{cor["ci"]}'
          'Escolha o intervalo de exibição dos dados:\n\n'
          '[ 1 ] Ultima Atualização\n'
          '[ 2 ] Especificar Datas\n'
          '[ 3 ] Retornar ao Menu Inicial')
    lista_opcoes = (1, 2, 3)
    escolha = escolha_usuario(lista_opcoes)

    # Ação de cada opção
    if escolha == 1:
        tipo_dado = menu_tipo_dados()
        dados_ultima_atualizacao(tipo_dado)

    elif escolha == 2:
        filtro = filtro_datas()
        tipo_dado = menu_tipo_dados()
        bairro_escolhido = bairros_lista()
        dados_periodo_datas(tipo_dado,filtro,bairro_escolhido)

    elif escolha == 3:
        print(f'\n{cor["ma"]}{"="*43}')
        print(f'\n{cor["vd"]}{"RETORNANDO AO MENU INICIAL...":^43}')
        return


# Função 'Menu Inicial'
def menu_inicial():
    encerrar = False

    while not encerrar:
        print(f'\n{cor["ma"]}{" MENU INICIAL ":=^43}')
        print(f'{cor["ci"]}'
              'Escolha a opção que deseja executar:\n\n'
              '[ 1 ] Visualização de Dados\n'
              '[ 2 ] Atualização de Dados\n'
              '[ 3 ] Encerrar o programa')
        lista_opcoes = (1, 2, 3)
        opcao = escolha_usuario(lista_opcoes)

        # Visualizar Dados
        if opcao == 1:
            menu_periodo()

        # Atualizar Dados
        elif opcao == 2:
            print('Atualizar Dados')
            # Deixar por ultimo, muita info

        # Encerrar o Programa
        elif opcao == 3:
            print(f'\n{cor["ma"]}{"="*43}')
            print(f'\n{cor["vd"]}{" PROGRAMA ENCERRADO ":*^43}\n')
            print(f'{cor["ma"]}{"="*43}')
            encerrar = True


menu_inicial()
