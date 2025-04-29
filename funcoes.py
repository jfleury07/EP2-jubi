
import random
def rolar_dados (dados): 
    dados_rolados = []
    for rolagem in range (1,dados+1): 
        dado_rolado = random.randint (1,6)
        dados_rolados.append (dado_rolado)
    return dados_rolados

def guardar_dado (dados_rolados, dados_guardados, indice_dado): 
    lista = [dados_guardados]
    sequencia_desejada = dados_guardados[:]
    sequencia_desejada.append (dados_rolados[indice_dado])
    lista.append (sequencia_desejada)
    return lista    
