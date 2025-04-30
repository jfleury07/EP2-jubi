
import random
def rolar_dados (dados): 
    dados_rolados = []
    for rolagem in range (1,dados+1): 
        dado_rolado = random.randint (1,6)
        dados_rolados.append (dado_rolado)
    return dados_rolados

def guardar_dado (dados_rolados, dados_guardados, indice_dado): 
    sequencia_desejada = dados_guardados[:]
    sequencia_desejada.append (dados_rolados[indice_dado])
    del dados_rolados[indice_dado]
    lista = [dados_rolados]
    lista.append (sequencia_desejada)
    return lista    

def remover_dado (dados_rolados, dados_guardados, indice_dado): 
    dados_rolados.append (dados_guardados[indice_dado])
    del dados_guardados [indice_dado]
    lista = [dados_rolados, dados_guardados]
    return lista

dados_rolados =[2, 2, 2, 2]
dados_no_estoque = [1]
dado_para_remover = 0

print (remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))
# tem que ser [[2, 2, 2, 2, 1], []]