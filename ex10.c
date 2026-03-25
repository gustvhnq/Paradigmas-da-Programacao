#include <stdio.h>

/*
ANÁLISE ARQUITETURAL:

À medida que o sistema cresce, o uso de structs gigantes e múltiplos ponteiros
torna o código difícil de manter.

Funções passam a depender de grandes blocos de estado compartilhado,
aumentando o acoplamento e o risco de corrupção de dados.

Esse cenário evidencia a limitação do paradigma procedural,
motivando o uso de encapsulamento na orientação a objetos.
*/

typedef struct {
    int pacientes;
    int medicos;
    int leitos;
    float caixa;
} SistemaHospitalar;

void realizar_internacao(SistemaHospitalar *s) {
    if (s->leitos > 0) {
        s->pacientes++;
        s->leitos--;
        s->caixa += 500.0;
    }
}

int main() {
    SistemaHospitalar hospital = {10, 5, 3, 1000.0};

    realizar_internacao(&hospital);

    printf("Pacientes: %d\n", hospital.pacientes);
    printf("Leitos: %d\n", hospital.leitos);
    printf("Caixa: %.2f\n", hospital.caixa);

    return 0;
}