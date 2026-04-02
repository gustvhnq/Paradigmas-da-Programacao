# ==========================================
# SISTEMA FARMÁCIA - PARADIGMA PROCEDURAL
# ==========================================

# Banco de dados simples (global)
estoque = []

# Função para cadastrar medicamento
def cadastrar_medicamento(nome, preco, quantidade):
    medicamento = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    estoque.append(medicamento)
    print(f"Medicamento '{nome}' cadastrado com sucesso!")

# Função para vender medicamento
def vender_medicamento(nome, quantidade):
    for med in estoque:
        if med["nome"] == nome:
            if med["quantidade"] >= quantidade:
                med["quantidade"] -= quantidade
                total = med["preco"] * quantidade
                print(f"Venda realizada! Total: R$ {total}")
            else:
                print("Erro: Estoque insuficiente!")
            return
    print("Erro: Medicamento não encontrado!")

# Função para exibir estoque
def listar_estoque():
    print("\n=== ESTOQUE ===")
    for med in estoque:
        print(f"{med['nome']} | R$ {med['preco']} | Qtd: {med['quantidade']}")
    print("================\n")


# MAIN
if __name__ == "__main__":
    cadastrar_medicamento("Paracetamol", 10.0, 50)
    cadastrar_medicamento("Dipirona", 8.0, 30)

    listar_estoque()

    vender_medicamento("Paracetamol", 10)
    vender_medicamento("Dipirona", 40)  # erro

    # PROBLEMA DO PROCEDURAL
    estoque[0]["quantidade"] = -999  # quebra o sistema

    listar_estoque()