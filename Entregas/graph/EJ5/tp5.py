
from graph import Graph
from stack import Stack


def crear_grafo():
    grafo = Graph(is_dir=False)

    # Equipos
    grafo.add_vertex("Red Hat", "notebook")
    grafo.add_vertex("Debian", "notebook")
    grafo.add_vertex("Manjaro", "notebook")
    grafo.add_vertex("Fedora", "notebook")
    grafo.add_vertex("Arch", "notebook")
    grafo.add_vertex("Ubuntu", "PC")
    grafo.add_vertex("Mint", "PC")
    grafo.add_vertex("Parrot", "PC")
    grafo.add_vertex("Guarani", "servidor")
    grafo.add_vertex("MongoDB", "servidor")
    grafo.add_vertex("Impresora", "impresora")
    grafo.add_vertex("Router 1", "router")
    grafo.add_vertex("Router 2", "router")
    grafo.add_vertex("Router 3", "router")
    grafo.add_vertex("Switch 1", "switch")
    grafo.add_vertex("Switch 2", "switch")

    # Conexiones
    grafo.add_edge(25, "Red Hat", "Router 2")
    grafo.add_edge(9, "Router 2", "Guarani")
    grafo.add_edge(50, "Router 2", "Router 3")
    grafo.add_edge(37, "Router 2", "Router 1")
    grafo.add_edge(43, "Router 1", "Router 3")
    grafo.add_edge(29, "Router 1", "Switch 1")
    grafo.add_edge(18, "Switch 1", "Ubuntu")
    grafo.add_edge(17, "Switch 1", "Debian")
    grafo.add_edge(22, "Switch 1", "Impresora")
    grafo.add_edge(80, "Switch 1", "Mint")
    grafo.add_edge(61, "Router 3", "Switch 2")
    grafo.add_edge(40, "Switch 2", "Manjaro")
    grafo.add_edge(12, "Switch 2", "Parrot")
    grafo.add_edge(5, "Switch 2", "MongoDB")
    grafo.add_edge(3, "Switch 2", "Fedora")
    grafo.add_edge(6, "Switch 2", "Arch")

    return grafo


# Recorridos en profundidad y amplitud
def recorridos(grafo):
    for equipo in ("Red Hat", "Debian", "Arch"):
        print("\nDFS desde", equipo)
        grafo.deep_show(equipo)

        print("BFS desde", equipo)
        grafo.amplitude_show(equipo)


# Camino más corto utilizando Dijkstra
def camino_mas_corto(grafo, origen, destino):
    print("\n", origen, "->", destino)

    if not grafo.exist_path(origen, destino):
        print("No existe un camino")
        return None

    caminos = grafo.dijkstra(origen)
    camino = Stack()
    actual = destino
    costo = None

    while caminos.size() > 0:
        dato = caminos.pop()

        if dato[0] == actual:
            if costo is None:
                costo = dato[1]

            camino.push(dato[0])
            actual = dato[2]

            if actual is None:
                break

    if costo is None:
        print("No se pudo encontrar el camino")
        return None

    print("Recorrido:", end=" ")

    while camino.size() > 0:
        print(camino.pop(), end=" ")
        if camino.size() > 0:
            print("->", end=" ")

    print("\nCosto:", costo)

    return costo


# Árbol de expansión mínima
def arbol_minimo(grafo):
    print("\nÁrbol de expansión mínima:")

    resultado = grafo.kruskal("Red Hat")
    peso_total = 0

    for conexion in resultado.split(";"):
        origen, destino, peso = conexion.split("-")

        print(origen, "<->", destino, "Peso:", peso)
        peso_total += int(peso)

    print("Peso total:", peso_total)


# Punto e: PC hasta Guarani
def punto_e(grafo):
    print("\nPC con camino más corto hasta Guarani:")

    mejor = None
    menor_costo = None

    for equipo in ("Ubuntu", "Mint", "Parrot"):
        costo = camino_mas_corto(grafo, equipo, "Guarani")

        if costo is not None:
            if menor_costo is None or costo < menor_costo:
                menor_costo = costo
                mejor = equipo

    print("\nPC más cercana:", mejor)
    print("Costo:", menor_costo)


# Punto f: equipos conectados a Switch 1 hasta MongoDB
def punto_f(grafo):
    print("\nCaminos hasta MongoDB desde Switch 1:")

    mejor = None
    menor_costo = None

    for equipo in ("Ubuntu", "Debian", "Mint"):
        costo = camino_mas_corto(grafo, equipo, "MongoDB")

        if costo is not None:
            if menor_costo is None or costo < menor_costo:
                menor_costo = costo
                mejor = equipo

    print("\nEquipo más cercano:", mejor)
    print("Costo:", menor_costo)


# Cambiar conexión de la impresora
def cambiar_impresora(grafo):
    grafo.delete_edge("Switch 1", "Impresora")
    grafo.add_edge(22, "Router 2", "Impresora")


# Programa principal
def main():
    grafo = crear_grafo()

    print("PUNTO B: RECORRIDOS")
    recorridos(grafo)

    print("\nPUNTO C: CAMINOS HASTA IMPRESORA")
    for equipo in ("Manjaro", "Red Hat", "Fedora"):
        camino_mas_corto(grafo, equipo, "Impresora")

    print("\nPUNTO D: ÁRBOL MÍNIMO")
    arbol_minimo(grafo)

    print("\nPUNTO E")
    punto_e(grafo)

    print("\nPUNTO F")
    punto_f(grafo)

    print("\nPUNTO G: NUEVA CONEXIÓN DE IMPRESORA")
    cambiar_impresora(grafo)
    recorridos(grafo)


main()
