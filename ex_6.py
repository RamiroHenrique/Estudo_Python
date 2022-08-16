lista_numeros = []
continuar_executando = True
while continuar_executando:
	numero = int(input("numero = "))
	if numero != 0:
		lista_numeros.append(numero)
	else:
		continuar_executando = False
numero_consulta = int(input("número para consulta = "))
posicao_numero = lista_numeros.index(numero_consulta)
print("posição do elemento = %d" %posicao_numero)
