#exercicios par ou impar modelo chatgpt

import random

def jogar_par_ou_impar():
    # O computador gera um número aleatório entre 1 e 10
    numero_computador = int(input("Digite um número aleatório (1 a 10) para o computador: "))

    # O usuário digita o seu número
    numero_usuario = int(input("Digite seu número: "))

    # Calcula a soma dos números
    soma = numero_computador + numero_usuario

    # Verifica se a soma é par ou ímpar
    if soma % 2 == 0:
        resultado = "par"
        vencedor = "Você venceu!"
    else:
        resultado = "ímpar"
        vencedor = "O computador venceu!"

    # Exibe o resultado
    print(f"A soma dos números é {soma}, que é {resultado}.")
    print(vencedor)

def main():
    print("Bem-vindo ao jogo de Par ou Ímpar!")
    jogar_par_ou_impar()

if __name__ == "__main__":
    main()