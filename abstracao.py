#Demonstração de oop em python
from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __init__(self,TITULAR,CONTA,SALDO):
        self.TITULAR = TITULAR
        