from graph import Graph
from stack import Stack


def crear_grafo():
    grafo = Graph(is_dir=False)

    grafo.add_vertex("Cocina")
    grafo.add_vertex("Comedor")
    grafo.add_vertex("Cochera")
    grafo.add_vertex("Quincho")
    grafo.add_vertex("Baño 1")
    grafo.add_vertex("Baño 2")
    grafo.add_vertex("Habitación 1")
    grafo.add_vertex("Habitación 2")
    grafo.add_vertex("Sala de estar")
    grafo.add_vertex("Patio")

    grafo.add_edge(5, "Cocina", "Comedor")
    grafo.add_edge(4, "Cocina", "Baño 1")
    grafo.add_edge(8, "Cocina", "Patio")
    grafo.add_edge(5, "Comedor", "Sala de estar")
    grafo.add_edge(9, "Comedor", "Quincho")
    grafo.add_edge(7, "Comedor", "Habitación 1")
    grafo.add_edge(6, "Sala de estar", "Habitación 1")
    grafo.add_edge(8, "Sala de estar", "Habitación 2")
    grafo.add_edge(4, "Sala de estar", "Patio")
    grafo.add_edge(6, "Habitación 1", "Habitación 2")
    grafo.add_edge(3, "Habitación 1", "Baño 1")
    grafo.add_edge(10, "Habitación 1", "Cochera")
    grafo.add_edge(4, "Habitación 2", "Baño 2")
    grafo.add_edge(7, "Habitación 2", "Patio")
    grafo.add_edge(7, "Baño 1", "Baño 2")
    grafo.add_edge(8, "Baño 1", "Cochera")
    grafo.add_edge(6, "Baño 2", "Quincho")
    grafo.add_edge(8, "Quincho", "Patio")
    grafo.add_edge(7, "Quincho", "Cochera")
    grafo.add_edge(9, "Cochera", "Patio")

    return grafo


def arbol_minimo(grafo):
    resultado = grafo.kruskal("Cocina")
    peso_total = 0

    print("Árbol de expansión mínima:")
    for conexion in resultado.split(";"):
        origen, destino, peso = conexion.split("-")
        peso = int(peso)
        print(origen, "<->", destino, "- peso:", peso, "m")
        peso_total += peso

    print("Total de cable:", peso_total, "m")
    print()


def camino_mas_corto(grafo):
    caminos = grafo.dijkstra("Habitación 1")
    destino = "Sala de estar"
    camino = Stack()
    costo_total = None

    while caminos.size() > 0:
        dato = caminos.pop()
        if dato[0] == destino:
            if costo_total is None:
                costo_total = dato[1]
            camino.push(dato[0])
            destino = dato[2]
            if destino is None:
                break

    print("Camino más corto desde Habitación 1 hasta Sala de estar:")
    print("Router -> Smart TV")
    print("Recorrido:", end=" ")
    while camino.size() > 0:
        print(camino.pop(), end="")
        if camino.size() > 0:
            print(" -> ", end="")
    print()
    print("Cable necesario:", costo_total, "m")


def main():
    grafo = crear_grafo()
    arbol_minimo(grafo)
    camino_mas_corto(grafo)


if __name__ == "__main__":
    main()
