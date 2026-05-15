# Trabajaremos utilizando listas que no son las originales de python, funcionan igual de todas maneras.

from typing import Any

class List(list):

    def show(self) -> None:
        for element in self:
            print(element)

    def search(self, search_value: Any):
        is_in_list = search_value in self
        return search_value in self, self.index(search_value)if is_in_list else None
        

l = List()

l.append(3)
l.append(1)
l.append(5)

print(l.search(2))

l.show()