#include <stdio.h>

/*
ANÁLISE ARQUITETURAL:

A versão iterativa possui complexidade O(n), pois percorre os termos apenas uma vez.

Já a versão recursiva ingênua possui complexidade O(2^n), pois recalcula
subproblemas repetidamente.

Cada chamada recursiva cria um novo Stack Frame, aumentando o consumo de memória.
Para n=40, isso gera milhares de chamadas, tornando a execução lenta e custosa.
*/

long long fib_iter(int n) {
    long long a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return (n == 0) ? 0 : b;
}

long long fib_rec(int n) {
    if (n <= 1) return n;
    return fib_rec(n-1) + fib_rec(n-2);
}

int main() {
    int n = 40;

    printf("Iterativo: %lld\n", fib_iter(n));
    printf("Recursivo: %lld\n", fib_rec(n));

    return 0;
}