# Listas com as opções de alimentos
cafe_da_manha_opcoes = []
almoco_opcoes = []
jantar_opcoes = []

# Listas com alimentos que causam intolerâncias
intolerancias = {
    'lactose': ['leite', 'queijo', 'iogurte'],
    'gluten': ['pão', 'massa', 'bolo']
}

# Função para adicionar uma opção ao cardápio e verificar intolerâncias
def adicionar_opcao(nome_opcao, categoria, intolerancias):
    opcoes = {
        'cafe_da_manha': cafe_da_manha_opcoes,
        'almoco': almoco_opcoes,
        'jantar': jantar_opcoes
    }
    
    for tipo_intolerancia, alimentos in intolerancias.items():
        if any(alimento in nome_opcao.lower() for alimento in alimentos):
            print(f"Alerta: '{nome_opcao}' pode conter {tipo_intolerancia}.")
            return
    
    opcoes[categoria].append(nome_opcao)
    print(f"'{nome_opcao}' adicionado ao cardápio de {categoria}.")

# Cadastro das opções de alimentos
print("Cadastro das opções de alimentos")

# Café da Manhã
for i in range(3):
    alimento = input(f"Digite a opção de café da manhã {i+1}: ")
    adicionar_opcao(alimento, 'cafe_da_manha', intolerancias)

# Almoço
for i in range(4):
    alimento = input(f"Digite a opção de almoço {i+1}: ")
    adicionar_opcao(alimento, 'almoco', intolerancias)

# Jantar
for i in range(4):
    alimento = input(f"Digite a opção de jantar {i+1}: ")
    adicionar_opcao(alimento, 'jantar', intolerancias)

# Exibindo o cardápio
print("\nCardápio do Dia")
print("\nCafé da Manhã:")
for opcao in cafe_da_manha_opcoes:
    print(f"- {opcao}")

print("\nAlmoço:")
for opcao in almoco_opcoes:
    print(f"- {opcao}")

print("\nJantar:")
for opcao in jantar_opcoes:
    print(f"- {opcao}")
