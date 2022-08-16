lista_nomes = []
continuar_executando = True
while continuar_executando:
	nome = ""
	nome = input("nome = ")
	if nome != "":
		lista_nomes.append(nome)
	else:
		continuar_executando = False
continuar_executando = True
while continuar_executando:
	letra = ""
	letra = input("letra = ")
	if letra != "":
		for i in range(0, len(lista_nomes), 1):
			aux_nome = lista_nomes[i]
			if aux_nome[0] == letra:
				print(aux_nome)
	else:
		continuar_executando = False
