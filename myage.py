# Demostração do uso de if/elif/else...
print("Digite a sua idade:")
IDADE = int(input())

if IDADE < 18:
    print("você não é maior de idade!")
    print("Não poderá realizar a operação!")
elif IDADE >= 65:
    print("você já está pronto para se aposentar?")
    print("poderemos oferecer suporte técnico...")
else:
     print("você é maior de idade.")
     print("portanto,poderá realizar a operação.")

     print("obrigado por optar pelos nossos serviços!")
     
