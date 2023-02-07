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
    
    def tamanho(self):
        no_atual = self.inicio
        #print(no_atual)
        contador = 0
        while no_atual:
            contador +=1
            no_atual = no_atual.proximo
        return contador

    def buscar(self, valor):
        retorno = 0
        no_atual = self.inicio
        while no_atual:
            if no_atual.valor == valor:
                retorno = no_atual.valor
                return retorno
            no_atual = no_atual.proximo
        return None

    def remover(self, valor):
        no_anterior = None
        no_atual = self.inicio
        while no_atual:
            if no_atual.valor == valor:
                if no_anterior is None:
                    self.inicio = no_atual.proximo
                else:
                    no_anterior.proximo = no_atual.proximo
                return True
            no_anterior = no_atual
            no_atual = no_atual.proximo
        return False