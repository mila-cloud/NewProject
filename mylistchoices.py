# Demonstração de funções em listas...
print("Eis, os meus maiores sonhos...")
SONHOS = ["1. Me divertir na Disney",
          "2. Me banhar na praia de sepetiba",
          "3.Tirar as férias em paris",
          "4. Fazer compras no westshopping",
          "5. Ver as pirâmides do egito"]
for X in SONHOS:
    print(X)

print("Ops, não quero Sepetiba!")
del(SONHOS[1])
print("E nem Westshopping...")
del(SONHOS[3])

print("Conferindo os sonhos...")
for X in SONHOS:
    print(X)


            