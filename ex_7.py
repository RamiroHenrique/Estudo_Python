lista_conceitos = []
continuar_executando = True
qtd_aprovados = 0
qtd_reprovados = 0
qtd_infrequentes = 0
while continuar_executando:
	conceito = input("conceito do aluno = ")
	if conceito != "F" and conceito != "f":
		lista_conceitos.append(conceito)
	else:
		continuar_executando = False
for i in range(0, len(lista_conceitos), 1):
	if lista_conceitos[i] == "A" or lista_conceitos[i] == "B" or lista_conceitos[i] == "C":
		qtd_aprovados = qtd_aprovados + 1
	elif lista_conceitos[i] == "D":
		qtd_reprovados = qtd_reprovados + 1
	else:
		qtd_infrequentes = qtd_infrequentes + 1
print("%d aprovados" %qtd_aprovados)
print("%d reprovados" %qtd_reprovados)
print("%d infrequentes" %qtd_infrequentes)
