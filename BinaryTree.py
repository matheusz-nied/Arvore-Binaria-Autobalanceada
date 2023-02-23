from time import sleep

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
    sleep(0.005)


    quantidadeBusca += 1
    if(no == None):
        return None, quantidadeBusca

    if (valor < no.valor):
        return buscar(valor, no.esq, quantidadeBusca)

    elif (valor > no.valor):
        return buscar(valor, no.dir, quantidadeBusca)

    return no, quantidadeBusca


def alturaArvore(noRaiz):
    if(noRaiz == None):
        return 0
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

