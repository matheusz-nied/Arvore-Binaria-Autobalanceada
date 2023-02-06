import time
import dados


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


def constroiNo(valor):

    temp = No(valor)

    temp.esq = None
    temp.dir = None

    return temp


def inserirNo(valor, no):

    if (no == None):
        return constroiNo(valor)

    if (valor < no.valor):
        no.esq = inserirNo(valor, no.esq)

    elif (valor > no.valor):
        no.dir = inserirNo(valor, no.dir)

    return no


def exibirEmOrdem(no):

    if (no.esq != None):
        exibirEmOrdem(no.esq)

    if (no.valor != None):
        print(f"{(no.valor)} - ", end="")

    if (no.dir != None):
        exibirEmOrdem(no.dir)


def buscar(valor, no, quantidadeBusca):

    quantidadeBusca += 1
    if(no == None):
        return None

    if (valor < no.valor):
        return buscar(valor, no.esq, quantidadeBusca)

    elif (valor > no.valor):
        return buscar(valor, no.dir, quantidadeBusca)

    return no, quantidadeBusca


def alturaArvore(noRaiz):
    if(noRaiz == None):
        return -1
    else:
        esq = alturaArvore(noRaiz.esq)
        dir = alturaArvore(noRaiz.dir)
        if(esq > dir):
            return esq + 1
        else:
            return dir + 1


def desenharABB(raiz, espaco):

    if (raiz == None):
        return

    espaco += 6
 
    desenharABB(raiz.dir, espaco)
 
    print("")
    i = 6
    while(i < espaco):
        print(" ", end="")
        i+=1


    print(f"{raiz.valor}") 
    desenharABB(raiz.esq, espaco)

# MAIN
raiz = None
quantidadeBusca = 0
tempo_gasto = 0

#print(dados.dados_avl_1)
raiz = inserirNo(10, raiz)
raiz = inserirNo(45, raiz)
raiz = inserirNo(13, raiz)
raiz = inserirNo(99, raiz)
raiz = inserirNo(25, raiz)
raiz = inserirNo(24, raiz)
raiz = inserirNo(98, raiz)
raiz = inserirNo(67, raiz)
raiz = inserirNo(68, raiz)
raiz = inserirNo(7, raiz)

# ini = time.time()

# item,quantidadeBusca  = buscar(67, raiz, quantidadeBusca)

# fim = time.time()
# tempo_gasto = fim - ini

# print(f"Quantidade de vezes que busca foi chamado: {quantidadeBusca}")
# print(f"Tempo gasto na busca: {tempo_gasto}")
#print(exibirEmOrdem(raiz))
#print(alturaArvore(raiz))
desenharABB(raiz, 0)