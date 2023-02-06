import time
import dados


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


def inserirNo(valor, no):

    if (no == None):

        return constroiNo(valor)

    if (valor < no.valor):
        no.esq = inserirNo(valor, no.esq)

    elif (valor > no.valor):
        no.dir = inserirNo(valor, no.dir)
    no =balancear(no)
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
        return noRaiz.altura
        # esq = alturaArvore(noRaiz.esq)
        # dir = alturaArvore(noRaiz.dir)
        # if(esq > dir):
        #     return esq + 1
        # else:
        #     return dir + 1
        


def maiorEntre(valor1, valor2):
    print(valor2)
    if(valor1 > valor2):
        return valor1
    elif(valor2 > valor1):
        return valor2
    else:
        return 0


def rotacionaEsq(noA):
    noB = noA.dir
    temp = noB.esq
    noA.dir = temp
    noB.esq = noA
    noA.altura = maiorEntre(alturaArvore(noA.esq), alturaArvore(noA.dir)) + 1
    noB.altura = maiorEntre(alturaArvore(noB.esq), alturaArvore(noB.dir)) + 1
    return noB


def rotacionaDir(noB):
    noA = noB.esq
    temp = noA.dir
    noB.esq = temp
    noA.dir = noB
    #print(noB)
    #print(maiorEntre(alturaArvore(noB.esq), alturaArvore(noB.dir)))
    noB.altura = maiorEntre(alturaArvore(noB.esq), alturaArvore(noB.dir)) + 1
    noA.altura = maiorEntre(alturaArvore(noA.esq), alturaArvore(noA.dir)) + 1
    return noA


def obterBalanceamento(no):
    if (no != None):
        return alturaArvore(no.esq) - alturaArvore(no.dir)
    return 0


def balancear(no):
    no.altura = maiorEntre(alturaArvore(no.esq), alturaArvore(no.dir)) + 1
  
    balanceamento = obterBalanceamento(no)
    print(f"{no.valor} - {balanceamento}")

    if(balanceamento > 1 and obterBalanceamento(no.esq) >= 0):
        return rotacionaDir(no)
    if(balanceamento > 1 and obterBalanceamento(no.esq) < 0):

        no.esq = rotacionaEsq(no.esq)
        return rotacionaDir(no)
    if (balanceamento < -1 and obterBalanceamento(no.dir) <= 0):

        return rotacionaEsq(no)

    if (balanceamento < -1 and obterBalanceamento(no.dir) > 0):

        print(no.dir)

        no.dir = rotacionaDir(no.dir)
        print("AQUi 4-2")

        return rotacionaEsq(no)

    return no


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

raiz = inserirNo(10, raiz)
raiz = inserirNo(45, raiz)
raiz = inserirNo(46, raiz)
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
#print("Em ordem")
print(exibirEmOrdem(raiz))
# print(alturaArvore(raiz.dir))

#print(item + 1)
desenharABB(raiz,0)