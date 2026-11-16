
from tree import BinaryTree


arbol = BinaryTree()


# CARGA DE DATOS
# derrotado_por: personaje que derroto a la criatura
# capturada: personaje que capturo a la criatura
# descripcion: descripcion de la criatura


criaturas = [
    ('Ceto', '-'),
    ('Tifón', 'Zeus'),
    ('Equidna', 'Argos Panoptes'),
    ('Dino', '-'),
    ('Perifedo', '-'),
    ('Enio', '-'),
    ('Escila', '-'),
    ('Caribdis', '-'),
    ('Euríale', '-'),
    ('Esteno', '-'),
    ('Medusa', 'Perseo'),
    ('Ladón', 'Heracles'),
    ('Águila del Cáucaso', '-'),
    ('Quimera', 'Belerofonte'),
    ('Hidra de Lerna', 'Heracles'),
    ('León de Nemea', 'Heracles'),
    ('Esfinge', 'Edipo'),
    ('Dragón de la Cólquida', '-'),
    ('Cerbero', '-'),
    ('Cerda de Cromión', 'Teseo'),
    ('Ortro', 'Heracles'),
    ('Toro de Creta', 'Teseo'),
    ('Jabalí de Calidón', 'Atalanta'),
    ('Carcinos', '-'),
    ('Gerión', 'Heracles'),
    ('Cloto', '-'),
    ('Láquesis', '-'),
    ('Átropos', '-'),
    ('Minotauro de Creta', 'Teseo'),
    ('Harpías', '-'),
    ('Argos Panoptes', 'Hermes'),
    ('Aves del Estínfalo', '-'),
    ('Talos', 'Medea'),
    ('Sirenas', '-'),
    ('Pitón', 'Apolo'),
    ('Cierva de Cerinea', '-'),
    ('Basilisco', '-'),
    ('Jabalí de Erimanto', '-')
]


for nombre, derrotado in criaturas:
    arbol.insert_node(nombre, {
        'derrotado_por': derrotado,
        'descripcion': 'Sin descripción cargada',
        'capturada': '-'
    })


# A. LISTADO INORDEN DE LAS CRIATURAS
# Y QUIENES LAS DERROTARON

def inorden(root):

    if root is not None:
        inorden(root.left)

        print(root.value, '| Derrotado por:',
              root.other_values['derrotado_por'])

        inorden(root.right)


print('--- LISTADO INORDEN ---')
inorden(arbol.root)


# B. CARGAR DESCRIPCION DE UNA CRIATURA

def cargar_descripcion(nombre, descripcion):

    aux = arbol.search(nombre)

    if aux is not None:
        aux.other_values['descripcion'] = descripcion
        print('Descripcion cargada correctamente')
    else:
        print('Criatura no encontrada')


# Ejemplo de carga de descripcion

cargar_descripcion('Talos', 'Gigante de bronce que protegía Creta')


# C. MOSTRAR TODA LA INFORMACION DE TALOS

print()
print('--- INFORMACION DE TALOS ---')

aux = arbol.search('Talos')

if aux is not None:
    print('Criatura:', aux.value)
    print('Derrotado por:', aux.other_values['derrotado_por'])
    print('Descripcion:', aux.other_values['descripcion'])
    print('Capturada por:', aux.other_values['capturada'])


# D. DETERMINAR LOS 3 HEROES O DIOSES
# QUE DERROTARON MAYOR CANTIDAD DE CRIATURAS

def contar_derrotas(root, derrotas):

    if root is not None:

        derrotado = root.other_values['derrotado_por']

        if derrotado != '-':
            if derrotado not in derrotas:
                derrotas[derrotado] = 0

            derrotas[derrotado] += 1

        contar_derrotas(root.left, derrotas)
        contar_derrotas(root.right, derrotas)


print()
print('--- TOP 3 HEROES O DIOSES ---')

derrotas = {}

contar_derrotas(arbol.root, derrotas)

ordenados = sorted(
    derrotas.items(),
    key=lambda x: (-x[1], x[0])
)

for nombre, cantidad in ordenados[:3]:
    print(nombre, '| Criaturas derrotadas:', cantidad)


# E. LISTAR CRIATURAS DERROTADAS POR HERACLES

def derrotadas_por(root, nombre):

    if root is not None:

        derrotadas_por(root.left, nombre)

        if root.other_values['derrotado_por'] == nombre:
            print(root.value)

        derrotadas_por(root.right, nombre)


print()
print('--- CRIATURAS DERROTADAS POR HERACLES ---')
derrotadas_por(arbol.root, 'Heracles')


# F. LISTAR CRIATURAS QUE NO HAN SIDO DERROTADAS

def no_derrotadas(root):

    if root is not None:

        no_derrotadas(root.left)

        if root.other_values['derrotado_por'] == '-':
            print(root.value)

        no_derrotadas(root.right)


print()
print('--- CRIATURAS NO DERROTADAS ---')
no_derrotadas(arbol.root)


# G. CADA NODO YA TIENE EL CAMPO CAPTURADA
# H. INDICAR QUE HERACLES CAPTURO CUATRO CRIATURAS

print()
print('--- CRIATURAS CAPTURADAS POR HERACLES ---')

criaturas_capturadas = [
    'Cerbero',
    'Toro de Creta',
    'Cierva de Cerinea',
    'Jabalí de Erimanto'
]

for nombre in criaturas_capturadas:

    aux = arbol.search(nombre)

    if aux is not None:
        aux.other_values['capturada'] = 'Heracles'
        print(nombre, '| Capturada por:',
              aux.other_values['capturada'])


# I. BUSQUEDA POR COINCIDENCIA

def busqueda_proximidad(root, nombre):

    if root is not None:

        busqueda_proximidad(root.left, nombre)

        if nombre.lower() in root.value.lower():
            print(root.value)

        busqueda_proximidad(root.right, nombre)


print()
print('--- BUSQUEDA POR COINCIDENCIA ---')

busqueda_proximidad(arbol.root, 'creta')


# J. ELIMINAR BASILISCO Y SIRENAS

print()
print('--- ELIMINAR CRIATURAS ---')

eliminadas = ['Basilisco', 'Sirenas']

for nombre in eliminadas:

    aux = arbol.delete_node(nombre)

    if aux[0] is not None:
        print('Criatura eliminada:', nombre)
    else:
        print('No se encontro:', nombre)


# K. MODIFICAR AVES DEL ESTINFALO

print()
print('--- MODIFICAR AVES DEL ESTINFALO ---')

aux = arbol.search('Aves del Estínfalo')

if aux is not None:
    aux.other_values['derrotado_por'] = 'Heracles (varias)'
    print('Informacion modificada correctamente')


# L. MODIFICAR NOMBRE DE LADON

print()
print('--- MODIFICAR NOMBRE DE LADON ---')

aux = arbol.search('Ladón')

if aux is not None:

    informacion = aux.other_values

    arbol.delete_node('Ladón')
    arbol.insert_node('Dragón Ladón', informacion)

    print('Nombre modificado: Dragón Ladón')


# M. LISTADO POR NIVEL DEL ARBOL

print()
print('--- LISTADO POR NIVEL ---')

arbol.by_level()
