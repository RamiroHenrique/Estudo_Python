qtd_idades = int(input("quantidade de idades = "))
lista_idades = []
for i in range(0, qtd_idades, 1):
	lista_idades.append(int(input("idade = ")))
index_idade = lista_idades.index(int(input("idade para consulta = ")))
qtd_antecessores = 0
qtd_sucessores = 0
for i in range(0, index_idade, 1):
	qtd_antecessores = qtd_antecessores + 1
for i in range(index_idade - 1, -1, -1):
	qtd_sucessores = qtd_sucessores + 1
print("quantidade de antecessores = %d" %qtd_antecessores)
print("quantidade de sucessores = %d" %qtd_sucessores)
