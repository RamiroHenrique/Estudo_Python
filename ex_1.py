nome = input("Nome = ")
vetor_palavras = nome.split(" ")
i = 0
abreviatura = ""
while i < len(vetor_palavras):
	palavra = vetor_palavras[i]
	abreviatura = abreviatura + palavra[0] + ". "
	i = i + 1
print(abreviatura)
