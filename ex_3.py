nome = input("Nome = ")
vetor_vogais_presentes = ""
num_vogais = 0
vetor_consoantes_presentes = ""
num_consoantes = 0
vogal_nao_encontrada = True
vetor_vogais = "aeiouAEIOU"
i = 0
while i < len(nome):
	j = 0
	while j < len(vetor_vogais):
		if nome[i] == vetor_vogais[j]:
			vetor_vogais_presentes = vetor_vogais_presentes + vetor_vogais[j]
			num_vogais = num_vogais + 1
			vogal_nao_encontrada = False
		j = j + 1
	if vogal_nao_encontrada and nome[i] != " ":
		vetor_consoantes_presentes = vetor_consoantes_presentes + nome[i]
		num_consoantes = num_consoantes + 1
	vogal_nao_encontrada = True
	i = i + 1


print("Vogais = " + vetor_vogais_presentes + " (%d)" %num_vogais)
print("Consoantes = " + vetor_consoantes_presentes + " (%d)" %num_consoantes)
print("Total de letras = %d" %len(nome))
