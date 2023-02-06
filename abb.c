#include <stdio.h>
#include <stdlib.h>
#define TAM_ARESTAS 6

struct No {
    int valor;
    struct No* esq;
    struct No* dir;
} typedef No;

No* constroiNo(int valor) {

    No* temp = (No*) malloc(sizeof(No));

    temp->valor = valor;
    temp->esq = NULL;
    temp->dir = NULL;

    return temp;
}

void exibirEmOrdem(No* no) {
    
    if (no->esq != NULL)
        exibirEmOrdem(no->esq);
    
    printf("%d ", no->valor);

    if (no->dir != NULL)
        exibirEmOrdem(no->dir);
}

void exibirPreOrdem(No* no) {
    
    printf("%d ", no->valor);

    if (no->esq != NULL)
        exibirPreOrdem(no->esq);

    if (no->dir != NULL)
        exibirPreOrdem(no->dir);
}

void exibirPosOrdem(No* no) {
    
    if (no->esq != NULL)
        exibirPosOrdem(no->esq);

    if (no->dir != NULL)
        exibirPosOrdem(no->dir);

    printf("%d ", no->valor);
}

No* inserirNo(int valor, No* no) {

    if (no == NULL) 
        return constroiNo(valor);

    if (valor < no->valor )
        no->esq = inserirNo(valor, no->esq);
    else if (valor > no->valor )
        no->dir = inserirNo(valor, no->dir);  

    return no;
}

No* buscar(int valor, No* no) {

    if (no == NULL) 
        return NULL;

    if (valor < no->valor )
        return buscar(valor, no->esq);
    else if (valor > no->valor )
        return buscar(valor, no->dir);  

    return no;
}

No* acharMinimo(No* raiz) {
    No* no = raiz;

    // Busca pela folha mais à esquerda
    while (no && no->esq != NULL)
        no = no->esq;

    return no;
}

No* removerNo(int valor, No* raiz) {

    // Se a árvore está vazia
    if (raiz == NULL)
        return raiz;

    // Procura o nó a ser removido, indo para esquerda ou direita
    if (valor < raiz->valor)
        raiz->esq = removerNo(valor, raiz->esq);
    else if (valor > raiz->valor)
        raiz->dir = removerNo(valor, raiz->dir);

    // Encontrou o nó com este valor
    else {
        // Condição 1 e 2: o nó não tem nenhum filho ou só tem um
        if (raiz->esq == NULL) {

            No* temp = raiz->dir;
            free(raiz);
            return temp;
        } else if (raiz->dir == NULL) {

            No* temp = raiz->esq;
            free(raiz);
            return temp;
        }

        // Condição 3: o nó tem dois filhos
        No *temp = acharMinimo(raiz->dir);

        // Coloca o sucessor "exibirEmOrdem" na posição do nó a ser removido
        raiz->valor = temp->valor;

        // Remove o sucessor "exibirEmOrdem"
        raiz->dir = removerNo(temp->valor, raiz->dir);
    }

    return raiz;
}

void desenharABB(struct No* raiz, int espaco) {

    if (raiz == NULL)
        return;

    espaco += TAM_ARESTAS;
 
    desenharABB(raiz->dir, espaco);
 
    printf("\n");
    for (int i = TAM_ARESTAS; i < espaco; i++)
        printf(" ");

    printf("%d\n", raiz->valor);
 
    desenharABB(raiz->esq, espaco);
}

int main() {
    No* raiz = NULL;
    
    raiz = inserirNo(10, raiz);
    raiz = inserirNo(45, raiz);
    raiz = inserirNo(13, raiz);
    raiz = inserirNo(99, raiz);
    raiz = inserirNo(25, raiz);
    raiz = inserirNo(24, raiz);
    raiz = inserirNo(98, raiz);
    raiz = inserirNo(67, raiz);

    desenharABB(raiz, 0);

    printf("Percurso em profundidade da árvore: \n");

    printf("Em ordem:\n");
    exibirEmOrdem(raiz);
    printf("\n");

    printf("Em ordem:\n");
    exibirEmOrdem(raiz);
    printf("\n");
    printf("Pré-ordem:\n");
    exibirPreOrdem(raiz);
    printf("\n");

    printf("Pós-ordem:\n");
    exibirPosOrdem(raiz);
    printf("\n");

    printf("Removendo nós 10 e 24...\n");
    raiz = removerNo(24, raiz);
    raiz = removerNo(10, raiz);

    printf("Folha mais à esquerda:\n");
    No* min = acharMinimo(raiz);
    printf("%d\n", min->valor); 

    printf("Procurando elemento 13:\n");
    No* treze = buscar(13, raiz);
    if (treze != NULL)
        printf("Achei o %d\n", treze->valor); 
    else
        printf("Não achei o 13\n");
        
    return 0;
}