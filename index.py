import BinaryTree
import AVLTree
import time
import dados

# MAIN


def ArvoreBinariaExe(exibirEmOrdem = False):
    raiz = None
    quantidadeBusca = 0
    tempo_gasto = 0

    for item in dados.dados_avl_1:
        raiz = BinaryTree.inserirNo(item, raiz)

    for item in dados.dados_avl_2:
        raiz = BinaryTree.inserirNo(item, raiz)
    ini = time.time()

    itemBuscado, quantidadeBusca = BinaryTree.buscar(
        6050, raiz, quantidadeBusca)

    fim = time.time()
    tempo_gasto = fim - ini
    alturaArvoreBinaria = BinaryTree.alturaArvore(raiz)

    if(exibirEmOrdem):        
        BinaryTree.exibirEmOrdem(raiz)
    
    print()
    print()

    print(f"Altura da árvore Binária: {alturaArvoreBinaria}")
    print(
        f"Quantidade de vezes que busca foi chamado na Árvore Binária: {quantidadeBusca}")
    print(f"Tempo gasto na busca da Árvore Binária: {tempo_gasto}")


def ArvoreAVLExe(exibirEmOrdem = False):
    # MAIN
    raiz = None
    quantidadeBusca = 0
    tempo_gasto = 0
    quantidade_rotacoes = 0

    for item in dados.dados_avl_1:
        raiz, quantidade_rotacoes = AVLTree.inserirNo(
            item, raiz, quantidade_rotacoes)

    for item in dados.dados_avl_2:
        raiz, quantidade_rotacoes = AVLTree.inserirNo(
            item, raiz, quantidade_rotacoes)

    ini = time.time()

    itemBuscado, quantidadeBusca = AVLTree.buscar(6050, raiz, quantidadeBusca)

    fim = time.time()
    tempo_gasto = fim - ini
    
    if(exibirEmOrdem):
        AVLTree.exibirEmOrdem(raiz)
        
    print()
    print()

    alturaArvoreAVL = AVLTree.alturaArvore(raiz)
    print(f"Altura da árvore AVL: {alturaArvoreAVL}")
    print(
        f"Quantidade de vezes que busca foi chamada na Árvore AVL: {quantidadeBusca}")
    print(f"Tempo gasto na busca da Árvore AVL: {tempo_gasto}")
    print(f"Quantidade rotações Ávore AVL: {quantidade_rotacoes}")


#Se quiser imprimir em Ordem só passar um argumento True 
#ArvoreBinariaExe(True) ou ArvoreAVLExe(True)

ArvoreBinariaExe(True)
print("\n")
ArvoreAVLExe(True)

