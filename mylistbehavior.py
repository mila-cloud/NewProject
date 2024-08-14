#Demonstração do comportamento das listas...
print("vou almoçar em um restaurante a quilo!")

ORIGINAL =["arroz", "feijão", "batata", "alface", "frango"]
print("Eis, a minha comida:", ORIGINAL)
DERIVADA = ORIGINAL
print("Meu amigo irá comer também:", DERIVADA)

print("Vou alterar as opções sem ele ver...")
ORIGINAL.remove("arroz")
ORIGINAL.remove("feijão")
ORIGINAL.remove("alface")
ORIGINAL.append("picanha")
ORIGINAL.append("linguiça")

print("Amiguinho, me mostre o que voçê vai comer?")
print("Claro! Dá uma conferida", DERIVADA)