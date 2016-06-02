from persistencia import *
import networkx as nx
import matplotlib.pyplot as plt

class informeSemanticoConversaciones:

    def __init__(self,identificador):

        self.moduloPersistencia = Persistencia()
        self.identificador = identificador

    def crearRed(self):
        mensajes = self.moduloPersistencia.getReplicasSeguimiento(self.identificador)
        nodos = set()
        relaciones = set()
        for k in mensajes:
            nodos.add(k["id_str"])
            nodos.add(k["in_reply_to_status_id"])
            relaciones.add((k["id_str"], k["in_reply_to_status_id"]))
        print(nodos)
        print(relaciones)
        grafo = nx.Graph()
        grafo.add_nodes_from(nodos)
        grafo.add_edges_from(relaciones)
        print(nx.info(grafo))
        nx.draw_random(grafo)
        plt.savefig("red.png")

informe = informeSemanticoConversaciones("#AlgoMásQueDeporte")
informe.crearRed()