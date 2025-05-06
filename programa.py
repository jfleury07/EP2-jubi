
import random
from funcoes import * 

cartela = {
    "regra_simples": {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    "regra_avancada": {
        "trinca": -1,
        "quadra": -1,
        "full": -1,
        "seq_peq": -1,
        "seq_grd": -1,
        "yahtzee": -1,
        "chance": -1
    }
}

rodadas = 1
rolagens = 1
inicio_de_rodada = 0
while rodadas <= 12: 
    imprime_cartela (cartela)
    if inicio_de_rodada == 0: 
        dados_rolados = rolar_dados (5)
        dados_guardados = []
    while True: 
        print (f'Dados rolados: {dados_rolados}')
        print (f'Dados guardados: {dados_guardados}')
        acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))
        while acao not in [0, 1, 2, 3, 4]: 
            print ('Opção inválida. Tente novamente.')
            acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))
        if acao == 1:    # guardar um dado (índice de 0 a 4)
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
            rolagens += 1
            if rolagens >= 3: 
                print ('Você já usou todas as rerrolagens.')
        if acao == 4:    # ver a cartela (imprime_cartela).
            imprime_cartela(cartela)
        if acao == 0: 
            combinacao = int(input('Digite a combinação desejada:\n>'))
            jogada = faz_jogada (dados_guardados, combinacao, cartela)
            break
        inicio_de_rodada += 1
        # A combinação pode ser uma str ou int 
    inicio_de_rodada = 0
    rodadas += 1

imprime_cartela(cartela)
