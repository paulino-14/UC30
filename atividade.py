# Criando o dicionário
aluno = {}

# Entrada de dados
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["nota1"] = float(input("Digite a nota da prova 1: "))
aluno["nota2"] = float(input("Digite a nota da prova 2: "))

# Calculando a média
media = (aluno["nota1"] + aluno["nota2"]) / 2

# Adicionando a média ao dicionário
aluno["media"] = media

# Verificando a situação
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Mostrando os dados
print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("Situação:", situacao)