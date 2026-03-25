#include <stdio.h>

/*
ANÁLISE:

Sem caso base, a função nunca para, gerando chamadas infinitas.
A pilha cresce até estourar (Stack Overflow).
*/

void erro(int n) {
    printf("%d\n", n);
    erro(n - 1); // sem parada
}

void correto(int n) {
    if (n == 0) return; // caso base
    printf("%d\n", n);
    correto(n - 1);
}

int main() {
    // erro(5); // causa crash
    correto(5);
    return 0;
}