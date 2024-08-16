# Demonstração de oop em python...
class CLIENTE:
    def __init__(self,TITULAR, CONTA, SALDO):
        self.TITULAR = TITULAR
        self.CONTA = CONTA
        self.SALDO = SALDO

class cliente_FISICO(CLIENTE):
    def APRESENTAR(self):
        print("Olá! Eu sou:", self.TITULAR)
        print("Minha conta é:", self.CONTA)
        print("E quero saber o meu saldo.")
        return
    
#Para criar uama instância baseada na classe cliente...
FULANO = cliente_FISICO("João","423.050205-21", 25000.00)

FULANO.APRESENTAR()

#Acessando os atributos das instâcias criadas...
print("De fato, você realmente é:", FULANO.TITULAR)
print("No momento,a sua conta possui RS",FULANO.SALDO)