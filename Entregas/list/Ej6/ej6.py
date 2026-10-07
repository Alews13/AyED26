# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:
#a. eliminar el nodo que contiene la información de Linterna Verde


from super_heroes import superheroes
from list_ import List
from copy import deepcopy

l = List(superheroes)

def eliminar_linterna_verde(l):
    l_aux = deepcopy(l)
    l_aux.show()
    l_aux.add_criterion('alias', lambda x: x['alias'])
    l_aux.delete_value("Linterna Verde", "alias")
    l_aux.show()

print("-" * 30)
eliminar_linterna_verde(l)

# b. mostrar el año de aparición de Wolverine

def mostrar_ano_aparicion_wolverine(l):
    l.add_criterion("alias", lambda x: x["alias"])
    index = l.search("Wolverine", "alias")
    if index is not None:
        print(f"Año de aparición de Wolverine: {l[index]['first_appearance']}")

print("-" * 30)
mostrar_ano_aparicion_wolverine(l)

# c. cambiar la casa de Dr. Strange a Marvel

def cambiar_casa_dr_strange(l):
    l.add_criterion("alias", lambda x: x["alias"])
    index = l.search("Doctor Strane", "alias")
    if index is not None:
        l[index]["house"] = "Marvel"
        print(f"Casa de Doctor Strange cambiada a: {l[index]['house']}")

print("-" * 30)
cambiar_casa_dr_strange(l)

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#“traje” o “armadura”

def mostrar_superheroes_con_traje_o_armadura(l):
    print("Superhéroes que mencionan 'traje' o 'armadura' en su biografía:")
    l.filter_contain_on_bio(["traje", "armadura"])

print("-" * 30)
mostrar_superheroes_con_traje_o_armadura(l)

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963

def mostrar_superheroes_anteriores_1963(l):
    print("Superhéroes cuya fecha de aparición es anterior a 1963:")
    for element in l:
        if element["first_appearance"] < 1963:
            print(f"Nombre: {element['name']}, Casa: {element['house']}")

print("-" * 30)
mostrar_superheroes_anteriores_1963(l)

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

def mostrar_casa_capitana_y_mujer_maravilla(l):
    l.add_criterion("alias", lambda x: x["alias"])
    capitana_index = l.search("Captain Marvel", "alias")
    mujer_maravilla_index = l.search("Wonder Woman", "alias")
    if capitana_index is not None:
        print(f"Casa de Capitana Marvel: {l[capitana_index]['house']}")
    if mujer_maravilla_index is not None:
        print(f"Casa de Mujer Maravilla: {l[mujer_maravilla_index]['house']}")

print("-" * 30)
mostrar_casa_capitana_y_mujer_maravilla(l)

# g. mostrar toda la información de Flash y Star-Lord

def mostrar_info_flas_y_starlord(l):
    l.add_criterion("alias", lambda x: x["alias"])
    flash_index = l.search("Flash", "alias")
    starlord_index = l.search("Star-Lord", "alias")
    if flash_index is not None:
        print(f"Información de Flash: {l[flash_index]}")
    if starlord_index is not None:
        print(f"Información de Star-Lord: {l[starlord_index]}")

print("-" * 30)
mostrar_info_flas_y_starlord(l)

# h. listar los superhéroes que comienzan con la letra B, M y S

def Listar_superheroes_con_letra_inicial(L):
    print("Superhéroes que comienzan con las letras B:")
    l.filter_start_with("B")
    print("Superhéroes que comienzan con las letras M:")
    l.filter_start_with("M")
    print("Superhéroes que comienzan con las letras S:")
    l.filter_start_with("S")
    
print("-" * 30)
Listar_superheroes_con_letra_inicial(l)

# i. determinar cuántos superhéroes hay de cada casa de comic.

def contar_superheroes_por_casa(l):
    marvel_count = 0
    dc_count = 0
    for element in L:
        if element["house"] == "Marvel":
            marvel_count += 1
        elif element["house"] == "DC":
            dc_count += 1
    print(f"Cantidad de superhéroes de Marvel: {marvel_count}")
    print(f"Cantidad de superhéroes de DC: {dc_count}")
