# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

mochila = ["comida", "sable de luz", "peron", "hitler"]

def usar_la_fuerza(mochila: list, indice=0):
    if indice >= len(mochila):
        return False
    
    if mochila[indice] == "sable de luz":
        return True, indice + 1
    
    return usar_la_fuerza(mochila, indice + 1)

encontrado, pos = usar_la_fuerza(mochila) 

if encontrado == True:
    print(f"Se encontró el Sabe de Luz y se necesitaron sacar {pos} objetos")
elif pos == 0:
    print("La mochila está vacía")
else:
    print("No se encontró el sable de luz en la mochila")