from stack import Stack
from random import randint

pila = Stack()

for i in range(10):
    pila.push(randint(1, 10))

# print()
# pila.show()
# print()

# search_value = int(input("Ingrese un numero para contar ocurrencias "))
# counter = 0

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         counter += 1

# print(f"cantidad de ocurrencias de {search_value} en la pila: {counter}")

# for i in range(10):
#     pila.push(randint(1, 10))

# print()
# pila.show()
# print() 

# pila_aux = Stack()

# while pila.size () > 0:
#     value = pila.pop()
#     if value % 2 == 0:
#         pila_aux.push(value)

# print()
# pila_aux.show()
# print()

# while pila_aux.size():
#     value = pila_aux.pop()
#     pila.push(value)

# pila.show

# Reemplazar todas las ocurrencias de un determinado elemento en una pila.

# for i in range(10):
#     pila.push(randint(1, 10))

# print()
# pila.show()
# print() 

# search_value = int(input("Ingrese un numero para contar ocurrencias "))
# new_value = int(input("Ingrese el nuevo valor: "))
# aux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         value = new_value
#     aux.push(value)

# aux.show()



# Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

# aux = Stack()
# pila.show()

# while pila.size() > 0:
#     value = pila.pop()
#     aux.push(value)

# print()
# aux.show()

# Determinar si una cadena de caracteres es un palíndromo.

aux = Stack()
pila.show()

while pila.size() > 0:
    value = pila.pop()
    