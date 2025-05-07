
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
        entrada = input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>')
        while entrada not in ['0', '1', '2', '3', '4']:
            print('Opção inválida. Tente novamente.')
            entrada = input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>')
        acao = int(entrada)

        if acao == 1:
            entrada = input('Digite o índice do dado a ser guardado (0 a 4):\n>')
            while entrada not in ['0', '1', '2', '3', '4']:
                print('Índice inválido.')
                entrada = input('Digite o índice do dado a ser guardado (0 a 4):\n>')
            escolher_pra_guardar = int(entrada)
            if escolher_pra_guardar < len(dados_rolados):
                resultado = guardar_dado(dados_rolados, dados_guardados, escolher_pra_guardar)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]

        elif acao == 2:
            entrada = input('Digite o índice do dado a ser removido (0 a 4):\n>')
            while entrada not in ['0', '1', '2', '3', '4']:
                print('Índice inválido.')
                entrada = input('Digite o índice do dado a ser removido (0 a 4):\n>')
            remover_indice = int(entrada)
            if remover_indice < len(dados_guardados):
                resultado = remover_dado(dados_rolados, dados_guardados, remover_indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]

        elif acao == 3:
            if rolagens >= 3:
                print('Você já usou todas as rerrolagens.')
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                print(f'Dados rerrolados: {dados_rolados}')
                rolagens += 1

        elif acao == 4:
            imprime_cartela(cartela)

        elif acao == 0:
            combinacao_valida = False
            while not combinacao_valida:
                combinacao = input('Digite a combinação desejada:\n>')
                if combinacao in simples:
                    combinacao = int(combinacao)
                    if cartela['regra_simples'][combinacao] == -1:
                        todos_dados = dados_guardados + dados_rolados
                        faz_jogada(todos_dados, combinacao, cartela)
                        combinacao_valida = True
                    else:
                        print('Essa combinação já foi usada.')
                elif combinacao in avancado:
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
