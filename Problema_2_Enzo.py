import csv
from datetime import datetime as dt
from datetime import timedelta as tmd

"""
/*******************************************************************************
Autor: Enzo Cauã da Silva Barbosa
Componente Curricular: Algoritmos I
Concluido em: 02/06/2024
Declaro que este código foi elaborado por mim de forma individual e não contém 
nenhum trecho de código de outro colega ou de outro autor, tais como provindos 
de livros e apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer 
trecho de código de outra autoria que não a minha está destacado com uma citação 
para o autor e a fonte do código, e estou ciente que estes trechos não serão 
considerados para fins de avaliação.
*******************************************************************************/
"""

""" 
 Caro Programador, este codigo foi feito para funcionar com um arquivo .csv que 
 tem como cabeçalho(1ªlinha) os seguintes itens: 
 (Data,Bairros,Habitantes,Casos Suspeitos,Casos Negativos,Casos Confirmados)
 ATENÇÃO!
 > Não faça alterações de ordem, caso contrario os dados serão exibidos de forma   
 incorreta.
 > Ao abrir o arquivo .csv, deixe sempre uma linha vazia no final do arquivo e  
 deixe o cursor nessa mesma linha, caso contrario ao realizar a atualização dos 
 dados, eles serão adicionado onde o cursor estiver, desconfigurando os dados e 
 causando falhas no programa.
"""


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


# Lê um arquivo .csv e retorna uma matriz com os dados encontrados
def ler_dados_arquivo():
    with open('dengue_free_feira.csv', 'r') as arquivo_fonte:
        leitor_arquivo = csv.reader(arquivo_fonte, delimiter=",")
        matriz_dados_do_arquivo = list(leitor_arquivo)
        matriz_dados_do_arquivo = matriz_dados_do_arquivo[1:]

    return matriz_dados_do_arquivo


# Percorre a matriz dos dados do arquivo, cria uma nova matriz de dicionarios e
# retorna uma matriz no formato { Bairro : { Data : [DADOS]} }
def criar_matriz_bairros_por_data():
    matriz_fonte = ler_dados_arquivo()
    matriz_bairros_por_data = {}

    for linha in matriz_fonte:
        chave_bairro = linha[1]

        if chave_bairro not in matriz_bairros_por_data:
            matriz_bairros_por_data[chave_bairro] = {}

        chave_data = linha[0]

        lista_de_casos = [linha[2], linha[3], linha[4], linha[5]]
        matriz_bairros_por_data[chave_bairro][chave_data] = lista_de_casos

    return matriz_bairros_por_data


# Verifica a data mais recente registrada no arquivo
def verificar_ultima_data(matriz_de_dados):
    ultima_data = dt.min.date()

    for chave_bairro in matriz_de_dados.values():
        for data_str in chave_bairro.keys():
            data = dt.strptime(data_str, '%d/%m/%Y').date()
            if data > ultima_data:
                ultima_data = data
    ultima_data = dt.strftime(ultima_data, '%d/%m/%Y')
    return ultima_data


# Solicita ao usuario novos dados a serem adicionados ao arquivo
def informar_novos_dados(data_atual, bairro_escolhido):
    def validar_entrada(informacao_a_ser_exibido):
        entrada_numeros_valida = False
        valor = ''

        while not entrada_numeros_valida:
            try:
                valor = input(
                    f'Informe {informacao_a_ser_exibido}: ')

                if not valor.isdigit():
                    raise ValueError
                entrada_numeros_valida = True

            except ValueError:
                print('Entrada Invalida')
        return valor

    print(f'\n{" REGISTRO DE NOVOS DADOS ":=^40}')

    bairro = bairro_escolhido
    habitantes = validar_entrada('o total de habitante')
    novos_casos_suspeitos = validar_entrada('o total de Casos Suspeitos')
    novos_casos_negativos = validar_entrada('o total de Casos Negativos')
    novos_casos_positivos = validar_entrada('o total de Casos Positivos')

    novos_dados = [data_atual, bairro, habitantes, novos_casos_suspeitos,
                   novos_casos_negativos, novos_casos_positivos]
    return novos_dados


# Recebe uma lista de dados e adiciona ao arquivo .csv
def adicionar_dados_arquivo(novos_dados):
    with open('dengue_free_feira.csv', 'a', newline='') as arquivo_fonte:
        escritor_arquivo = csv.writer(arquivo_fonte, delimiter=",")
        escritor_arquivo.writerow(novos_dados)

    print(f'{cor["vd"]}DADOS ATUALIZADOS COM SUCESSO!')


# Exibe todos os bairros e solicita a escolha de um
def escolher_bairro():
    lista_de_bairros = ['Tomba', 'Campo Limpo', 'Muchila', 'Conceição', 'Caseb',
                        'Mangabeira', 'Calumbi', 'Queimadinha', 'Gabriela', 'Parque Ipê',
                        'Jardim Cruzeiro', 'Rua Nova', 'Lagoa Grande', 'Aviário', 'Santa Mônica',
                        'Centro', 'Pedra de Descanso', 'Brasília', 'São João', 'Cidade Nova',
                        'Jardim Acácia', 'Serraria Brasil', 'Baraúna', 'Cis', 'Ponto Central',
                        'Todos os Bairros']
    i = 0
    escolha_do_usuario = 0
    entrada_valida = False

    for i, bairro in enumerate(lista_de_bairros):
        print(f'{i + 1} - {bairro}')

    while not entrada_valida:
        try:
            escolha_do_usuario = (int(input('Escolha um bairro: ')) - 1)
            if escolha_do_usuario not in range(i + 1):
                raise ValueError
            entrada_valida = True
        except ValueError:
            print('Entrada Invalida')

    if escolha_do_usuario < 25:
        bairro_escolhido = lista_de_bairros[escolha_do_usuario]
    else:
        bairro_escolhido = lista_de_bairros
    return bairro_escolhido


# Valida a entrada do usuario
def validar_escolha_usuario(opcoes):
    escolha = 0
    while escolha not in opcoes:
        try:
            escolha = input(f'{cor["ci"]}Escolha uma opção: ')
            if escolha not in opcoes:
                raise IndexError
        except ValueError:
            print(f'{cor["vm"]}Atenção: Entrada invalida!')
        except IndexError:
            print(f'{cor["vm"]}Atenção: Opção invalida!')
    return escolha


# Verifica se não existem dados para o bairro escolhido na data atual
def verificar_atualizao_valida(data_atual, bairro_escolhido, matriz_de_dados):
    valido = matriz_de_dados[bairro_escolhido].get(data_atual, True)
    if not valido:
        return False
    else:
        return True


def exibir_menu_formato():
    print(f'\n{cor["ma"]}{" Tipo de Dados ":=^43}')
    print(f'{cor["ci"]}'
          'Escolha o tipo de dado a ser exibido:\n\n'
          '[ 1 ] Valores Numericos\n'
          '[ 2 ] Porcentagens\n'
          '[ 3 ] Retornar ao Menu Principal')
    lista_opcoes = ['1', '2', '3']
    escolha_usuario = validar_escolha_usuario(lista_opcoes)

    if escolha_usuario == '1':
        return 'Numero'
    elif escolha_usuario == '2':
        return 'Porcentagem'
    elif escolha_usuario == '3':
        exibir_menu_principal()


# Solicita ao usuario duas datas
def informar_intervalo_de_datas():
    data_inicial_valido = False
    data_final_valido = False
    data_inicial = data_final = dt.min

    print(f'\n{cor["ma"]}{" Intervalo de Datas ":=^43}')
    print(f'{cor["ci"]}Informe a data inicial e a data final '
          f'\nno formato (Dia/Mes/Ano Completo)\n')

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

    while not data_final_valido:
        try:
            data_input = str(input('Data Final: '))
            data_final = dt.strptime(data_input, '%d/%m/%Y')

            if data_inicial <= data_final:
                data_final_valido = True
            elif data_inicial > data_final:
                print('Data final anterior a data inicial!')
        except ValueError as ve:
            if "day is out of range for month" in str(ve):
                print('Data não existente nesse mês!')
            else:
                print('Data Invalida! Siga o padrão "dia/mes/ano"')

    return data_inicial, data_final


# Criar uma lista como todas as datas existentes entre duas datas
def criar_filtro_de_datas():
    data_inicial, data_final = informar_intervalo_de_datas()
    filtro_datas = []

    # Adiciona a lista todas as datas no intervalo definido
    periodo = [data_inicial + tmd(days=x) for x in
               range((data_final - data_inicial).days + 1)]

    # Converter todas as datas do periodo para string e adiciona a lista filtro
    for datas in periodo:
        dias = datas.date().strftime('%d/%m/%Y')
        filtro_datas.append(dias)
    return filtro_datas


# Exibe as opções de periodo para exibição dos dados
def exibir_menu_periodo():
    print(f'\n{cor["ma"]}{" Periodo de Exibição ":=^43}')
    print(f'{cor["ci"]}'
          'Escolha o intervalo de exibição dos dados:\n\n'
          '[ 1 ] Ultima Atualização\n'
          '[ 2 ] Especificar Datas\n'
          '[ 3 ] Todo o periodo registrado\n'
          '[ 4 ] Retornar ao Menu Inicial')
    lista_opcoes = ['1', '2', '3', '4']
    escolha_usuario = validar_escolha_usuario(lista_opcoes)

    if escolha_usuario == '1':
        matriz_de_dados = criar_matriz_bairros_por_data()
        data_da_ultima_atualizacao = verificar_ultima_data(matriz_de_dados)
        return data_da_ultima_atualizacao

    elif escolha_usuario == '2':
        intervalo = criar_filtro_de_datas()
        return intervalo

    elif escolha_usuario == '3':
        return 'Todo o periodo'

    elif escolha_usuario == '4':
        exibir_menu_principal()


# Exibe os dados em forma de numeros
def exibir_dados_numericos(matriz_de_dados, periodo_dos_dados):
    dados_existentes_no_periodo = False

    if periodo_dos_dados == 'Todo o periodo':
        print(f"\n{'_' * 83}")
        print(f"|{'BAIRRO':^17}|{'DATA':^12}|{'HABITANTES':^12}"
              f"|{'SUSPEITOS':^11}|{'NEGATIVOS':^11}|{'CONFIRMADOS':^13}|")
        for chave_bairro, dicionario_data in matriz_de_dados.items():
            for chave_data, valores_data in dicionario_data.items():
                if chave_bairro != 'Nova Data':
                    print(f"|{chave_bairro[:15]:^17}|{chave_data:^12}"
                          f"|{valores_data[0]:^12}|{valores_data[1]:^11}"
                          f"|{valores_data[2]:^11}|{valores_data[3]:^13}|")
        print(f"|{'_' * 17:^17}|{'_' * 12:^12}|{'_' * 12:^12}|{'_' * 11:^11}"
              f"|{'_' * 11:^11}|{'_' * 13:^13}|")

    elif periodo_dos_dados != 'Todo o periodo':
        bairro = escolher_bairro()

        print(f"\n{'_' * 83}")
        print(f"|{'BAIRRO':^17}|{'DATA':^12}|{'HABITANTES':^12}"
              f"|{'SUSPEITOS':^11}|{'NEGATIVOS':^11}|{'CONFIRMADOS':^13}|")

        for chave_bairro, dicionario_data in matriz_de_dados.items():
            if chave_bairro in bairro:
                for chave_data, valores_data in dicionario_data.items():
                    if chave_data in periodo_dos_dados:
                        print(f"|{chave_bairro[:15]:^17}|{chave_data:^12}"
                              f"|{valores_data[0]:^12}|{valores_data[1]:^11}"
                              f"|{valores_data[2]:^11}|{valores_data[3]:^13}|")
                        dados_existentes_no_periodo = True
        if not dados_existentes_no_periodo:
            print(f'|{"SEM DADOS PARA O PERIODO SELECIONADO":^81}|')
            print(f"|{'_' * 81}|")
        else:
            print(f"|{'_' * 17:^17}|{'_' * 12:^12}|{'_' * 12:^12}|{'_' * 11:^11}"
                  f"|{'_' * 11:^11}|{'_' * 13:^13}|")


# Exibe os dados em forma de porcentagem
def exibir_dados_porcentagem(matriz_de_dados, periodo_dos_dados):
    dados_existentes_no_periodo = False

    if periodo_dos_dados != 'Todo o periodo':
        bairro = escolher_bairro()
        print(f"\n{'_' * 83}")
        print(f"|{'BAIRRO':^17}|{'DATA':^12}|{'HABITANTES':^12}"
              f"|{'SUSPEITOS':^11}|{'NEGATIVOS':^11}|{'CONFIRMADOS':^13}|")

        for chave_bairro, dicionario_data in matriz_de_dados.items():
            if chave_bairro in bairro:
                for chave_data, valores_data in dicionario_data.items():
                    if chave_data in periodo_dos_dados:
                        casos_suspeitos = int(valores_data[1])
                        casos_confirmados = int(valores_data[3])
                        total_caso = casos_suspeitos + casos_confirmados
                        percentual_suspeitos = (casos_suspeitos / total_caso) * 100
                        percentual_confirmados = (casos_confirmados / total_caso) * 100
                        print(f"|{chave_bairro[:15]:^17}|{chave_data:^12}"
                              f"|{valores_data[0]:^12}"
                              f"|{f'{percentual_suspeitos:.1f}%':^11}"
                              f"|{valores_data[2]:^11}"
                              f"|{f'{percentual_confirmados:.1f}%':^13}|")
                        dados_existentes_no_periodo = True
        if not dados_existentes_no_periodo:
            print(f'|{"SEM DADOS PARA O PERIODO SELECIONADO":^81}|')
            print(f"|{'_' * 81}|")
        else:
            print(f"|{'_' * 17:^17}|{'_' * 12:^12}|{'_' * 12:^12}|{'_' * 11:^11}"
                  f"|{'_' * 11:^11}|{'_' * 13:^13}|")


# Visualização dos Dados
def visualizar_dados(matriz_de_dados):
    periodo_dos_dados = exibir_menu_periodo()

    if periodo_dos_dados == 'Todo o periodo':
        formato_dos_dados = 'Numero'
    else:
        formato_dos_dados = exibir_menu_formato()

    if formato_dos_dados == 'Numero':
        exibir_dados_numericos(matriz_de_dados, periodo_dos_dados)
    elif formato_dos_dados == 'Porcentagem':
        exibir_dados_porcentagem(matriz_de_dados, periodo_dos_dados)


# Exibe o somatorio total dos dados
def exibir_panorama_geral(matriz_de_dados, data):
    total_habitantes = []
    total_suspeitos = []
    total_negativos = []
    total_positivos = []

    print(f"\n{'_' * 52}")
    print(f'|{"TOTAL DE DADOS REGISTRADOS":^50}|')
    print(f"|{'HABITANTES':^12}|{'SUSPEITOS':^11}|{'NEGATIVOS':^11}"
          f"|{'CONFIRMADOS':^13}|")

    for chave_bairro, dicionario_data in matriz_de_dados.items():
        for chave_data, valores_data in dicionario_data.items():
            if chave_data == data:
                total_habitantes.append(int(valores_data[0]))
                total_suspeitos.append(int(valores_data[1]))
                total_negativos.append(int(valores_data[2]))
                total_positivos.append(int(valores_data[3]))
    total_habitantes = sum(total_habitantes)
    total_suspeitos = sum(total_suspeitos)
    total_negativos = sum(total_negativos)
    total_positivos = sum(total_positivos)

    total_casos = total_suspeitos + total_negativos + total_positivos
    if total_casos > 0:
        percentual_suspeitos = (total_suspeitos / total_casos) * 100
        percentual_negativos = (total_negativos / total_casos) * 100
        percentual_positivos = (total_positivos / total_casos) * 100

        print(f"|{total_habitantes:^12}|{total_suspeitos:^11}|{total_negativos:^11}"
              f"|{total_positivos:^13}|")
        print(f"|{total_habitantes:^12}|{f'{percentual_suspeitos:.1f}%':^11}"
              f"|{f'{percentual_negativos:.1f}%':^11}"
              f"|{f'{percentual_positivos:.1f}%':^13}|")
        print(f"|{'_' * 12:^12}|{'_' * 11:^11}|{'_' * 11:^11}|{'_' * 13:^13}|")
    else:
        print(f'|{"SEM DADOS PARA O PERIODO SELECIONADO":^50}|')
        print(f"|{'_' * 50}|")


# Exibe as opçoes do menu inicial
def exibir_menu_principal():
    encerrar = False

    while not encerrar:
        matriz_de_dados = criar_matriz_bairros_por_data()
        ultima_data = verificar_ultima_data(matriz_de_dados)
        data_atual = ultima_data
        novo_dia = ultima_data
        um_dia = tmd(days=1)

        print(f'\n{cor["ma"]}{" MENU INICIAL ":=^43}')
        print(f'{"Data Atual: "f"{data_atual}":^43}')
        print(f'{cor["ci"]}'
              'Escolha a opção que deseja executar:\n\n'
              '[ 1 ] Panorama Geral\n'
              '[ 2 ] Visualização de Dados\n'
              '[ 3 ] Atualização de Dados\n'
              '[ 4 ] Atualizar Data\n'
              '[ 5 ] Encerrar o Programa')
        lista_opcoes = ['1', '2', '3', '4', '5']
        escolha_usuario = validar_escolha_usuario(lista_opcoes)

        if escolha_usuario == '1':
            exibir_panorama_geral(matriz_de_dados, ultima_data)

        elif escolha_usuario == '2':
            visualizar_dados(matriz_de_dados)

        elif escolha_usuario == '3':
            bairro = escolher_bairro()
            try:
                valido = verificar_atualizao_valida(data_atual, bairro,
                                                    matriz_de_dados)
                if valido is True:
                    novos_dados = informar_novos_dados(data_atual, bairro)
                    adicionar_dados_arquivo(novos_dados)
                else:
                    print(f'Dados existentes para o bairro {bairro} '
                          f'no dia {data_atual}')
            except TypeError:
                print('POR FAVOR INFORME APENAS UM BAIRRO')

        elif escolha_usuario == '4':
            ultima_data = dt.strptime(novo_dia, '%d/%m/%Y')
            novo_dia = ultima_data + um_dia
            nova_data = dt.strftime(novo_dia, '%d/%m/%Y')
            dados_para_nova_data = [nova_data, 'Nova Data', 0, 0, 0, 0]
            adicionar_dados_arquivo(dados_para_nova_data)

        elif escolha_usuario == '5':
            encerrar = True


# Função Principal
def main():
    exibir_menu_principal()

    print(f'\n{cor["ma"]}{"=" * 43}')
    print(f'\n{cor["vd"]}{" PROGRAMA ENCERRADO ":*^43}\n')
    print(f'{cor["ma"]}{"=" * 43}')


main()
