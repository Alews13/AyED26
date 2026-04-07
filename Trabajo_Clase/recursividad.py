# FACTORIAL !
# factorial(5) = 5 * 4 * 3 * 2 * 1
# 5!

# fac(5) = 5 * fac(4)
# fac(4) = 4 * fac(3)
# fac(3) = 3 * fac(2)
# fac(2) = 2 * fac(1)
# fac(N) = N * fac(N-1) -> fac (0) = 1

# def factorial_r(num: int) -> int:
#     print(f"calcular factorial de {num}")
#     if num == 0:
#         print("se alcanzó condición de fin, devolver valor por defecto")
#         a = input()
#         return 1
#     else:
#         print(f"resolucion parcial para {num}, hacer llamada recursiva con {num -1}")
#         a = input()
#         temporal = num *factorial_r(num -1)
#         print(f"fin solucion parcial para {num} con resultado {temporal}")
#         a = input()
#         return temporal

# def factorial(num: int) -> int:
#     res = 1
#     for i in range(1, num+1):
#        res = res * i
#     return res

# print(factorial(5))
# print(factorial_r(5))

# fibonacci
# manera recursiva

def fibonacci_r(num: int) -> int:
    if num == 0 or num == 1:
        return num
    else: 
        return fibonacci_r(num-1) + fibonacci_r(num-2)

# manera interativa
def fibonacci(num):
    fib_1 = 0
    fib_2 = 1
    for i in range(2, num+1):
        fib_aux = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 =fib_aux

    return fib_aux

print(fibonacci(33))
print(fibonacci_r(50))