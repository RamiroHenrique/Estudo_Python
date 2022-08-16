def palavras(texto):
	return len(texto.split())
nome = input("Nome: ")
print("quantidade de palavras = %d" %palavras(nome))
"""
"""
def verificar_data(data):
	if len(data) == 10:
		aux_vet = data.split('/')
		dia = int(aux_vet[0])
		mes = int(aux_vet[1])
		ano = int(aux_vet[2])
		return dia, mes, ano
	else:
		print("Erro: formato inválido")
		return 0, 0, 0
dia, mes, ano = verificar_data("18/03/1996")
print("dia:%d" %dia)
print("mes:%d" %mes)
print("ano:%d" %ano)
