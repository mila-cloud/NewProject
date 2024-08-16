#Demonstração de aula de aula cardápio com lista...
print("Vamos montar um cardápio personalizado?")

BREAKFAST = []
LUNCH = []
DINNER = []

for X in range(0,3):
    OPCAO = input(f"Digite a {X+1}:")
    BREAKFAST.append(OPCAO)
    if OPCAO == "leite" or OPCAO == "queijo" or OPCAO == "pão":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas:", BREAKFAST)

print("Almoço:")
for X in range (0,4):
    OPCAO = input(f"Digite a opção {X+1}:")
    LUNCH.append(OPCAO)
    if OPCAO == "camarão" or OPCAO == "pimenta":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas:" , LUNCH)

print("jantar:")
for X in range (0,4):
    OPCAO = input(f"Digite a opção {X+1}:")
    DINNER.append(OPCAO)
    if OPCAO == "camarão" or OPCAO == "pimenta":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas:", DINNER)