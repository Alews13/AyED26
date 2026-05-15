# Eliminar el i-ésimo elemento despues del frente de la cola.

from random import randint
from queue_ import Queue
from typing import Any

queue_number = Queue()

for i in range (0, 20):
    queue_number.arrive(randint(0, 20))

wanted_to_delete = int(input("Ingrese la posición que quiere eliminar: "))

queue_number.show()

while queue_number.size() > 0:
    for x in range(20):
        if x == wanted_to_delete:
            queue_number.attention()
        else:
            queue_number.move_to_end()


print("----------------------------------------")
queue_number.show()