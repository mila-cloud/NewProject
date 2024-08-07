# Demostração do uso de funções... 
def ADICAO(X, Y):
    return X + Y
def SUBTRACAO(X,Y):
    return X - Y

print("Digite dois valores inteiros...")
N1 = int (input("X: "))
N2 = int (input("Y: "))
OP = input("qual operação (+ ou -)?")

if OP == "+":
    Z = ADICAO(N1,N2)
    print("Resultado da soma:", Z)
elif OP == "-":
    Z = SUBTRACAO(N1, N2)
    print("Resultado da subtração:",Z)
else:
    print("opção digite inesxistente!")

