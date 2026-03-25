#include <stdio.h>

/*
ANÁLISE ARQUITETURAL:

Na passagem por valor, o parâmetro recebe uma cópia da variável original.
Alterações ocorrem apenas na cópia, sem afetar o valor original.

Na passagem por referência (ponteiro), manipulamos diretamente o endereço
da variável, permitindo alteração real do estado.
*/

void alterar_valor(int saldo) {
    saldo += 1000;
}

void alterar_referencia(int *saldo) {
    *saldo += 1000;
}

int main() {
    int saldo_bancario = 500;

    alterar_valor(saldo_bancario);
    printf("Após valor: %d\n", saldo_bancario);

    alterar_referencia(&saldo_bancario);
    printf("Após referência: %d\n", saldo_bancario);

    return 0;
}