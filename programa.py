
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
    imprime_cartela (cartela)
    while True: 
        if inicio_de_rodada == 0: 
            dados_rolados = rolar_dados (5)
            dados_guardados = []
        print (f'Dados rolados: {dados_rolados}')
        print (f'Dados guardados: {dados_guardados}')
        acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))
        while acao not in [0, 1, 2, 3, 4]: 
            print ('Opção inválida. Tente novamente.')
            acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))
        if acao == 1:    # guardar um dado 
            escolher_pra_guardar = int(input('Digite o índice do dado a ser guardado (0 a 4):\n>'))
            dados = guardar_dado (dados_rolados, dados_guardados, escolher_pra_guardar)
            dados_rolados = dados[0]
            dados_guardados = dados[1]
        if acao == 2:    # remover um dado da lista de guardados
            dado_remover = int(input('Digite o índice do dado a ser removido (0 a 4):\n>'))
            dados = remover_dado (dados_rolados, dados_guardados, dado_remover)
            dados_rolados = dados[0]
            dados_guardados = dados[1]
        if acao == 3:    # rerrolar os dados não guardados
            dados_rerolados = rolar_dados (len(dados_rolados))
            dados_rolados = dados_rerolados
            inicio_de_rodada += 1
            rolagens += 1
            if rolagens > 3: 
                print ('Você já usou todas as rerrolagens.')
        if acao == 4:    # ver a cartela 
            imprime_cartela(cartela)
        if acao == 0: 
            combinacao = (input('Digite a combinação desejada:\n>'))
            if combinacao in avancado:
                combinacao = str(combinacao)
            elif combinacao in simples:
                combinacao = int(combinacao)
            todos_dados = dados_guardados + dados_rolados
            jogada = faz_jogada(todos_dados, combinacao, cartela)
            break
        inicio_de_rodada += 1
    inicio_de_rodada = 0
    rolagens = 1
    rodadas += 1

soma = 0
for pontos in cartela:['regra_simples'].values(): 
    if pontos != -1: 
        soma += pontos
    if soma >= 63: 
        soma += 35

soma = 0
for pontos in cartela['regra_avancada'].values (): 
    if pontos != -1: 
        soma += pontos

imprime_cartela(cartela)

print (f'Pontuação total: {soma}')
