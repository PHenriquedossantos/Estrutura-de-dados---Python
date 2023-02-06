from listas_ligadas.no import No

class ListaLigada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    def imprimir(self):
        no_atual = self.inicio
        while no_atual:
            print(no_atual.valor)
            no_atual = no_atual.proximo