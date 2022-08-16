lista_pessoa = []
permanecer_executando = ""
while permanecer_executando != "n" and permanecer_executando != "N":
	nome = input("nome = ")
	idade = int(input("idade = "))
	lista_pessoa.append([nome, idade])
	permanecer_executando = input("Continuar [S/N] = ")
for i in range(0, len(lista_pessoa), 1):
	for j in range(0, len(lista_pessoa), 1):
		if lista_pessoa[i][1] > lista_pessoa[j][1]:
			pessoa_aux = lista_pessoa[i]
			lista_pessoa[i] = lista_pessoa[j]
			lista_pessoa[j] = pessoa_aux
print(lista_pessoa)
