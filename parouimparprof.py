#demostração do uso de funçoes feito pelo professor
def Menor():
    print("Eis, os programas ideais para você:")
    print("teletubies, tom & jerri, xou da xuxa...")
    return
def MAIOR():
    print("Eis, boas opções de carro para comprar:")
    print("Fiat 147, VW Fusca, chevette...")
    return

print("Digite a sua idade:")
IDADE = int(input())

if IDADE <18:
    Menor()
else:
    MAIOR()