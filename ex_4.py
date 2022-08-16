letra = ""
continuar_executando = True
lista_letras = []
lista_letras_invertida = []
while continuar_executando:
	letra = input("letra = ")
	if letra != "":
		lista_letras.append(letra)
	else:
		continuar_executando = False
for i in range(len(lista_letras) -1, -1, -1):
	lista_letras_invertida.append(lista_letras[i])
print(lista_letras)
print(lista_letras_invertida)
