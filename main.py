from vetores import vetor
from listas_ligadas.listas_ligadas import ListaLigada

print(30 * "-", "MENU", 30 * "-")

print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    #vetor_teste.inserir_elemento_final(1)
    #vetor_teste.inserir_elemento_final(2)
    #vetor_teste.inserir_elemento_final(1)
    
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_final(2)
    

    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))
    print(vetor_teste.listar_elemento(2))
    print(vetor_teste.listar_elemento(3))
    print(vetor_teste.tamanho_vetor())
    print(vetor_teste.contem(3))
    print(vetor_teste)
elif menu == 2:
    minha_lista = ListaLigada()
    minha_lista.adicionar(1)
    minha_lista.adicionar(2)
    minha_lista.adicionar(3)
    minha_lista.imprimir()