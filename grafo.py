import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def mostrarGrafo():

    pilotos_bruto = pd.read_csv('drivers.csv')

    # Gerando grafo
    brasileiros = pilotos_bruto.query("nationality == 'Brazilian'")
    sobrenomes = list(brasileiros['surname'])
    grafo = nx.Graph()
    for sobrenome in sobrenomes:
        grafo.add_node(sobrenome)
    for sobrenome in sobrenomes:
        grafo.add_edge('Time Brasil', sobrenome)

    pos = nx.spring_layout(grafo, seed=1)
    nx.draw(grafo, with_labels = True)
    plt.savefig("grafo.png")

    im = Image.open(r"grafo.png") 
    im.show()