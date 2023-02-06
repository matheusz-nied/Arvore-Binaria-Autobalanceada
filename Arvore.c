struct No {
    int valor;
    struct No* esqFilho;
    struct No* dirFilho;
} typedef No;

No* constroiNo(int valor){
    No* no = malloc(sizeof(No));
    no->valor = valor;

    return no;
}
int main(){
    No* no = constroiNo(10);
    printf("Valor no: %d\n", no->valor);
}