"""
ANÁLISE:

Caso Base: quando encontra o arquivo
Passo Recursivo: percorre subpastas
"""

def buscar(estrutura, alvo):
    if alvo in estrutura:
        return True  # Caso base

    for chave in estrutura:
        if isinstance(estrutura[chave], dict):
            if buscar(estrutura[chave], alvo):  # Recursão
                return True

    return False

dados = {
    "pasta1": {
        "pasta2": {
            "arquivo.txt": None
        }
    }
}

print(buscar(dados, "arquivo.txt"))