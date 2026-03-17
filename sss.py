#print("hola mundo", "desde piton") # print se utiliza para imprimr todos los datos que queramos

#name = input('ingrese su nombre: ')

#print('su nombre es:', name)

# TIPOS DE DATOS PRIMITIVOS: STR, INT, FLOAT, BOOL, NONE
#variable = 'Ana'
#print(type[variable])
#variable = 1234
#print(type[variable])
#variable = 12.5
#print(type[variable])
#variable = True
#print(type[variable])

#number = int(input('ingrese un numero: '))
#print(number + 100)

# Funciones de conversion: int, str, float, bool(input'...')
# Estas convierten un tipo de dato a otro
# Funciones aritmeticas +,-,*,/, //, %, **
#print(5-2)
#print(5 + 2)
#print( 5*2)
#print(5 / 2)
##print(5 % 2)
#print(5 ** 2)

# asignacion = a = 10

#secuencial
#condicional
# if - else | case
# operadores de control <, > , <=, >=
# num = 10
# if num > 5:
#     print("hola")
#     print("5 es menor a 10")
#     print("dentro del if")
# print("fuera del if")

# if num > 5:
#     print("es mayor")
# elif num < 5:
#     print("es menor")
# else:
#     print("es 5")

# operadores logicos and or not ^

# if num > = 5 and num <= 10:
#       print (" el nuero esta entre 5 y 10")

# control = True
# if control: # no hace falta por si control == True, como es booleana solo con poner la variable ya alcanza
#     print("se cumple el control")

# match num :
#       case 1: print("es uno")
#       case 5: print("5")


# ciclo
    # for | while
# num = 1
# while num < 5:
#     print (num)
#     num = num + 1 # es igual a num+= 1
    
# for i in range(0,9,2):
#      print(i)

# estructuras list, dic, tuple

# num_list = [1,2,3,4,"hola",True,None]

# num_list = []

# print(type(num_list))
# print(len(num_list))

# num_list.append(1) # append surve para agregar cosas a la lista
# num_list.append(7)
# num_list.append(3)
# num_list.append(2)

# print(num_list.clear)

# print(num_list.count(9))


# print(num_list.index(7)) # nos devuelve la ubiación del primer que nos encuentre de lo que le indiquemos
# print(num_list.insert(2,9)) #nos sirve para insertar elementos en un lugar a nuestra elección y corre las valores que sigan una posicion a la derecha

# print(num_list)

# print(num_list.pop(2)) #con el pop podemos eliminar un indice a elección, si no se lo pasamos remueve el ultimo

# num_list.remove(9) #parecido al pop, pero elimina el primer valor igual al que le pasemos

# print(num_list)
# print(num_list.reverse) # invierte la lista

# print(num_list.sort(reverse=True)) # ordena la lista de menor a mayor y requiere que todos los elemtnos sean de l mismo tipo el reverse para invertir

# print(num_list[4])  se pone entre [] el valor del index al que queremos acceder
      

# nums = [1,2,3,4,5]
# nums.append(100)
# nums.reverse

# for num in nums:
#     print(num)

# for i in range(len(nums-1, 0, -1)):
#     print(nums[i])

# for i in range (len(nums)): utiliznaod len(nums) hacemos que siempre el rangos ea el largo total de la lista
#     print(nums[i])

# for index,number in enumerate(nums):
#     print("posicion", index, "valore",number)



# funciones y modulo

# def mi_funcion(num1, num2, otro= "hola wachin"):
#     print("q onda pa")

#     num1 = num1 * 2
#     return num1 + num2, num1 - num2

# n1 = 5
# n2= 3
# lista_nums = []
# suma, diferencia= mi_funcion(n1,n2,"nuevo mensaje")

# print(suma, "|", diferencia)

# print(lista_nums)

#            import

# from math import sqrt, factorial
# from math import sqrt as raiz_cuadrada

# from mi_modulo import suma

# print(suma(1,2))

# print(raiz_cuadrada(16))
# print(suma(2,2))
# print(factorial(5))


# # diccionarios clave -> valor
# dic = {32: "juan", 45: "ana", 12: "pepe"}
# print(type(dic))

# print(dic.get(32)) # nos da el valor segun la clave que le pasemos

# print(dic.keys()) # nos da todas las claves en el dic

# print(dic.values()) # nos da todos los valores sin las keys

# print(dic.items()) # nos da cada valor con su llave

# dic[99] = "maria" # sirve para agregar un valor con una llave


# dic.pop(32) # borra el value segun la key que le pasemos

# print(dic)

print("hola")