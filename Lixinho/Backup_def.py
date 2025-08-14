import csv
from datetime import datetime as dt

#Função para escolha do Bairro
def lista_bairro():
    lt_bairro = []
    bairro = e_bairro = 0

    with open('dengue_free_feira.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=",")
        dados = list(leitor)
        
        # Exibe todos os bairros enumerados
        for i, linha in enumerate(dados):
            if i == 0:
                print(f'{linha[1]:^70}')
            elif i < 26:
                print(i, '-', linha[1])
                lt_bairro.append(linha[1])
        
        #Escolha do Bairro
        while not e_bairro > 0 and e_bairro < 26:
            e_bairro = int(input('Informe o numero do Bairro: '))
        bairro = lt_bairro[(e_bairro - 1)]
        print(f'Bairro Escolhido: {bairro}')
        return bairro
    

# Função para escolha do periodo dos dados
def periodo():

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
        except:
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
        except:
            print('Data Invalida! Siga o padrão "dia/mes/ano"')
    return data_inicial, data_final

# Função para atualizar o arquivo
def arqv_atualizar():
    # Variaveis
    dados_atualizados = []
    data_att_valido = habitantes_valido = casos_suspeitos_valido = casos_negativos_valido = casos_positivos_valido = False
    casos_suspeitos = casos_negativos = casos_positivos = habitantes = confirmar = ''

    # Validação da data da atualização
    while not data_att_valido:
        try:
            data_atualizacao = str(input('Data da Atualização: '))
            data_att = dt.strptime(data_atualizacao, '%d/%m/%Y')
            data_att_valido = True
        except:
            print('Data Invalida! Siga o padrão "dia/mes/ano"')

    # Escolha do bairro da atualização (chama a funcao lista_bairro)
    bairro_atualizacao = lista_bairro()

    # Validação do n de habitantes e confirmação do n informado
    while not habitantes_valido:
        try:    
            habitantes = int(input('Informe o numero de habitantes: '))
            habitantes = str(habitantes)
            while confirmar not in 'SsFf':
                confirmar = str(f'Valor informado {habitantes}! Deseja continuar [S/N]? ')
            habitantes_valido = True
        except:
            print('Entrada Invalida')

    # Validação do n de casos positivos e confirmação do n informado
    while not casos_positivos_valido:
        try:    
            casos_positivos = int(input('Informe o total de casos positivos: '))
            casos_positivos = str(casos_positivos)
            while confirmar not in 'SsFf':
                confirmar = str(f'Valor informado {casos_positivos}! Deseja continuar [S/N]? ')
            casos_positivos_valido = True
        except:
            print('Entrada Invalida')

    # Validação do n de casos negativos e confirmação do n informado
    while not casos_negativos_valido:
        try:    
            casos_negativos = int(input('Informe o total de casos negativos: '))
            casos_negativos = str(casos_negativos)
            while confirmar not in 'SsFf':
                confirmar = str(f'Valor informado {casos_negativos}! Deseja continuar [S/N]? ')
            casos_negativos_valido = True
        except:
            print('Entrada Invalida')

    # Validação do n de casos suspeitos e confirmação do n informado
    while not casos_suspeitos_valido:
        try:    
            casos_suspeitos = int(input('Informe o total de casos suspeitos: '))
            casos_suspeitos = str(casos_suspeitos)
            while confirmar not in 'SsFf':
                confirmar = str(f'Valor informado {casos_suspeitos}! Deseja continuar [S/N]? ')
            casos_suspeitos_valido = True
        except:
            print('Entrada Invalida')


    # Lista para adicionar no arquivo csv
    dados_atualizados.append(data_atualizacao)
    dados_atualizados.append(bairro_atualizacao)
    dados_atualizados.append(habitantes)
    dados_atualizados.append(casos_suspeitos)
    dados_atualizados.append(casos_negativos)
    dados_atualizados.append(casos_positivos)

    with open('dengue_free_feira2.csv', 'a', newline='') as arquivo:
        editor = csv.writer(arquivo, delimiter=",")
        editor.writerow(dados_atualizados)