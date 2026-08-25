
from typing import Any
import copy

class Stack:

    def __init__(self):
        self.__elements = [] #lista 

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:  
        return self.__elements.pop()
    
    def pila_vacia(self) -> bool:
        if self.__elements == []:
            return print(True)
        else:
            return print(False)

    def show(self) -> None: #sacar
        stack_aux = Stack()
        stack_aux.__elements = copy.copy(self.__elements) 
        
        while stack_aux.size() > 0:
            value = stack_aux.pop()
            print(value)

    def size(self) -> int:
        return len(self.__elements)
    
    def cima_pila(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]
