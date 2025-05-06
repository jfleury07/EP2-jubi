
import random
from funcoes import * 

rodadas = 1
rolagens = 0
inicio_de_rodada = 0
while rodadas <= 12: 
    print (imprime_cartela (cartela))
    # if rolagens <= 3: 
        # dados_rolados = rolar_dados (5)
    dados_rolados = [2, 2, 3, 5, 6]
    if inicio_de_rodada == 0: 
        dados_guardados = []
    else: 
        dados_guardados = guardar_dado(dados_rolados, dados_guardados, esolher_pra_guardar)[1]
    print (f'Dados rolados: {dados_rolados}')
    print (f'Dados guardados: {dados_guardados}')
    while True: 
        acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))
        while acao not in [0, 1, 2, 3, 4]: 
            print ('Opção inválida. Tente novamente.')
            acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:\n>'))
        if acao == 1:    # guardar um dado (índice de 0 a 4)
            # dados_rolados = rolar_dados (5)
            esolher_pra_guardar = int(input('Digite o índice do dado a ser guardado (0 a 4):\n>'))
            dados_pra_guardar = guardar_dado (dados_rolados, dados_guardados, esolher_pra_guardar)
            if inicio_de_rodada != 0: 
                dados_pra_guardar[1].append (dados_guardados)
            print (f'Dados rolados: {dados_rolados}') # ou dados_pra_guardar[0]
            print (f'Dados guardados: {dados_pra_guardar[1]}')
        if acao == 2:    # remover um dado da lista de guardados
            dado_remover = int(input('Digite o índice do dado a ser removido (0 a 4):\n>'))
            guardar_dado (dados_rolados, cartela, dado_remover)
        if acao == 3:    # rerrolar os dados não guardados
            rerrolar = str(input('Quer rerrolar? '))
            rolagens += 1
            if rolagens >= 3: 
                print ('Você já usou todas as rerrolagens.')
                print (f'Dados rolados: {dados_rolados}')
                print (f'Dados guardados: {dados_guardados}')
        if acao == 4:    # ver a cartela (imprime_cartela).
            print (imprime_cartela(cartela))
        if acao == 0: 
            combinacao = int(input('Digite a combinação desejada:\n>'))
            print (f'Dados rolados: {dados_rolados}')
            print (f'Dados guardados: {dados_guardados}')
            break
        inicio_de_rodada += 1
        # A combinação pode ser uma str ou int 
    inicio_de_rodada = 0
    rodadas += 1

print (imprime_cartela(cartela))


# Enquanto a acao for diferente de 0 
# Só conta uma rodada (acaba uma rodada) quando ele digitar 0

# ADICIONAR EM ALGUM LUGAR: 
    # if rolagens == 3: 
    #     print ('Você já usou todas as rerrolagens.')
    #     print (f'Dados rolados: {dados_rolados}')

    # while acao not in [0, 1, 2, 3, 4]: 
    #     print ('Opção inválida. Tente novamente.')
    #     acao = int (input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:'))


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