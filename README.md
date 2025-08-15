Este produto foi desenvolvido como avaliação da disciplina MI Algoritmos I – EXA854.

O produto solicitado foi um código para registro, atualização e visualização de dados sobre casos de dengue em diferentes bairros de Feira de Santana, a partir de um arquivo CSV previamente formatado.
O código permite ao usuário interagir por meio de menus para:
- Visualizar um panorama geral dos casos em uma data específica.
- Visualizar dados detalhados por bairro, podendo escolher entre formato numérico ou em porcentagem.
- Filtrar dados por última atualização, intervalo de datas ou todo o período registrado.
- Atualizar registros de casos para um bairro específico na data atual, com validação para evitar duplicidade de informações.
- Avançar a data de referência para novas atualizações.

O sistema trabalha com um arquivo dengue_free_feira.csv contendo obrigatoriamente o cabeçalho:

Data,Bairros,Habitantes,Casos Suspeitos,Casos Negativos,Casos Confirmados

> ⚠ Atenção ao uso do arquivo CSV:
> 
> Não alterar a ordem das colunas, para evitar que os dados sejam exibidos de forma incorreta.
Manter uma linha vazia no final do arquivo e posicionar o cursor nessa linha ao abrir no editor, evitando que novas inserções desconfigurem o arquivo.
Durante a execução, o usuário poderá selecionar o bairro (ou todos) para consulta e informar novos valores de forma validada, garantindo que apenas números inteiros sejam aceitos.
Ao final da execução, o programa exibirá os dados de forma tabulada, permitindo identificar a situação de cada bairro ou o cenário geral da cidade, com cálculos automáticos de totais e percentuais.

Todas as entradas do usuário possuem validação, prevenindo falhas de execução por erros de digitação.
