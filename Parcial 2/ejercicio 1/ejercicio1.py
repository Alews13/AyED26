from tree import BinaryTree
from pokemon_data import pokemones


# Cantidad de Pokémon que se cargan para probar.
CANTIDAD_CARGA = 7

NUMEROS_PARA_PRUEBA = [135, 745, 697, 1, 94, 6, 208]


def seleccionar_pokemones(lista, cantidad):
    # Selecciona algunos Pokémon para las pruebas.
    # Si se pide una cantidad mayor, toma los primeros registros de la lista.
    seleccion = []

    if cantidad <= 7:
        for pokemon in lista:
            if pokemon["numero"] in NUMEROS_PARA_PRUEBA:
                seleccion.append(pokemon)
                if len(seleccion) == cantidad:
                    break
    else:
        for pokemon in lista:
            if len(seleccion) == cantidad:
                break
            seleccion.append(pokemon)

    return seleccion


def construir_arboles(lista):
    arbol_nombre = BinaryTree()
    arbol_numero = BinaryTree()
    arbol_tipo = BinaryTree()

    for pokemon in lista:
        arbol_nombre.insert_node(pokemon["nombre"].lower(), pokemon)
        arbol_numero.insert_node(pokemon["numero"], pokemon)

        for tipo in pokemon["tipos"]:
            tipo = tipo.lower()
            nodo = arbol_tipo.search(tipo)

            if nodo is None:
                arbol_tipo.insert_node(tipo, [pokemon])
            else:
                nodo.other_values.append(pokemon)

    return arbol_nombre, arbol_numero, arbol_tipo


def buscar_por_numero(arbol_numero, numero):
    nodo = arbol_numero.search(numero)

    if nodo is not None:
        return nodo.other_values

    return None


def buscar_por_nombre(arbol_nombre, nombre):
    nodo = arbol_nombre.search(nombre.lower())

    if nodo is not None:
        return nodo.other_values

    return None


def buscar_por_tipo(arbol_tipo, tipo):
    nodo = arbol_tipo.search(tipo.lower())

    if nodo is not None:
        return nodo.other_values

    return []


def mostrar_pokemon(pokemon):
    print("Nombre:", pokemon["nombre"])
    print("Número:", pokemon["numero"])
    print("Tipos:", ", ".join(pokemon["tipos"]))
    print("Debilidades:", ", ".join(pokemon["debilidades"]))
    print("Megaevolución:", pokemon["mega_evolucion"])
    print("Gigamax:", pokemon["gigamax"])


def mostrar_por_numero(arbol_numero, numero):
    pokemon = buscar_por_numero(arbol_numero, numero)

    if pokemon is None:
        print("No se encontró un Pokémon con ese número.")
    else:
        mostrar_pokemon(pokemon)


def mostrar_por_nombre(arbol_nombre, nombre):
    pokemon = buscar_por_nombre(arbol_nombre, nombre)

    if pokemon is None:
        print("No se encontró ese Pokémon.")
    else:
        mostrar_pokemon(pokemon)


def mostrar_por_proximidad(arbol_nombre, texto):
    # Recorre el árbol y muestra los Pokémon cuyo nombre contiene el texto.
    # Se hace este recorrido porque proxy_search() solamente imprime las claves.
    texto = texto.lower()

    def recorrer(nodo):
        if nodo is not None:
            recorrer(nodo.left)

            if texto in nodo.value:
                mostrar_pokemon(nodo.other_values)
                print()

            recorrer(nodo.right)

    recorrer(arbol_nombre.root)


def mostrar_por_tipo(arbol_tipo, tipos):
    for tipo in tipos:
        print("Pokémon de tipo", tipo, ":")

        resultados = buscar_por_tipo(arbol_tipo, tipo)

        if len(resultados) == 0:
            print("No hay Pokémon de ese tipo entre los cargados.")
        else:
            for pokemon in resultados:
                print(pokemon["nombre"])

        print()


def mostrar_en_orden(nodo):
    # Realiza un recorrido inorden: izquierda, nodo actual y derecha.
    # Como el árbol está ordenado, los registros salen en orden ascendente por su clave.
    if nodo is not None:
        mostrar_en_orden(nodo.left)
        pokemon = nodo.other_values
        print(pokemon["numero"], "-", pokemon["nombre"])
        mostrar_en_orden(nodo.right)


def mostrar_listados(arbol_nombre, arbol_numero):
    print("Pokémon ordenados por número:")
    mostrar_en_orden(arbol_numero.root)

    print("\nPokémon ordenados por nombre:")
    mostrar_en_orden(arbol_nombre.root)

    print("\nPokémon por niveles del árbol de nombre:")
    arbol_nombre.by_level()


def buscar_en_lista(lista, nombre):
    for pokemon in lista:
        if pokemon["nombre"].lower() == nombre.lower():
            return pokemon

    return None


def mostrar_debiles(arbol_numero, lista_original, nombres=None):
    if nombres is None:
        nombres = ["Jolteon", "Lycanroc", "Tyrantrum"]

    for nombre in nombres:
        pokemon_objetivo = buscar_en_lista(lista_original, nombre)

        print("Pokémon débiles frente a", nombre, ":")

        if pokemon_objetivo is None:
            print("No se encontró el Pokémon de referencia.")
        else:
            tipos = pokemon_objetivo["tipos"]
            encontrados = []

            def recorrer(nodo):
                if nodo is not None:
                    recorrer(nodo.left)

                    pokemon = nodo.other_values
                    es_debil = False

                    for tipo in tipos:
                        if tipo in pokemon["debilidades"]:
                            es_debil = True

                    if es_debil:
                        encontrados.append(pokemon)

                    recorrer(nodo.right)

            recorrer(arbol_numero.root)

            if len(encontrados) == 0:
                print("No hay resultados entre los Pokémon cargados.")
            else:
                for pokemon in encontrados:
                    print(pokemon["nombre"])

        print()


def mostrar_estadisticas(arbol_tipo, arbol_numero):
    print("Cantidad de Pokémon por tipo:")

    def recorrer_tipos(nodo):
        if nodo is not None:
            recorrer_tipos(nodo.left)
            print(nodo.value, ":", len(nodo.other_values))
            recorrer_tipos(nodo.right)

    recorrer_tipos(arbol_tipo.root)

    def contar_formas(nodo):
        # Cuenta recursivamente las megaevoluciones y formas Gigamax del árbol.
        cantidad_mega = 0
        cantidad_gigamax = 0

        if nodo is not None:
            mega_izquierda, giga_izquierda = contar_formas(nodo.left)
            mega_derecha, giga_derecha = contar_formas(nodo.right)

            pokemon = nodo.other_values
            cantidad_mega = mega_izquierda + mega_derecha
            cantidad_gigamax = giga_izquierda + giga_derecha

            if pokemon["mega_evolucion"]:
                cantidad_mega += 1

            if pokemon["gigamax"]:
                cantidad_gigamax += 1

        return cantidad_mega, cantidad_gigamax

    cantidad_mega, cantidad_gigamax = contar_formas(arbol_numero.root)

    print("\nPokémon con megaevolución:", cantidad_mega)
    print("Pokémon con forma Gigamax:", cantidad_gigamax)


# Programa principal: selecciona los registros, construye los árboles y ejecuta las pruebas.
lista_cargada = seleccionar_pokemones(pokemones, CANTIDAD_CARGA)

arbol_nombre, arbol_numero, arbol_tipo = construir_arboles(lista_cargada)

print("Cantidad de Pokémon cargados:", len(lista_cargada))
print("--------------------------------------------")


# Busquedas: se encuentran hardcoeadas pero se pueden descomentar las líneas para ingresar los datos por teclado (comentando las hardcodeadas).

print("Búsqueda por número:")
mostrar_por_numero(arbol_numero, 6)

# numero_ingresado = int(input("Ingrese el número de Pokédex que desea buscar: "))
# mostrar_por_numero(arbol_numero, numero_ingresado)
print("--------------------------------------------")


print("Búsqueda por nombre:")
mostrar_por_nombre(arbol_nombre, "Gengar")

# nombre_ingresado = input("Ingrese el nombre del Pokémon que desea buscar: ")
# mostrar_por_nombre(arbol_nombre, nombre_ingresado)
print("--------------------------------------------")


print("Búsqueda por proximidad:")
mostrar_por_proximidad(arbol_nombre, "bul")

# texto_ingresado = input("Ingrese el texto para buscar por proximidad: ")
# mostrar_por_proximidad(arbol_nombre, texto_ingresado)
print("--------------------------------------------")


print("Búsqueda por tipo:")
mostrar_por_tipo(arbol_tipo, ["Fantasma", "Fuego", "Acero", "Eléctrico"])

# tipo_ingresado = input("Ingrese el tipo que desea buscar: ")
# mostrar_por_tipo(arbol_tipo, [tipo_ingresado])
print("--------------------------------------------")


print("Listados:")
mostrar_listados(arbol_nombre, arbol_numero)
print("--------------------------------------------")


print("Búsqueda por debilidades:")
mostrar_debiles(arbol_numero, pokemones)

# nombre_referencia = input("Ingrese Jolteon, Lycanroc o Tyrantrum para buscar por debilidades: ")
# mostrar_debiles(arbol_numero, pokemones, [nombre_referencia])
print("--------------------------------------------")


print("Estadísticas:")
mostrar_estadisticas(arbol_tipo, arbol_numero)


