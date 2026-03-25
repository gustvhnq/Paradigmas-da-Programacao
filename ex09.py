"""
ANÁLISE:

Geração sob demanda evita carregar tudo na memória.
Ideal para streams infinitos.
"""

def gerar_logs():
    i = 1
    while True:
        yield f"Log {i}"
        i += 1

logs = gerar_logs()

for _ in range(5):
    print(next(logs))