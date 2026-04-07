# 5 + 4 + 3 + 2 + 1

def suma(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num + suma(num-1)
    
# print(suma(5))

# Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado. Con recursividad

def prod(num1: int, num2: int) -> int:
    if num2 == 0:
        return 0
    else:
        return num1 + prod(num1, num2-1)

# print(prod(1,3))

def serie(n: float) -> float:
    if n == 1:
        return 1
    else:
        return 1/n + serie(n-1)
    
# print(serie(4))

# Implementar una función para calcular la potencia dado dos números enteros, el primero re-presenta la base y segundo el exponente.



def potencia(base: int, exponente: int) -> int:
    if base == 0:
        return 0
    elif exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)
    
# print(potencia(2,4))

# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def contar_cifras(n:int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + contar_cifras(n // 10)

# print(contar_cifras(0))

# Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

#

def invertir_numero(n: int) -> int:
    if n < 10:
        return n
    else:
        return 


# Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.


# Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir_cadena(cadena: str) -> str:
    if cadena == '':
        return ''
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
    
# print(invertir_cadena("pija"))