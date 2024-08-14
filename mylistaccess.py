#Demostração de acesso a listas...

print("vou montar a marmita com 5 alimentos!")
MARMITA = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa recomendação:", MARMITA)

RESPOSTA = input("você quer montar uma marmita diferente (s/n)?")
if RESPOSTA == "5":
    for X in range(0,5):
     print(f'Digite o {X+1}o. item do cardápio:')
     MARMITA[X] = input()
    print("A marmita montada foi:", MARMITA)
    print(" O três primeiros itens foram:", MARMITA[0:3])
    print("O último item da marmita foi:", MARMITA)
else:
   print("ok. você decide...")


                 