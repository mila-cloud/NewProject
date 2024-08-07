# Demonstração do uso de funções...
def Apresentar():
    print("Meu nome é", MyName, ",")
    print("Minha altura é de", MyAge, "anos.")
    print("Minha idade é", MyAge, "anos.")
    return

def conferir(x):
    if x >=18:
        print("você é maior de idade!")
    else:
        print("ops, menor de idade não pode!")
    return

MyName = str(input("digite o seu nome: "))
MyHeigh = float(input("digite a sua altura: "))
MyAge = int(input("Digite a sua idade: "))

Apresentar()
conferir(MyAge)
    


