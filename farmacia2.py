# ==========================================
# SISTEMA FARMÁCIA - ORIENTADO A OBJETOS
# ==========================================

# Classe base
class Medicamento:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # Método de venda (protegido)
    def vender(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida.")
            return

        if self.__quantidade >= quantidade:
            self.__quantidade -= quantidade
            total = self.calcular_preco(quantidade)
            print(f"Venda realizada: {self.nome} | Total: R$ {total}")
        else:
            print(f"Erro: Estoque insuficiente de {self.nome}")

    # Método que pode ser sobrescrito (polimorfismo)
    def calcular_preco(self, quantidade):
        return self.__preco * quantidade

    def exibir(self):
        print(f"{self.nome} | R$ {self.__preco} | Qtd: {self.__quantidade}")


# Classe filha (normal)
class MedicamentoComum(Medicamento):
    pass


# Classe filha com desconto (polimorfismo)
class MedicamentoGenerico(Medicamento):
    def calcular_preco(self, quantidade):
        preco_original = super().calcular_preco(quantidade)
        desconto = preco_original * 0.2  # 20% desconto
        return preco_original - desconto


# Sistema da farmácia
class Farmacia:
    def __init__(self):
        self.medicamentos = []

    def adicionar(self, medicamento):
        self.medicamentos.append(medicamento)

    def listar(self):
        print("\n=== ESTOQUE ===")
        for m in self.medicamentos:
            m.exibir()
        print("================\n")

    def vender(self, nome, quantidade):
        for m in self.medicamentos:
            if m.nome == nome:
                m.vender(quantidade)
                return
        print("Medicamento não encontrado!")


# MAIN
if __name__ == "__main__":
    farmacia = Farmacia()

    med1 = MedicamentoComum("Paracetamol", 10.0, 50)
    med2 = MedicamentoGenerico("Dipirona Genérico", 8.0, 30)

    farmacia.adicionar(med1)
    farmacia.adicionar(med2)

    farmacia.listar()

    farmacia.vender("Paracetamol", 10)
    farmacia.vender("Dipirona Genérico", 10)

    farmacia.listar()

    # TENTATIVA DE QUEBRAR O SISTEMA
    med1.__quantidade = -999  # não afeta o real

    print("\nSistema protegido! Estado interno intacto:")
    farmacia.listar()