# EXEMPLO 1:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {12345678: "Paulo", 
            88888888: "Maria", 
            4565456: "João"}

print(cadastro)
print(cadastro[12345678])

# Adicionar os dados de uma pessoa no dicionario
cadastro[7777777] = "Fernando"
print(cadastro)

# Alterar o Nome de uma pessoa
cadastro[12345678] = "Paulo Vieira"
print(cadastro)

# Excluir os dados de uma pessoa
cadastro.pop(12345678)
print(cadastro)

# Verificar se chave existe no dicionário
if 7777777 in cadastro:
    cadastro.pop(7777777)	# se existir, exclui
else:
    print("Chave inexistente")
print(cadastro)
    
# Percorrer o dicionario
for a in cadastro:
    print("CPF:", a, "- Nome:", cadastro[a])


# preencher dicionário com dados informados pelo usuário
cadastro = {}
for a in range(3):
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    cadastro[cpf] = nome
print(cadastro)

# EXEMPLO 2:
# Dicionario para armazenar o nome de um aluno e uma lista com 5 notas
alunos = {"Paulo": [9, 8, 7, 4, 10], 
          "Maria": [8, 3, 8, 9, 10], 
          "Pedro": [10, 7, 6, 4, 8]}

# Exibir lista de notas de um aluno
print(alunos["Paulo"])

# Inserir uma nova nota para um aluno 
alunos["Paulo"].append(10)
print(alunos)

# Substituir a lista de notas por uma nota vazia
alunos["Paulo"] = []

