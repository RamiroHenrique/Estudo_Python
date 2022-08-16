nome = input("Nome = ")
vetor_nomes = nome.split(" ")
nome_autor = vetor_nomes[len(vetor_nomes) - 1] + ", " + vetor_nomes[0] + " "
i = 1
while i < len(vetor_nomes) - 1:
	palavra = vetor_nomes[i]
	if palavra != "de" and palavra != "da":
		nome_autor = nome_autor + palavra[0] + ". "
	i = i + 1
print(nome_autor)
