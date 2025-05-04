
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


def calcula_pontos_regra_simples (face_dados_rolados):
    dicio= {}
    for numero in range(1, 7):
        pontuaçao = numero * face_dados_rolados.count(numero)
        dicio[numero]= pontuaçao

    return dicio


def calcula_pontos_soma (face_dados_rolados):
    soma=0
    for numeros in face_dados_rolados:
        soma+=numeros

    return soma

def calcula_pontos_sequencia_baixa (lista_face_dados):
    lista_face_dados.sort ()
    i = 0
    while i < len(lista_face_dados) -1: 
        if lista_face_dados[i+1] == lista_face_dados[i]:
            del lista_face_dados [i]
        i += 1
    sequencia = [lista_face_dados[0]]
    i = 0
    while i < len(lista_face_dados) -1: 
        if lista_face_dados[i+1] == sequencia[-1]+1:
            sequencia.append (lista_face_dados[i+1])
        i += 1
    if len(sequencia) in [4, 5, 6]: 
        return 15 
    else: 
        return 0 

print(calcula_pontos_sequencia_baixa([5, 3, 5, 5, 3, 5, 6, 5, 6, 3, 2, 1])) # 0
