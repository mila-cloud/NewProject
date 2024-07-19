# correção exercicios serviços
EXECUCAO = input("O serviço foi feito (sim/não)? ")
AVALIACAO = int(input("qual a nota da avaliação (1/5)?"))

if EXECUCAO == "sim" and AVALIACAO == 1:
    print("o serviço foi péssimo!")
elif EXECUCAO == "sim" and AVALIACAO == 2:
    print("o serviço foi ruim!")
elif EXECUCAO == "sim" and AVALIACAO == 3:
    print("o serviço foi razoável")
elif EXECUCAO == "sim" and AVALIACAO == 4:
    print("o serviço foi bom!")
elif EXECUCAO == "sim" and AVALIACAO == 5:
    print("o serviço foi ótimo!")
else:
    if EXECUCAO == "não" and AVALIACAO == 0:
        RECLAMACAO = input("digite sua reclamação!")
    else:
        print("as avaliaçoes não fazem sentido!")       