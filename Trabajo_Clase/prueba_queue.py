from random import randint
from queue_ import Queue

queue_numbers= Queue()

for i in range(20):
    queue_numbers.arrive(randint(0,20))

queue_numbers.show()
counter = 0

search_value = int(input("Ingrese el numero que quiere determinar la cantidad de ocurrencias: "))

for i in range(queue_numbers.size()):
    if queue_numbers.on_front() == search_value:
        counter += 1

    queue_numbers.move_to_end()

print(f"la cantidad de ocurrencias de {search_value} en la cola es {counter}")


# queue_letters = Queue()

# for i in range(15):
#     queue_letters.arrive(chr(randint(97, 122)))

# queue_letters.show()
# print()

