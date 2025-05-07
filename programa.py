

import random
from funcoes import * 

cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1,
    }
}

simples = ['1', '2', '3', '4', '5', '6']
avancado = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

rodadas = 1
rolagens = 1
inicio_de_rodada = 0
while rodadas <= 12: 
    imprime_cartela(cartela)
    if inicio_de_rodada == 0:
        dados_rolados = rolar_dados(5)
        dados_guardados = []

    while True:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        acao = int(input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))

        while acao not in [0, 1, 2, 3, 4]:
            print('Opção inválida. Tente novamente.')
            acao = int(input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))

        if acao == 1:  # guardar dado
            escolher_pra_guardar = int(input('Digite o índice do dado a ser guardado (0 a 4):\n>'))
            resultado = guardar_dado(dados_rolados, dados_guardados, escolher_pra_guardar)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif acao == 2:  # remover dado guardado
            remover_indice = int(input('Digite o índice do dado a ser removido (0 a 4):\n>'))
            if remover_indice >= len(dados_guardados):
                print("Índice inválido.")
            else:
                resultado = remover_dado(dados_rolados, dados_guardados, remover_indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]

        elif acao == 3:  # rerrolar dados restantes
            if rolagens >= 3:
                print('Você já usou todas as rerrolagens.')
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                print(f'Dados rerrolados: {dados_rolados}')
                rolagens += 1

        elif acao == 4:  # ver cartela
            imprime_cartela(cartela)

        elif acao == 0:  # marcar pontuação
            combinacao_valida = False
            while not combinacao_valida:
                combinacao = input('Digite a combinação desejada:\n>')
                while combinacao not in ['0', '1', '2', '3', '4']:
                    print("Entrada inválida.")
                    combinacao = input('Digite o índice do dado a ser guardado (0 a 4):\n>')
                if combinacao in simples:
                    combinacao = int (combinacao)
                    if cartela['regra_simples'][combinacao] == -1:
                        todos_dados = dados_guardados + dados_rolados
                        faz_jogada(todos_dados, combinacao, cartela)
                        combinacao_valida = True
                    else:
                        print('Essa combinação já foi usada.')
                elif combinacao in avancado:
                    combinacao = str (combinacao)
                    if cartela['regra_avancada'][combinacao] == -1:
                        todos_dados = dados_guardados + dados_rolados
                        faz_jogada(todos_dados, combinacao, cartela)
                        combinacao_valida = True
                    else:
                        print('Essa combinação já foi usada.')
                else:
                    print('Combinação inválida.')
            break

        inicio_de_rodada += 1
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    inicio_de_rodada = 0
    rolagens = 1
    rodadas += 1

# cálculo da pontuação final
soma = 0
for pontos in cartela['regra_simples'].values(): 
    if pontos != -1: 
        soma += pontos
if soma >= 63: 
    soma += 35
for pontos in cartela['regra_avancada'].values(): 
    if pontos != -1: 
        soma += pontos

imprime_cartela(cartela)
print(f'Pontuação total: {soma}')
