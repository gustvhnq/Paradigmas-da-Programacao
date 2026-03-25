# ANTES (CAÓTICO)
sal1 = 2000
sal2 = 3000
sal3 = 1500

total1 = sal1 * 1.1
print(total1)

total2 = sal2 * 1.1
print(total2)

total3 = sal3 * 1.1
print(total3)

# DEPOIS (CORRETO)

"""
ANÁLISE ARQUITETURAL:

Separação de responsabilidades:
- Função pura: cálculo
- Procedimento: exibição

Aumenta coesão e reduz acoplamento.
"""

def calcular_salario(salario):
    return salario * 1.1

def imprimir_salario(valor):
    print(f"Salário final: {valor}")

salarios = [2000, 3000, 1500]

for s in salarios:
    resultado = calcular_salario(s)
    imprimir_salario(resultado)