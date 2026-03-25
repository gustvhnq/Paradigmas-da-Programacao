#include <stdio.h>

/*
ANÁLISE:

Função: não altera estado (segura)
Procedimento: altera via ponteiro (efeito colateral)
*/

float calcular_altitude(float atual, float variacao) {
    return atual + variacao;
}

void forcar_altitude(float *altitude, float nova) {
    *altitude = nova;
}

int main() {
    float altitude = 1000;

    float nova = calcular_altitude(altitude, 200);
    printf("Calculada: %.2f\n", nova);

    forcar_altitude(&altitude, 5000);
    printf("Forçada: %.2f\n", altitude);

    return 0;
}