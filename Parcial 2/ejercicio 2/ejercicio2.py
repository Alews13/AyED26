from graph import Graph
from personajes_data import personajes


# Convierte el nombre en una clave sencilla para guardar en el grafo.
# Se quitan espacios y guiones para evitar problemas al buscar los vértices.
def crear_clave(nombre):
    clave = nombre.replace("-", "")
    clave = clave.replace(" ", "")
    return clave


def buscar_personaje_por_clave(grafo, clave):
    posicion = grafo.search(clave, "value")

    if posicion is not None:
        return grafo[posicion].other_values

    return None


def contar_episodios_compartidos(personaje_uno, personaje_dos):
    cantidad = 0

    for episodio in personaje_uno["episodios"]:
        if episodio in personaje_dos["episodios"]:
            cantidad += 1

    return cantidad


# Crea un grafo no dirigido.
# agrega todos los personajes como vértices.
# conecta cada pareja que tenga al menos un episodio en común.
def construir_grafo(lista_personajes):
    grafo = Graph(is_dir=False)

    for personaje in lista_personajes:
        clave = crear_clave(personaje["nombre"])
        grafo.add_vertex(clave, personaje)

    for indice_uno in range(len(lista_personajes)):
        personaje_uno = lista_personajes[indice_uno]

        for indice_dos in range(indice_uno + 1, len(lista_personajes)):
            personaje_dos = lista_personajes[indice_dos]
            peso = contar_episodios_compartidos(personaje_uno, personaje_dos)

            if peso > 0:
                clave_uno = crear_clave(personaje_uno["nombre"])
                clave_dos = crear_clave(personaje_dos["nombre"])
                grafo.add_edge(peso, clave_uno, clave_dos)

    return grafo


def obtener_arbol_minimo(grafo, nombre_inicio):
    clave_inicio = crear_clave(nombre_inicio)
    resultado = grafo.kruskal(clave_inicio)
    aristas_seleccionadas = []

    if not isinstance(resultado, str):
        return aristas_seleccionadas

    partes = resultado.split(";")

    for parte in partes:
        datos_arista = parte.split("-")

        if len(datos_arista) == 3:
            clave_origen = datos_arista[0]
            clave_destino = datos_arista[1]
            peso = int(datos_arista[2])

            personaje_origen = buscar_personaje_por_clave(grafo, clave_origen)
            personaje_destino = buscar_personaje_por_clave(grafo, clave_destino)

            if personaje_origen is not None and personaje_destino is not None:
                aristas_seleccionadas.append(
                    [personaje_origen["nombre"], personaje_destino["nombre"], peso]
                )

    return aristas_seleccionadas


def mostrar_arbol_minimo(grafo):
    referencias = ["C-3PO", "Yoda", "Leia"]
    resultados = []

    for nombre in referencias:
        aristas = obtener_arbol_minimo(grafo, nombre)
        resultados.append(aristas)

    print("Árbol de expansión mínimo:")
    print("Referencias consultadas: C-3PO, Yoda y Leia.")

    if len(resultados[0]) == 0:
        print("No se pudo obtener el árbol de expansión mínimo.")
        return

    for arista in resultados[0]:
        print(arista[0], "<->", arista[1], "- episodios compartidos:", arista[2])

    if resultados[0] == resultados[1] and resultados[1] == resultados[2]:
        print("Las tres referencias producen el mismo árbol.")

    print("Cantidad de conexiones:", len(resultados[0]))


def buscar_pares_con_maximo(grafo):
    maximo = 0
    pares_maximos = []

    for indice_origen in range(len(grafo)):
        vertice_origen = grafo[indice_origen]

        for arista in vertice_origen.edges:
            indice_destino = None

            for indice in range(len(grafo)):
                if grafo[indice].value == arista.destination:
                    indice_destino = indice
                    break

            if indice_destino is not None and indice_origen < indice_destino:
                if arista.weight > maximo:
                    maximo = arista.weight
                    pares_maximos = []

                if arista.weight == maximo:
                    nombre_origen = vertice_origen.other_values["nombre"]
                    personaje_destino = buscar_personaje_por_clave(
                        grafo, arista.destination
                    )
                    pares_maximos.append(
                        [nombre_origen, personaje_destino["nombre"], arista.weight]
                    )

    return maximo, pares_maximos


def obtener_camino_minimo(grafo, nombre_origen, nombre_destino):
    clave_origen = crear_clave(nombre_origen)
    clave_destino = crear_clave(nombre_destino)

    if not grafo.exist_path(clave_origen, clave_destino):
        return [], None

    pila_caminos = grafo.dijkstra(clave_origen)
    caminos = []

    while pila_caminos.size() > 0:
        caminos.append(pila_caminos.pop())

    datos_destino = None

    for camino in caminos:
        if camino[0] == clave_destino:
            datos_destino = camino
            break

    if datos_destino is None:
        return [], None

    costo_total = datos_destino[1]
    camino_invertido = []
    clave_actual = clave_destino

    while clave_actual is not None:
        personaje = buscar_personaje_por_clave(grafo, clave_actual)

        if personaje is None:
            return [], None

        camino_invertido.append(personaje["nombre"])
        datos_actuales = None

        for camino in caminos:
            if camino[0] == clave_actual:
                datos_actuales = camino
                break

        if datos_actuales is None:
            return [], None

        clave_actual = datos_actuales[2]

    camino_invertido.reverse()
    return camino_invertido, costo_total


def mostrar_camino_minimo(grafo, nombre_origen, nombre_destino):
    camino, costo = obtener_camino_minimo(grafo, nombre_origen, nombre_destino)

    print(nombre_origen, "->", nombre_destino)

    if len(camino) == 0:
        print("No existe un camino entre esos personajes.")
    else:
        print("Recorrido:", " -> ".join(camino))
        print("Costo total:", costo)


def personajes_en_nueve_episodios(lista_personajes):
    presentes_en_todos = []

    for personaje in lista_personajes:
        if len(personaje["episodios"]) == 9:
            presentes_en_todos.append(personaje["nombre"])

    return presentes_en_todos


grafo = construir_grafo(personajes)

print("Cantidad de personajes:", len(grafo))
print()
print("--------------------------------------------")

mostrar_arbol_minimo(grafo)

maximo, pares = buscar_pares_con_maximo(grafo)

print("Máximo de episodios compartidos:", maximo)
for par in pares:
    print(par[0], "<->", par[1])
print("--------------------------------------------")


print("Caminos mínimos:")
mostrar_camino_minimo(grafo, "C-3PO", "R2-D2")
mostrar_camino_minimo(grafo, "Yoda", "Darth Vader")
print("--------------------------------------------")


presentes = personajes_en_nueve_episodios(personajes)

print("Personajes presentes en los nueve episodios:")
for nombre in presentes:
    print(nombre)