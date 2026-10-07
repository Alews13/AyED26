from list_ import List
from trainers_pokemon import trainers

l = List(trainers)
l.add_criterion("name", lambda x: x["name"])


def buscar_entrenador(lista, nombre):
    index = lista.search(nombre, "name")
    return lista[index] if index is not None else None


# a. obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemones_de_entrenador(lista):
    nombre = input("Ingrese el nombre del entrenador: ")
    entrenador = buscar_entrenador(lista, nombre)
    if entrenador is not None:
        print(f"{nombre} tiene {len(entrenador['pokemons'])} Pokémons.")
    else:
        print("Entrenador no encontrado.")


# b. listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_con_mas_de_tres_torneos(lista):
    print("Entrenadores que ganaron más de tres torneos:")
    for entrenador in lista:
        if entrenador["tournaments_won"] > 3:
            print(entrenador["name"])


# c. Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_entrenador_mas_torneos(lista):
    entrenador = max(lista, key=lambda x: x["tournaments_won"])
    pokemon = max(entrenador["pokemons"], key=lambda x: x["level"])
    print(f"Entrenador con más torneos: {entrenador['name']}")
    print(f"Pokémon de mayor nivel: {pokemon['name']} - nivel {pokemon['level']}")


# d. mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador_y_pokemones(lista):
    nombre = input("Ingrese el nombre del entrenador: ")
    entrenador = buscar_entrenador(lista, nombre)
    if entrenador is None:
        print("Entrenador no encontrado.")
        return

    print(f"Nombre: {entrenador['name']}")
    print(f"Torneos ganados: {entrenador['tournaments_won']}")
    print(f"Batallas ganadas: {entrenador['battles_won']}")
    print(f"Batallas perdidas: {entrenador['battles_lost']}")
    print("Pokémons:")
    for pokemon in entrenador["pokemons"]:
        print(f"  {pokemon['name']} - nivel {pokemon['level']} - tipo {pokemon['type']} - subtipo {pokemon['subtype']}")


# e. mostrar entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def mostrar_entrenadores_mas79(lista):
    print("Entrenadores con porcentaje de batallas ganadas mayor al 79%:")
    for entrenador in lista:
        total = entrenador["battles_won"] + entrenador["battles_lost"]
        porcentaje = entrenador["battles_won"] / total * 100 if total > 0 else 0
        if porcentaje > 79:
            print(f"{entrenador['name']} - {porcentaje:.2f}%")


# f. entrenadores con Pokémons fuego/planta o agua/volador
def entrenadores_por_tipo_subtipo(lista):
    print("Entrenadores con Pokémon Fuego/Planta o Agua/Volador:")
    for entrenador in lista:
        encontrado = False
        for pokemon in entrenador["pokemons"]:
            tipo = pokemon["type"].lower()
            subtipo = pokemon["subtype"].lower()
            if ((tipo == "fuego" and subtipo == "planta") or
                    (tipo == "planta" and subtipo == "fuego") or
                    (tipo == "agua" and subtipo == "volador") or
                    (tipo == "volador" and subtipo == "agua")):
                encontrado = True
        if encontrado:
            print(entrenador["name"])


# g. promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(lista):
    nombre = input("Ingrese el nombre del entrenador: ")
    entrenador = buscar_entrenador(lista, nombre)
    if entrenador is None:
        print("Entrenador no encontrado.")
        return

    pokemons = entrenador["pokemons"]
    if len(pokemons) == 0:
        print("El entrenador no tiene Pokémons.")
        return

    suma = 0
    for pokemon in pokemons:
        suma += pokemon["level"]
    promedio = suma / len(pokemons)
    print(f"Promedio de nivel de los Pokémons de {nombre}: {promedio:.2f}")


# h. determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(lista):
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
    cantidad = 0
    for entrenador in lista:
        for pokemon in entrenador["pokemons"]:
            if pokemon["name"].lower() == nombre_pokemon.lower():
                cantidad += 1
                break
    print(f"Cantidad de entrenadores que tienen a {nombre_pokemon}: {cantidad}")


# i. mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(lista):
    print("Entrenadores con Pokémons repetidos:")
    hay_repetidos = False
    for entrenador in lista:
        nombres = []
        repetido = False
        for pokemon in entrenador["pokemons"]:
            nombre = pokemon["name"].lower()
            if nombre in nombres:
                repetido = True
            else:
                nombres.append(nombre)
        if repetido:
            print(entrenador["name"])
            hay_repetidos = True
    if not hay_repetidos:
        print("No hay entrenadores con Pokémons repetidos.")


# j. entrenadores que tengan Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especiales(lista):
    buscados = ["tyrantrum", "terrakion", "wingull"]
    print("Entrenadores con Tyrantrum, Terrakion o Wingull:")
    for entrenador in lista:
        for pokemon in entrenador["pokemons"]:
            if pokemon["name"].lower() in buscados:
                print(f"{entrenador['name']} - {pokemon['name']}")
                break


# k. determinar si un entrenador X tiene al Pokémon Y y mostrar los datos de ambos
def entrenador_tiene_pokemon(lista):
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
    entrenador = buscar_entrenador(lista, nombre_entrenador)

    if entrenador is None:
        print("Entrenador no encontrado.")
        return

    pokemon_encontrado = None
    for pokemon in entrenador["pokemons"]:
        if pokemon["name"].lower() == nombre_pokemon.lower():
            pokemon_encontrado = pokemon
            break

cantidad_pokemones_de_entrenador(l)

entrenadores_con_mas_de_tres_torneos(l)

pokemon_mayor_nivel_entrenador_mas_torneos(l)

mostrar_datos_entrenador_y_pokemones(l)

mostrar_entrenadores_mas79(l)

entrenadores_por_tipo_subtipo(l)

promedio_nivel_pokemons(l)

cantidad_entrenadores_con_pokemon(l)

entrenadores_con_pokemons_repetidos(l)

entrenadores_con_pokemons_especiales(l)

entrenador_tiene_pokemon(l)