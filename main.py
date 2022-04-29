import os
from grafo import mostrarGrafo
from ordenacao import mostrarTabela

def mostrarMenu():
    while True:
        prompt = "\nBem vindo ao visualizador de pilotos brasileiros de Fórmula 1!\n\n\
1) Ver tabela\n\
2) Ver grafo\n\
3) Sair\n\n\
Escolha uma entre as opções acima: "

        os.system('clear')
        escolha = input(prompt)
        os.system('clear')

        if(escolha == '1'):
            print("Lista de pilotos brasileiros ordenados por sobrenome:\n\n")
            mostrarTabela()
            input("\nPressione Enter para continuar...")
        elif(escolha == '2'):
            mostrarGrafo()
        elif(escolha == '3'):
            os.system('clear')
            exit()

if __name__ == "__main__":
    mostrarMenu()