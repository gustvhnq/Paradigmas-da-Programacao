"""
ANÁLISE:

Listas são mutáveis e passadas por referência (call-by-sharing).

A função recebe a MESMA estrutura na memória, então alterações
afetam o objeto original.
"""

def aplicar_desconto(estoque):
    for i in range(len(estoque)):
        estoque[i] -= 10

produtos = [100, 200, 300]

aplicar_desconto(produtos)

print(produtos)