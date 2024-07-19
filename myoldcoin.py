# Demostração do uso da condicional match/case...
print("Digite o número referente ao estado da moeda:")
print("1. flor de cunho")
print("2. soberba")
print("3. muito bem conservada")
print("4. bem conservado")
print("5. outros estados")
Estado = int(input())

match Estado:
    case 1:
        print("perfeita!vou pagar R$ 1.000.000,00!")
    case 2:
        print("Quase perfeita! ofereço R$ 250.000,00!")
    case 3:
        print("Que ótimo! posso dar uns R$ 100.000,00!")
    case 4:
        print("Que bom aceitaria R$ 30.000,00!")
    case 5:
         print("Desculpa, não aceito neste estado.")
    case 6:
        print("opção não reconhecida!")
        

 

      