# Classificação dos times campeonato

clube = input("Digite o nome do time: ")
posicao = int(input("Digite a sua posição: "))

if posicao == 1:
    print("É campeão!")
elif posicao > 1 and posicao <= 6:
    print("Libertadores da América!")
elif posicao > 6 and posicao <= 12:
    print("Sul-Americana!")
elif posicao > 12 and posicao <= 16:
    print("Sem classificação!")
elif posicao >= 17 and posicao <= 20:
    print("Rebaixado!")
else:
    print("Digite a posição correta!")

    
       