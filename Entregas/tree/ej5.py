
from tree import BinaryTree


arbol = BinaryTree()


# CARGA DE DATOS
# True = villano
# False = superheroe

personajes = [
    ('Iron Man', False),
    ('Captain America', False),
    ('Thor', False),
    ('Hulk', False),
    ('Black Widow', False),
    ('Hawkeye', False),
    ('Doctor Strang', False),
    ('Spider-Man', False),
    ('Black Panther', False),
    ('Captain Marvel', False),
    ('Scarlet Witch', False),
    ('Ant-Man', False),
    ('Wasp', False),
    ('Vision', False),
    ('Falcon', False),
    ('Thanos', True),
    ('Loki', True),
    ('Ultron', True),
    ('Green Goblin', True),
    ('Red Skull', True),
    ('Hela', True),
    ('Killmonger', True),
    ('Doctor Doom', True),
    ('Kang', True)
]


for nombre, villano in personajes:
    arbol.insert_node(nombre, {'is_villain': villano})


# B. LISTAR VILLANOS ORDENADOS ALFABETICAMENTE

def inorden_villain(root):

    if root is not None:
        inorden_villain(root.left)

        if root.other_values['is_villain']:
            print(root.value)

        inorden_villain(root.right)


print('--- VILLANOS ---')
inorden_villain(arbol.root)


# C. MOSTRAR SUPERHEROES QUE EMPIEZAN CON C

def inorden_hero_star_with(root, prefix):

    if root is not None:
        inorden_hero_star_with(root.left, prefix)

        if root.value.startswith(prefix) and not root.other_values['is_villain']:
            print(root.value)

        inorden_hero_star_with(root.right, prefix)


print()
print('--- HEROES QUE EMPIEZAN CON C ---')
inorden_hero_star_with(arbol.root, 'C')


# D. CONTAR SUPERHEROES

print()
print('--- CANTIDAD DE SUPERHEROES ---')
print('Cantidad:', arbol.count_heroes())


# E. BUSQUEDA POR PROXIMIDAD Y MODIFICACION

def proxy_search(root, prefix):

    if root is not None:

        aux = proxy_search(root.left, prefix)

        if aux is not None:
            return aux

        if prefix.lower() in root.value.lower():
            return root

        return proxy_search(root.right, prefix)

    return None


print()
print('--- BUSQUEDA DE DOCTOR STRANGE ---')

busqueda = proxy_search(arbol.root, 'stran')

if busqueda is not None:

    print('Personaje encontrado:', busqueda.value)

    nombre_anterior = busqueda.value
    informacion = busqueda.other_values

    arbol.delete_node(nombre_anterior)
    arbol.insert_node('Doctor Strange', informacion)

    print('Nombre corregido: Doctor Strange')

else:
    print('Personaje no encontrado')


# F. SUPERHEROES EN ORDEN DESCENDENTE

print()
print('--- HEROES EN ORDEN DESCENDENTE ---')
arbol.postorden_hero()


# G. GENERAR UN BOSQUE

arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()


def generar_bosque(root):

    if root is not None:

        if root.other_values['is_villain']:
            arbol_villanos.insert_node(root.value, root.other_values)
        else:
            arbol_heroes.insert_node(root.value, root.other_values)

        generar_bosque(root.left)
        generar_bosque(root.right)


generar_bosque(arbol.root)


# G-I. CANTIDAD DE NODOS DE CADA ARBOL

def contar_nodos(root):

    if root is None:
        return 0

    return 1 + contar_nodos(root.left) + contar_nodos(root.right)


print()
print('--- CANTIDAD DE NODOS DEL BOSQUE ---')

print('Superheroes:', contar_nodos(arbol_heroes.root))
print('Villanos:', contar_nodos(arbol_villanos.root))


# G-II. BARRIDO ORDENADO ALFABETICAMENTE

def barrido_inorden(root):

    if root is not None:
        barrido_inorden(root.left)
        print(root.value)
        barrido_inorden(root.right)


print()
print('--- ARBOL DE SUPERHEROES ---')
barrido_inorden(arbol_heroes.root)

print()
print('--- ARBOL DE VILLANOS ---')
barrido_inorden(arbol_villanos.root)
