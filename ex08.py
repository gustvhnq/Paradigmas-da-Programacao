"""
ANÁLISE:

Diferente de funções normais, que executam até o fim,
corrotinas pausam e retomam execução mantendo estado.
"""

def linha_montagem():
    etapa = 1
    while True:
        yield f"Processando peça {etapa}"
        etapa += 1

gen = linha_montagem()

print(next(gen))
print(next(gen))
print(next(gen))