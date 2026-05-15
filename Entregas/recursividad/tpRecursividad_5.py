# Desarrollar una función que permita convertir un número romano en un número decimal.

# Utilizamos dos funciones, una para resolver que numero es cada simbolo y otra para encontrar el valor del numero romano.

def valor_simbolo(caracter: str) -> int:
    if caracter == "I":
        return 1
    elif caracter == "V":
        return 5
    elif caracter == "X":
        return 10
    elif caracter == "C":
        return 100
    elif caracter == 'D':
        return 500
    elif caracter == 'M':
        return 1000
    else:
        return 0 
    
def romano_a_decimal(romano: str) -> int:
    if romano == "":
        return 0
    
    if len(romano) == 1:
        return valor_simbolo(romano[0])
    
    primero = valor_simbolo(romano[0])
    segundo = valor_simbolo(romano[1])

    if primero < segundo:
        return -primero + romano_a_decimal(romano[1:])
    else:
        return primero + romano_a_decimal(romano[1:])


print(romano_a_decimal("III"))    
print(romano_a_decimal("IV"))      
print(romano_a_decimal("IX"))      
print(romano_a_decimal("LVIII"))   
print(romano_a_decimal("MCMXCIV")) 
print(romano_a_decimal("MMXXIV"))