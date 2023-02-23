from time import sleep

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.altura = 0


def constroiNo(valor):

    temp = No(valor)

    temp.esq = None
    temp.dir = None

    return temp


def inserirNo(valor, no, quantidade_rotacoes):

    if (no == None):

        return constroiNo(valor), quantidade_rotacoes

    if (valor < no.valor):
        no.esq, quantidade_rotacoes = inserirNo(
            valor, no.esq, quantidade_rotacoes)

    elif (valor > no.valor):
        no.dir, quantidade_rotacoes = inserirNo(
            valor, no.dir, quantidade_rotacoes)
    no, quantidade_rotacoes = balancear(no, quantidade_rotacoes)
    return no, quantidade_rotacoes


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


def maiorEntre(valor1, valor2):
    if(valor1 > valor2):
        return valor1
    elif(valor2 > valor1):
        return valor2
    else:
        return 0


def rotacionaEsq(noA, quantidade_rotacoes):
    quantidade_rotacoes += 1
    noB = noA.dir
    temp = noB.esq
    noA.dir = temp
    noB.esq = noA
    noA.altura = maiorEntre(alturaArvore(noA.esq), alturaArvore(noA.dir)) + 1
    noB.altura = maiorEntre(alturaArvore(noB.esq), alturaArvore(noB.dir)) + 1
    return noB, quantidade_rotacoes


def rotacionaDir(noB, quantidade_rotacoes):
    quantidade_rotacoes += 1
    noA = noB.esq
    temp = noA.dir
    noB.esq = temp
    noA.dir = noB
    noB.altura = maiorEntre(alturaArvore(noB.esq), alturaArvore(noB.dir)) + 1
    noA.altura = maiorEntre(alturaArvore(noA.esq), alturaArvore(noA.dir)) + 1
    return noA, quantidade_rotacoes


def obterBalanceamento(no):
    if (no != None):
        return alturaArvore(no.esq) - alturaArvore(no.dir)
    return 0


def balancear(no, quantidade_rotacoes):
    no.altura = maiorEntre(alturaArvore(no.esq), alturaArvore(no.dir)) + 1

    balanceamento = obterBalanceamento(no)

    if(balanceamento > 1 and obterBalanceamento(no.esq) >= 0):
        return rotacionaDir(no, quantidade_rotacoes)
    if(balanceamento > 1 and obterBalanceamento(no.esq) < 0):

        no.esq, quantidade_rotacoes = rotacionaEsq(no.esq, quantidade_rotacoes)
        return rotacionaDir(no, quantidade_rotacoes)
    if (balanceamento < -1 and obterBalanceamento(no.dir) <= 0):

        return rotacionaEsq(no, quantidade_rotacoes)

    if (balanceamento < -1 and obterBalanceamento(no.dir) > 0):

        no.dir, quantidade_rotacoes = rotacionaDir(no.dir, quantidade_rotacoes)

        return rotacionaEsq(no, quantidade_rotacoes)

    return no, quantidade_rotacoes


def desenharABB(raiz, espaco):

    if (raiz == None):
        return

    espaco += 6

    desenharABB(raiz.dir, espaco)

    print("")
    i = 6
    while(i < espaco):
        print(" ", end="")
        i += 1

    print(f"{raiz.valor}")
    desenharABB(raiz.esq, espaco)
