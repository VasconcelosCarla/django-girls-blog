pessoas = {}

for i in range(1, 3):
    nome = input(f"Digite o nome da {i}º pessoa: ")
    idade = input(f"Digite a idade da {i}º pessoa: ")
    endereco = input(f"Digite seu endereço da {i}º pessoa: ")
    pessoas.setdefault(nome, [idade, endereco] )
    
for i,n in pessoas.items():
    print(f"{i} tem {n[0]} anos e mora em {n[1]}")
